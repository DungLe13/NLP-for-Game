#!/usr/bin/env python3
"""
    user_process.py - Process users' input (syntactics, semantics and pragmatics)
    Author: Dung Le (dungle@bennington.edu)
    Date: 01/08/2017
"""

import nltk
import language_check
import requests
from spelling_correction import Spelling_Correction
from nltk.corpus import stopwords
from rake_nltk import Rake

stop_words = set(stopwords.words('english'))

while True:
    # STEP 1: Take user input
    command = input("Enter your command: ")

    # STEP 2: Check for spelling and grammar
    sc = Spelling_Correction(command)
    suggestion = sc.run()
    print(suggestion)

    tool = language_check.LanguageTool('en-US')
    errors = tool.check(command)
    for i in range(len(errors)):
        print(errors[i])

    # STEP 3: Check for semantics and pragmatics using OMCS
    if suggestion != "No spelling error found..." or len(errors) != 0:
        continue
    else:
        # User input is grammatically correct
        # Attempt 1: Remove stopwords from user's input
        word_list = nltk.word_tokenize(command.lower())
        filtered_words = []
        for word in word_list:
            if word not in stop_words:
                filtered_words.append(word)
        print(filtered_words)

        # Attempt 2: Extract keywords from user's input
        r = Rake()
        r.extract_keywords_from_text(command.lower())
        user_keywords = r.get_ranked_phrases()
        print(user_keywords)

        # For each pair of words from the list of words generated above,
        # the system requests a REST endpoint to ConceptNet (OMCS database)
        # If a relation can be found between any pair, user's input is very
        # likely to be meaningful.
        if len(user_keywords) >= 2:
            for i in range(len(user_keywords)-1):
                for j in range(i+1, len(user_keywords)):
                    url = "http://api.conceptnet.io/query?node=/c/en/{0}&other=/c/en/{1}".format(user_keywords[i], user_keywords[j])
                    obj = requests.get(url).json()
                    if len(obj['edges']) != 0:
                        print("The input is possibly meaningful")
        elif len(filtered_words) >= 2:
            for i in range(len(filtered_words)-1):
                for j in range(i+1, len(filtered_words)):
                    url = "http://api.conceptnet.io/query?node=/c/en/{0}&other=/c/en/{1}".format(filtered_words[i], filtered_words[j])
                    obj = requests.get(url).json()
                    if len(obj['edges']) != 0:
                        print("The input is possibly meaningful")
        else:
            print("The input is too short. Try entering the full command.")
