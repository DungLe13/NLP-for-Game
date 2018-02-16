## NLP for Language Teaching Application

This project focuses on building an NLP component for language teaching game, in which the user has to input a series of command expressed in natural language (i.e. English, German or Spanish) in order to complete each game level. This component acts as a question answering system in which it automatically checks with the knowledge given from game designer to walk the user through each level. Each level requires a different grammar, advancing from simple command like "Open the door" to question like "Can you open the door?" or using passive like "Can the door be opened?"

The three folders contain these following information:

### Data
This folder contains any kind of dataset that is useful for any part of this project.

- `big.txt` and `small.txt` contains all (or parts of) the text from Guttenberg project, which has been used to provide data for spelling correction and grammar checker.
- `level-desc.txt` is a sample of level description that game designer needs to provide beforehand. `level_1.json` and `level_1b.json` are another two possible level description template (given in json format.)
- If a rule-based grammar is used for grammar checker, it should be updated at `level-pos.txt`
- `sample-pos.txt` contains the grammar from the `small.txt` corpus.

### Literatures
A list of research papers that I found related to three topics: knowledge representation, commonsense knowledge and question answering. The file `NLP for Educational Game` is my proposal for the project. See this file for more information about the methods.

### Src
This folder contains all the files written in Python (will be updated regularly):

- spelling_correction.py: An algorithm for spelling correction using probability and minimum edit distance (more at http://norvig.com/spell-correct.html)
- user_process.py: Processing user's input. This includes checking for spelling, grammar and pragmatic (whether or not the command makes sense using commonsense knowledge.)
- grammar_checker.py: Simple grammar checker using one of the two options: i.POS tagging from large corpus, or ii. pre-defined rule-based grammar.
- HMM_grammar\_checker.py: Grammar checker using Hidden Markov Model (HMM) - will be updated later.
- parser_sample.py: A sample POS parser used to parse the large corpus for grammar checker.
- knowledge_rep.py: Knowledge representation of text (level description). The script returns a dictionary of objects and possible object interactions.
- question_answering.py: Answer user's command/question using the knowledge extracted from level description.
- nlp_comp.py: REST endpoint for the whole system.

### game_assets
This folder contains the game assets for the game Language Explorer, which can be found at https://github.com/DungLe13/Language-Explorer .