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
ATTEMPTS = data.get('TRANSFOREMD_ATTEMPTS')
STEP = data.get('STEP_MULTIPLIER')
WEIGHTED_STEP = data.get('WEIGHTED_STEP_MULTIPLIER')

        
def make_tests(method="basic"):
    max_attempts = 0
    if method == "transformed":
        max_attempts = ATTEMPTS - 1

    weighted_step = STEP
    if method == "weighted":
        weighted_step = WEIGHTED_STEP
    
    mistakes = 0
    attempts = 0
    delta_f = 5
    
    while mistakes < 3:
        delta_f *= randint(0, 1) * 2 - 1
        answer = test(BASE_FREQ, delta_f)
        user_answer = input("Do you hear the difference? [T/F]\n")
        if user_answer == 'T' and attempts == max_attempts:
            delta_f /= STEP
            attempts = 0
        elif user_answer == 'T' and attempts < max_attempts:
            attempts += 1
        else:
            delta_f *= weighted_step
            mistakes += 1
            attempts = 0
    return abs(delta_f / weighted_step)

        
def test(base_freq, delta_freq):
    test_sound = create_stimuli(BASE_FREQ, delta_freq)
    play(test_sound)
    return 2 if delta_freq > 0 else 1


if __name__ == '__main__':
    print(make_tests('transformed'))