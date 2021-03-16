import numpy as np
import simpleaudio as sa
from random import shuffle
from time import sleep
import matplotlib.pyplot as plt
from sound_generation import *
from random import randint
import json

with open('./setup.json') as f:
    data = json.load(f)

BASE_FREQ = data.get('BASE_FREQ')


def make_tests():
    delta_f = randint(5, 15)
    
    while True:
        delta_f *= randint(0, 1) * 2 - 1
        test(BASE_FREQ, delta_f)
        user_answer = input("Do you hear difference? [T/F]\n")
        if user_answer == 'F':
            return delta_f
        delta_f /= 2
        print(delta_f)
    return None
        
        
def test(base_freq, delta_freq):
    test_sound = create_stimuli(BASE_FREQ, delta_freq)
    play(test_sound)
    

if __name__ == '__main__':
    print(make_tests())