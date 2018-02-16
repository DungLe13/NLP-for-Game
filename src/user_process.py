#!/usr/bin/env python3
"""
    user_process.py - Process users' input (syntactics, semantics and pragmatics)
    Author: Dung Le (dungle@bennington.edu)
    Date: 01/08/2017
"""

import nltk
import requests
from spelling_correction import Spelling_Correction
from grammar_checker import Grammar_Checker
from nltk.corpus import stopwords
from rake_nltk import Rake

stop_words = set(stopwords.words('english'))

# Supporting Function:
def conceptnet_checker(words_list):
    for i in range(len(words_list)-1):
        for j in range(i+1, len(words_list)):
            url = "http://api.conceptnet.io/query?node=/c/en/{0}&other=/c/en/{1}".format(words_list[i], words_list[j])
            obj = requests.get(url).json()
            if len(obj['edges']) != 0:
                return "Possibly meaningful"
    return "No collusion"

# MAIN PART:
def spelling_check(command):
    # STEP 2: Check for spelling and grammar
    # Step 2-a: Check for spelling
    sc = Spelling_Correction(command)
    suggestion = sc.run()
    return suggestion

def grammar_check(command):
    # Step 2-b: Check again using pre-defined grammar
    gc = Grammar_Checker(command)
    grammar_eval = gc.run()
    return grammar_eval

def pragmatic_check(command):
    # STEP 3: Check for semantics and pragmatics using OMCS
    # Attempt 1: Remove stopwords from user's input
    word_list = nltk.word_tokenize(command.lower())
    filtered_words = []
    for word in word_list:
        if word not in stop_words:
            filtered_words.append(word)
    #print(filtered_words)

    # Attempt 2: Extract keywords from user's input
    r = Rake()
    r.extract_keywords_from_text(command.lower())
    user_keywords = r.get_ranked_phrases()
    #print(user_keywords)

    '''
    For each pair of words from the list of words generated above,
    the system requests a REST endpoint to ConceptNet (OMCS database)
    If a relation can be found between any pair, user's input is very
    likely to be meaningful.
    '''
    if len(user_keywords) >= 2:
        return conceptnet_checker(user_keywords)
    elif len(filtered_words) >= 2:
        return conceptnet_checker(filtered_keywords)
    else:
        return "The input is too short. Try entering the full command."

def input_checker(command):
    spelling = spelling_check(command)
    grammar = grammar_check(command)
    pragmatic = pragmatic_check(command)
    
    if spelling == "No spelling error found..." and grammar == "Corrected":
        if pragmatic == "Possibly meaningful":
            return command
        else:
            return command, "without collusion"
    else:
        return spelling, grammar + " grammar"

