#!/usr/bin/env python3
"""
    question_answering.py - Question Answering using vector representation of phrase
    Author: Dung Le (dungle@bennington.edu)
    Date: 02/12/2017
"""

import json
import gensim
import numpy as np
import scipy

# Load Google's pre-trained Word2Vec model.
model = gensim.models.KeyedVectors.load_word2vec_format('../../../../Natural Language Processing/Miscellaneous/GoogleNews-vectors-negative300.bin', binary=True)
vocab = model.vocab.keys()

# Command Phrase and its Vector Representation
def command_representation(command):
    cmd_words = command.split()
    phrase_vec = []

    for w in cmd_words:
        if w in vocab:
            phrase_vec.append(model.wv[w].tolist())

    cmd_vec = np.sum(phrase_vec, axis=0)
    return cmd_vec

# Objects Interaction and their Vector Representation
def semantic_difference(level, lvl_objects, command):
    cmd_vec = command_representation(command)
    actions = []
    for obj in lvl_objects:
        if isinstance(level[obj]['possible_action'], str):
            actions.append(level[obj]['possible_action'])
        else:
            actions += level[obj]['possible_action']

    differences = []
    for action in actions:
        vec = []
        for w in action.split():
            if w in vocab:
                vec.append(model.wv[w].tolist())

        action_vec = np.sum(vec, axis=0)

        # calculate cosine similarity between action_vec and cmd_vec
        score = scipy.spatial.distance.cosine(action_vec, cmd_vec)
        differences.append(score)
    return differences

# Answers for simple command (easy level)
def simple_answer(level, lvl_objects, command):
    sem_diff = semantic_difference(level, lvl_objects, command)
    for obj in lvl_objects:
        if obj in command and min(sem_diff) <= 0.25:
            if level[obj]['requirement'] == None:
                return "You can " + command.lower()
            else:
                req = "The " + level[obj]['requirement']['object'] + " " + level[obj]['requirement']['location'] + " is required."
                return "Nothing happened. " + req
    return "The command is either non-valid or nothing is moved."     

# Answers for complicated command (with question-typed)

