import numpy as np
import simpleaudio as sa
from random import shuffle
from time import sleep
import matplotlib.pyplot as plt

BASE_FREQ = 150
TESTS = 5
MAX_DELTA_F = 5
FS = 44100


def fade_in(note):
    samples = FS//50
    for i in range(samples):
        note[i] = note[i]*(i/samples)
    return note


def fade_out(note):
    samples = FS//50
    for i in range(samples):
        note[-i + 1] = note[-i + 1]*(i/samples)
    return note


def create_stimuli(base_freq, delta_freq):
    frequency = base_freq
    seconds = 1  
    
    t = np.linspace(0, seconds, seconds * FS, False)
    note = np.sin(frequency * t * 2 * np.pi)
    note = fade_in(note)
    note = fade_out(note)
    
    notes_break = np.zeros(FS//2)
    
    pitched_note = np.sin((frequency + delta_freq) * t * 2 * np.pi)

    pitched_note = fade_in(pitched_note)
    pitched_note = fade_out(pitched_note)

    test_sound = np.concatenate((note, notes_break, pitched_note))

    return test_sound
    


def play(test_sound):
    
    audio = test_sound * (2**15 - 1) / np.max(np.abs(test_sound))
    audio = audio.astype(np.int16)
    play_obj = sa.play_buffer(audio, 1, 2, FS)
    play_obj.wait_done()