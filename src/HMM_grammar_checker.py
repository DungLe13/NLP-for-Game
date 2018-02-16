#!/usr/bin/env python3
"""
    HMM_grammar_checker.py - Grammar Checker using HMM, dependency parsing and POS tagging
    Author: Dung Le (dungle@bennington.edu)
    Date: 02/12/2017
"""

import nltk

command = input("Enter your command: ")
words = nltk.word_tokenize(command)
bigrm = nltk.bigrams(words)
print(bigrm.)
