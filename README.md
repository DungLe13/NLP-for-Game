## NLP for Language Teaching Application

This project focuses on building an NLP component for language teaching game, in which the user has to input a series of command expressed in natural language (i.e. English, German or Spanish) in order to complete each game level. This component acts as a question answering system in which it automatically checks with the knowledge given from game designer to walk the user through each level. Each level requires a different grammar, advancing from simple command like "Open the door" to question like "Can you open the door?" or using passive like "Can the door be opened?"

The three folders contain these following information:

### Data
This folder contains any kind of dataset that is useful for any part of this project. At the moment, the file `big.txt` contains all the text from Guttenberg project, which has been used to provide data for spelling correction and grammar checker.

### Literatures
A list of research papers that I found related to three topics: knowledge representation, commonsense knowledge and question answering. The file `NLP for Educational Game` is my proposal for the project. See this file for more information about the methods.

### Src
This folder contains all the files written in Python (will be updated regularly):

- spelling_correction.py: An algorithm for spelling correction using probability and minimum edit distance (more at http://norvig.com/spell-correct.html)
- user_process.py: Processing user's input. This includes checking for spelling and grammar (since this is a language teaching application, this part is crucial) and checking for semantics and pragmatics (whether the input command makes sense given the game/real world environment.)