# Introduction

This is a Python library for generating new keyboard layouts based on data.
It uses a cost function derived from your own keypresses. There is a tool which generates all the 2 key combinations and arranges them for you to type.
You can visualize the keyboard layout as the model trains.

## Installation

## Usage

Modify the config file to change the genetic algoithm parameters.

- `python main.py -d /Users/Shuza/Code/setters-admin -e .js -s -o js_dataset.txt` this will create a dataset of all the .js files in the directory and subdirectories
- `python main.py -g` this will generate a cost matrix
- `python main.py -t -e .py -p python_dataset.txt` this will train a new keyboard layout. requires a keylog file and a cost matrix
- `python main.py -l` this will create a keylog file and populate it with user data
- `python main.py -k` this will generate a new keyboard layout. requires a keylog file and a cost matrix

## Using the keyboard layouts

`Mac osx only.`

When the program writes the file to the keyboard layout directory, look it up in the keyboard preferences under 'Other' and select it. If you make changes to it, you may need to log out and back in to see the changes.
