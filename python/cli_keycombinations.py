# create all possible two key combinations and randomly sample from them.

import datetime
from datatypes import MODIFIER_KEYS,ALL_USED_KEYS,stoi
from utils import filter_keylogs

from pynput.keyboard import Key, Listener
import logging
import os
from pathlib import Path


def start_logging():
    logging.basicConfig(filename = os.path.join(Path(os.getcwd()).parent,"keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
    def on_press(key):
        logging.info(str(key))
    with Listener(on_press=on_press) as listener:
        listener.join()

def generate_key_combinations():
    key_combinations = []
    for key1 in ALL_USED_KEYS + MODIFIER_KEYS:
        for key2 in ALL_USED_KEYS + MODIFIER_KEYS:
            key_combinations.append((key1,key2))
    return key_combinations

def get_executed_commands(filtered_logs):
    executed_commands = set()
    for line,next_line in zip(filtered_logs,filtered_logs[1:]):
        date,command = line
        next_date,next_command = next_line
        time_delta = datetime.datetime.strptime(next_date,'%Y-%m-%d %H:%M:%S,%f') - datetime.datetime.strptime(date,'%Y-%m-%d %H:%M:%S,%f')
        if time_delta.seconds <= 1 and (stoi[command],stoi[next_command]) not in executed_commands:
            executed_commands.add((stoi[command],stoi[next_command]))
    print(len(executed_commands))
    return executed_commands


def return_command_chain(key_combos):
    starts = {}
    for key in key_combos:
        if key[0] in starts:
            starts[key[0]].append(key[1])
        else:
            starts[key[0]] = [key[1]]
    chain = [key_combos[0][0]]
    while True:
        s = chain[-1]
        if starts.get(s):
            chain.append(starts[s].pop())
        else:
            found = False
            for k,v in starts.items():
                if len(v) > 0:
                    chain.append(k)
                    found = True
                    break
            if not found:
                break
    # print(chain)
    return chain
    
def get_key_combos():
    key_combos = generate_key_combinations()
    with open('../keyLog.txt','r') as f:
        key_logs = f.read().splitlines()
    filtered_logs = filter_keylogs(key_logs)
    executed_commands = get_executed_commands(filtered_logs)
    remaining_commands = [k for k in key_combos if (stoi[k[0]],stoi[k[1]]) not in executed_commands]
    return remaining_commands,len(key_combos)

def populate_user_data():
    start_logging()
    remaining_commands,total = get_key_combos()
    print(f'{len(remaining_commands)} key combinations remaining out of {total}')
    while len(remaining_commands) > 0:
        command_chain = return_command_chain(remaining_commands)
        key_combinations_pressed = 0
        print(f'remaining commands to test {len(command_chain)}')
        try:
            start = 0
            while True:
                command_string = command_chain[start:start+10]
                print(start,command_string)
                input()
                key_combinations_pressed += len(command_string)
                start += 10
                if start >= len(command_chain):
                    break
            remaining_commands,total = get_key_combos()
        except KeyboardInterrupt:
            print('You did {} key combinations'.format(key_combinations_pressed))
    print('You did all the key combinations!')

if __name__ == '__main__':
    populate_user_data()
