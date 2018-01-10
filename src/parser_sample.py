#!/usr/bin/env python3
"""
    parser_sample.py - An automatic parser using spaCy to build POS for sentence
                       from Gutenberg project.
    Author: Dung Le (dungle@bennington.edu)
    Date: 01/09/2017
    Note: Since the amount of text from Gutenberg project is enormous,
          this file should not be rebuilt if not neccessary.
"""

import spacy
import nltk
from nltk.tokenize import sent_tokenize

parser = spacy.load('en')
sample_pos = []

print("+++ START PARSING +++")
with open('../data/smaller.txt', 'r') as doc:
    doc_text = doc.read()
    sent_list = sent_tokenize(doc_text)
    for sent in sent_list:
        sample = parser(sent)
        sample_sent_pos = ""
        for token in sample:
            if token.is_alpha:
                sample_sent_pos = sample_sent_pos + token.tag_ + " "
        sample_pos.append(sample_sent_pos)
doc.close()
print("+++ END OF PARSING +++")

with open('../data/sample-pos.txt', 'w') as pos_file:
    for item in sample_pos:
        pos_file.write(item + "\n")
pos_file.close()
