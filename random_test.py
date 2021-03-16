import numpy as np
import simpleaudio as sa
from random import shuffle
from time import sleep
import matplotlib.pyplot as plt
from sound_generation import *

with open('./setup.json') as f:
    data = json.load(f)

BASE_FREQ = data.get('BASE_FREQ')
MAX_DELTA_F = 3
TESTS = 5


def make_tests():
    delta_f = np.linspace(-MAX_DELTA_F, MAX_DELTA_F, TESTS, False)
    shuffle(delta_f)
    scores = []
    for f in delta_f:
        answer = test(BASE_FREQ, f)
        user_answer = int(input("Which sound was higher (1 or 2): "))
        scores.append((f, answer == user_answer))
    return scores


def test(base_freq, delta_freq):
    test_sound = create_stimuli(base_freq, delta_freq)
    play(test_sound)
    return 2 if delta_freq > 0 else 1


def create_plot(scores=[]):
    scores = sorted(scores)
    scores = np.rot90(scores)
    plt.ylabel('Answer')
    plt.xlabel('Frequency shift')
    plt.plot(scores[1], scores[0])
    plt.show()


if __name__ == '__main__':
    scores = make_tests()
    create_plot(scores)
    
