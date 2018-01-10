#!/usr/bin/env python3
"""
    spelling_correction.py - Spelling correction using Probability and Minimum Edit Distance
    Author: Peter Norvig (http://norvig.com/spell-correct.html)
    Modifier: Dung Le (dungle@bennington.edu)
    Date: 01/08/2017
"""

import re
import nltk
from collections import Counter
from nltk.tokenize import word_tokenize

def words(text):
    return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open('../data/big.txt').read()))

class Spelling_Correction:
    def __init__(self, user_input):
        # user_input: the command input by user
        self.user_input = user_input.lower()

    def P(self, word, N=sum(WORDS.values())):
        # Probability of `word`
        return WORDS[word] / N

    def correction(self, word):
        # Most probable spelling correction for word.
        # (word with highest probability from list of candidates)
        return max(self.candidates(word), key=self.P)

    def candidates(self, word):
        # Generate possible spelling corrections for word.
        return (self.known([word]) or self.known(self.edits1(word))
                or self.known(self.edits2(word)) or [word])

    def known(self, words):
        # The subset of `words` that appear in the dictionary of WORDS.
        return set(w for w in words if w in WORDS)

    def edits1(self, word):
        # All edits that are one edit away from `word`
        letters = 'abcdefghijklmnopqrstuvwxyz'
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        # The edits will be letter-by-letter
        # There are four possible transformation: insert, delete, replace, and transpose
        deletes = [L + R[1:] for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
        replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
        inserts = [L + c + R for L, R in splits for c in letters]

        return set(deletes + transposes + replaces + inserts)

    def edits2(self, word):
        # All edits that are two edits away from `word`
        return (e2 for e1 in self.edits1(word) for e2 in self.edits1(e1))

    def run(self):
        word_list = word_tokenize(self.user_input)
        correct_list = []
        non_alphameric = False
        for word in word_list:
            if word.isalnum():
                correct_spelling = self.correction(word)
                correct_list.append(correct_spelling)
            else:
                non_alphameric = True
        correction = ' '.join(correct_list)
        if (non_alphameric == True and correction != ' '.join(word_list[:-1])) or (non_alphameric == False and correction != self.user_input):
            return "Do you mean: '{0}'?".format(correction)
        else:
            return "No spelling error found..."
