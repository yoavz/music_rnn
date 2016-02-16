import numpy as np
from pprint import pprint

import midi_util


class Sampler(object):

    def __init__(self, min_prob=0.5):
        self.notes_on = {k: False for k in range(midi_util.RANGE)}
        self.history = []
        self.min_prob = min_prob

    def sample_notes_prob(self, probs):
        """ simplest sampling """
        visualize_probs(probs)
        return (probs > self.min_prob).astype(np.float32)

    def sample_notes_static(self, probs, num_notes=4):
        """ Samples a static amount of notes from probabilities by highest prob """
        visualize_probs(probs)
        top_idxs = probs.argsort()[-num_notes:][::-1]
        chord = np.zeros([len(probs)], dtype=np.int32)
        chord[top_idxs] = 1.0
        return chord

    # def sample_notes_history(self, probs, min_prob=0.5, max_notes=4):
    #     top_note_on = list()
    #     top_note_off = list()
    #     for idx in probs.argsort()[::-1]:
    #         if probs[idx] < min_prob:
    #             break
    #         if len(top_note_on) <= max_notes:
    #             top_note_on.append(idx)
    #         if len(top_note_off) <= max_notes:
    #             if (top_note_off - midi_util.RANGE) in history[:-4]:
    #                 break
    #         top_idxs.append(idx)
    #     chord = np.zeros([len(probs)], dtype=np.int32)
    #     chord[top_idxs] = 1.0
    #      
    #     return chord

    def sample_notes_dynamic(probs, min_prob=0.5, max_notes=4):
        """ Samples all notes that are over a certain probability"""
        top_idxs = list()
        for idx in probs.argsort()[::-1]:
            if len(top_idxs) >= max_notes:
                break
            if probs[idx] < min_prob:
                break
            top_idxs.append(idx)
        chord = np.zeros([len(probs)], dtype=np.int32)
        chord[top_idxs] = 1.0
        return chord

def visualize_probs(probs):
    print 'Highest four probs: '
    pprint(sorted(list(enumerate(probs)), key=lambda x: x[1], 
           reverse=True)[:10])
