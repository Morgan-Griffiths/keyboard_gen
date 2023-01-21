import numpy as np
from cli_keycombinations import populate_user_data
from genetic_algo import GenericKeyboardSearch
from create_keyboard import create_keyboard_layout,save_keyboard_layout
from utils import parse_keys, parse_python,generate_cost_matrix
from create_dataset import create_dataset
import json

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Train and generate a new keyboard layout. Requires a keylog file. Generate your key log data')
    parser.add_argument('--keylog','-l', action='store_true', help='Path to keylog file')
    parser.add_argument('--train','-t', action='store_true', help='Train a new keyboard layout')
    parser.add_argument('--generate','-g', action='store_true', help='Generate cost matrix')
    parser.add_argument('--path', type=str, help='Path to data file')
    parser.add_argument('--keyboard', action="store_true", help='Generate keyboard layout')
    parser.add_argument('--datapath','-d', type=str, help='Path to folder containing relevant files')
    parser.add_argument('--extension','-e', type=str, help='File extension to parse')

    args = parser.parse_args()

    if args.keylog:
        populate_user_data()
        generate_cost_matrix()
    elif args.generate:
        generate_cost_matrix()
    elif args.train:
        cost_matrix = np.load('cost_matrix.npy')
        test_data = parse_python()
        training_data = parse_keys(test_data)
        search = GenericKeyboardSearch(training_data,cost_matrix)
        keyboard = search.run_evolution()
        with open('keyboard.json','w') as f:
            json.dump(keyboard,f)
        # save keyboard
        save_keyboard_layout(keyboard)
    elif args.keyboard:
        with open('keyboard.json','r') as f:
            keyboard = json.load(f)
        layout = create_keyboard_layout()
        save_keyboard_layout(layout)
    elif args.data:
        create_dataset(args.datapath,args.extension)
    else:
        print('Please specify a command')