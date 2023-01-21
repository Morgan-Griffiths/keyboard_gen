import datetime
import re
import time
import numpy as np
import regex

from datatypes import MODIFIER_KEYS,ALL_USED_KEYS,BACKSPACE_WIDTH, CAPSLOCK_WIDTH, COMMAND_WIDTH, ENTER_WIDTH, KEY_HEIGHT, KEY_POSITIONS, KEY_WIDTH, KEYBOARD_HEIGHT, KEYBOARD_WIDTH, ROW_HEIGHT, SHIFT_WIDTH, SPACE_WIDTH, TAB_WIDTH,stoi,itos,MODIFIER_KEY_MAP,SHIFT_KEY_MAP


import matplotlib.pyplot as plt
import matplotlib.patches as patches

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print('%r  %2.2f s' % (method.__name__, te-ts))
        return result
    return timed

def display_keyboard(translation_dictionary,score):
    fig,ax = plt.subplots(1,dpi=900)

    for key in KEY_POSITIONS:
        # if key.startswith('Key'):
        #     print(key,key in translation_dictionary)
        if key in translation_dictionary:
            translated_key = translation_dictionary[key]
            key_position = KEY_POSITIONS[translated_key]
            if translated_key == 'Key.space':
                rect = patches.Rectangle((key_position[0] - SPACE_WIDTH * 0.5,key_position[1] - KEY_HEIGHT*0.5),SPACE_WIDTH,ROW_HEIGHT,linewidth=1,edgecolor='k',facecolor='w')
            elif key in ['Key.shift','Key.shift_r']:
                rect = patches.Rectangle((KEY_POSITIONS[key][0] - SHIFT_WIDTH * 0.5,KEY_POSITIONS[key][1] - KEY_HEIGHT*0.5),SHIFT_WIDTH,ROW_HEIGHT,linewidth=1,edgecolor='k',facecolor='w')
            elif key in ['Key.cmd','Key.cmd_r']:
                rect = patches.Rectangle((KEY_POSITIONS[key][0] - COMMAND_WIDTH * 0.5,KEY_POSITIONS[key][1] - KEY_HEIGHT*0.5),COMMAND_WIDTH,ROW_HEIGHT,linewidth=1,edgecolor='k',facecolor='w')
            elif key in ['Key.caps_lock','Key.enter']:
                rect = patches.Rectangle((KEY_POSITIONS[key][0] - CAPSLOCK_WIDTH * 0.5,KEY_POSITIONS[key][1] - KEY_HEIGHT*0.5),ENTER_WIDTH,ROW_HEIGHT,linewidth=1,edgecolor='k',facecolor='w')
            elif key in ['Key.tab','Key.backspace']:
                rect = patches.Rectangle((KEY_POSITIONS[key][0] - TAB_WIDTH * 0.5,KEY_POSITIONS[key][1] - KEY_HEIGHT*0.5),BACKSPACE_WIDTH,ROW_HEIGHT,linewidth=1,edgecolor='k',facecolor='w')
            else:
                rect = patches.Rectangle((key_position[0] - KEY_WIDTH * 0.5,key_position[1] - KEY_HEIGHT*0.5),KEY_WIDTH,ROW_HEIGHT,linewidth=1,edgecolor='k',facecolor='w')
            ax.text(key_position[0],key_position[1],key,fontsize=5,ha='center',va='center')
        else:
            rect = patches.Rectangle((KEY_POSITIONS[key][0] - KEY_WIDTH * 0.5,KEY_POSITIONS[key][1] - KEY_HEIGHT*0.5),KEY_WIDTH,ROW_HEIGHT,linewidth=1,edgecolor='k',facecolor='w')
            ax.text(KEY_POSITIONS[key][0],KEY_POSITIONS[key][1],key,fontsize=5,ha='center',va='center')
        ax.add_patch(rect)

    ax.set_xlim(0,KEYBOARD_WIDTH)
    ax.set_ylim(0,KEYBOARD_HEIGHT)
    ax.set_aspect('equal')
    plt.savefig(f'./images/{datetime.datetime.utcnow()}_{score}_keyboard.png',dpi=900)

def visualize_keypress_matrix(cost_matrix):
    fig, ax = plt.subplots(figsize=(32,32))
    ax.matshow(cost_matrix,cmap='Blues')
    for (i, j), z in np.ndenumerate(cost_matrix):
        row = MODIFIER_KEY_MAP[itos[i]] if itos[i] in MODIFIER_KEYS else itos[i]
        col = MODIFIER_KEY_MAP[itos[j]] if itos[j] in MODIFIER_KEYS else itos[j]
        chstr = row + col
        ax.text(j,i, chstr, ha='center',va='bottom',color='gray')
        ax.text(j,i, round(cost_matrix[i,j],2), ha='center',va='top',color='gray')
    ax.set_xlabel('Key pressed')
    ax.set_title('Average time between key presses')
    plt.axis('off');
    plt.savefig('./images/keypress_matrix.png',dpi=900)
    
    
def generate_cost_matrix():
    with open('../keyLog.txt','r') as f:
        key_logs = f.read().splitlines()
    # unique_commands = np.unique([line.split(': ')[1] for line in key_logs])
    # print(unique_commands)

    cost_matrix = np.zeros((len(ALL_USED_KEYS + MODIFIER_KEYS),len(ALL_USED_KEYS + MODIFIER_KEYS)))
    count_matrix = np.ones((len(ALL_USED_KEYS + MODIFIER_KEYS),len(ALL_USED_KEYS + MODIFIER_KEYS)))

    filtered_key_logs = filter_keylogs(key_logs)
    # time_deltas = []
    for line,next_line in zip(filtered_key_logs,filtered_key_logs[1:]):
        # print(line)
        date,command = line
        next_date,next_command = next_line
        # print('date,command',date,command)
        # print('next_date,next_command',next_date,next_command)
        time_delta = datetime.datetime.strptime(next_date,'%Y-%m-%d %H:%M:%S,%f') - datetime.datetime.strptime(date,'%Y-%m-%d %H:%M:%S,%f')
        if time_delta.seconds <= 1:
            cost_matrix[stoi[command],stoi[next_command]] += time_delta.total_seconds()
            count_matrix[stoi[command],stoi[next_command]] += 1
            # time_deltas.append(time_delta)
        # break
    # print(key_logs[:20])
    # print(time_deltas[:25])
    cost_matrix = cost_matrix / count_matrix
    np.save('assets/cost_matrix.npy',cost_matrix)

def keyboard_cost(text,cost_matrix,translation_dictionary):
    cost = 0
    for letter,next_letter in zip(text,text[1:]):
        cost += cost_matrix[stoi[translation_dictionary[letter]],stoi[translation_dictionary[next_letter]]]
    return cost / len(text)# normalized by text length

# def keyboard_cost_vectorized(text,cost_matrix,translation_dictionary):
#     cost = 0
#     translated_text = [stoi[translation_dictionary[letter]],stoi[translation_dictionary[next_letter]] for letter,next_letter in zip(text,text[1:])]
#     for letter,next_letter in zip(text,text[1:]):
#         cost += cost_matrix[stoi[translation_dictionary[letter]],stoi[translation_dictionary[next_letter]]]
#     return cost / len(text)# normalized by text length

def parse_files(extension,file_path):
    if extension == 'txt':
        return parse_text(file_path)
    elif extension == '.py':
        return parse_python(file_path)
    elif extension == '.js':
        return parse_javascript(file_path)
    else:
        raise Exception('Invalid extension')

def parse_javascript(file_path):
    with open(file_path,'r') as f:
        text = f.read()
    return text

def parse_text(file_path):
    with open(file_path,'r') as f:
        text = f.read()
    return text

def parse_python(file_path):
    with open(file_path,'r') as f:
        text = f.read()
    text = re.sub('\\n', '',text)
    text = re.sub('\s{4}', '\t',text)
    number_of_letters = len(text)
    print('number of letters',number_of_letters)
    return text

def parse_keys(text):
    keys = []
    for item in text:
        if item in SHIFT_KEY_MAP:
            shift,normal = SHIFT_KEY_MAP[item]
            keys.append(shift)
            keys.append(normal)
        elif item == '\t':
            keys.append('Key.tab')
        elif item == ' ':
            keys.append('Key.space')
        elif item in ALL_USED_KEYS:
            keys.append(item)
    return keys

def filter_keylogs(key_logs):
    valid_keys = set(MODIFIER_KEYS + ALL_USED_KEYS)
    filtered_logs = []
    for line in key_logs:
        date,command = line.split(': ')
        if command.startswith("This process"):
            continue
        command = regex.sub(r'\'(?P<key>.)\'',r'\g<key>',command)
        command = regex.sub(r'"(?P<key>.)"',r'\g<key>',command)
        if command == ('\'\\\\\''):
            command = '\\'
        if command not in valid_keys:
            continue
        filtered_logs.append((date,command))
    return filtered_logs

def L2(point1,point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

def calculate_distance_matrix(key_positions):
    distance_matrix = {}
    for key1 in key_positions:
        for key2 in key_positions:
            distance_matrix[(key1,key2)] = L2(key_positions[key1],key_positions[key2])
    return distance_matrix

