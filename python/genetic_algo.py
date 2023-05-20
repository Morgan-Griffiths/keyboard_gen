from random import shuffle
import numpy as np
from datatypes import CHANGEABLE_KEYS, REMAINING_MODIFIER_KEYS
from utils import display_keyboard, keyboard_cost
from config import Config


class GenericKeyboardSearch:
    def __init__(self,training_data,cost_matrix):
        config = Config()
        self.population_size = config.population_size
        self.mutation_rate = config.mutation_rate
        self.num_generations = config.num_generations
        self.survival_rate = config.survival_rate
        self.parent_selection_rate = config.parent_selection_rate
        self.random_portion = config.random_portion
        self.cost_matrix = cost_matrix
        self.text = training_data

    def randomly_permute_keyboard(self):
        result = np.random.choice(CHANGEABLE_KEYS, size=len(CHANGEABLE_KEYS), replace=False)
        translation_dictionary = {k:v for k,v in zip(result,CHANGEABLE_KEYS)}
        translation_dictionary |= {k:v for k,v in zip(REMAINING_MODIFIER_KEYS,REMAINING_MODIFIER_KEYS)}
        # print('randomly_permute_keyboard',translation_dictionary)
        return translation_dictionary

    def random_half_keyboard(self,keyboard):
        new_keyboard = keyboard.copy()
        same_keys = np.random.choice(CHANGEABLE_KEYS, size=len(CHANGEABLE_KEYS)//2, replace=False)
        other_keys = [key for key in CHANGEABLE_KEYS if key not in same_keys]
        values = [keyboard[key] for key in other_keys]
        shuffle(values)
        new_keyboard.update({k:v for k,v in zip(other_keys,values)})
        return new_keyboard

    def generate_population(self):
        population = []
        for i in range(self.population_size):
            population.append(self.randomly_permute_keyboard())
        return population

    def mutate_keyboard(self,keyboard):
        new_keyboard = keyboard.copy()
        for key in new_keyboard:
            if np.random.random() < self.mutation_rate:
                # randomly swap two keys
                key1,key2 = np.random.choice(CHANGEABLE_KEYS,replace=False,size=2)
                new_keyboard[key1],new_keyboard[key2] = new_keyboard[key2],new_keyboard[key1]
        return new_keyboard

    def mutate_population(self,population):
        new_population = population
        random_keyboards = [self.random_half_keyboard(np.random.choice(population)) for _ in range(int(self.random_portion * self.population_size))]
        for _ in range(int(self.population_size * self.parent_selection_rate)):
            new_population.append(self.mutate_keyboard(np.random.choice(population)))
        return new_population + random_keyboards

    def select_k_best(self,population):
        costs = [keyboard_cost(self.text,self.cost_matrix,keyboard) for keyboard in population]
        # print('costs',costs)
        # select the top 15% of the population
        k = int(len(population) * self.survival_rate)
        best_indices = np.argsort(costs)[:k]
        # print('best_indices',best_indices)
        return [population[i] for i in best_indices],np.min(costs)

    def run_evolution(self):
        population = self.generate_population()
        for i in range(self.num_generations):
            # print(f'processing {i} of {self.num_generations}')
            k_best,min_cost = self.select_k_best(population)
            if i % 50 == 0:
                print('generation',i,'min_cost',min_cost)
                display_keyboard(k_best[0],min_cost)
            population = self.mutate_population(k_best)
            # break
        return k_best[0]