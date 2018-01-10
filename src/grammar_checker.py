#!/usr/bin/env python3
"""
    grammar_checker.py - Checking for grammar using parser
    Author: Dung Le (dungle@bennington.edu)
    Date: 01/09/2017
"""

import spacy

parser = spacy.load('en')

# Possibility 1: Rule-based grammar
# The grammar in this case is hand-coded. High precision, yet, scale poorly.
# Need to enter correct parse tree manually
with open("../data/level-pos.txt", "r") as rule_grammar:
    grammar_list = rule_grammar.read().splitlines()
rule_grammar.close()

# Possibility 2: Grammar learned from large corpus
# The grammar in this case is learned using spaCy parser for a subset taken
# from Gutenberg project (1 MB dataset). Difficult to match exactly (lower
# precision), yet, high coverage.
with open("../data/sample-pos.txt", "r") as auto_grammar:
    large_grammar_list = auto_grammar.read().splitlines()
auto_grammar.close()

class Grammar_Checker:
    def __init__(self, user_input):
        self.user_input = user_input.lower()

    def checker(self):
        # First, parse user input
        text = parser(self.user_input)
        sent_pos = ""
        for token in text:
            if token.is_alpha:
                sent_pos = sent_pos + token.tag_ + " "
        # print(sent_pos)

        # If the grammar input by user is in the pre-defined list
        # the user_input's grammar is then correct
        if sent_pos in grammar_list:
            return "Corrected"
        else:
            return "Incorrected"

    def run(self):
        return self.checker()
