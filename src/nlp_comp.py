#!/usr/bin/env python3
"""
    nlp_comp.py - Completed NLP component for Language Explorer game
    Author: Dung Le (dungle@bennington.edu)
    Date: 02/14/2017
"""

import json
from flask import Flask
from user_process import input_checker
from question_answering import simple_answer

app = Flask(__name__)
with open('../data/level_1b.json', 'r') as lvl_des:
    level = json.load(lvl_des)

lvl_objects = list(level.keys())

@app.route('/nlp/<string:command>', methods=['GET'])
def get_answer(command):
    cmd_checker = input_checker(command)

    if cmd_checker == command:
        answer = simple_answer(level, lvl_objects, cmd_checker)
        return answer
    else:
        return cmd_checker
