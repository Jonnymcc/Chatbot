import re, random
import english
from collections import defaultdict
from profile import profile
from variables import markov
import variables

# Adds the users msg to the "brain"
def memorize(msg, write=True):
    if write:
        f = open('training_text.txt', 'a')
        f.write(msg + '\n')
        f.close()
    
    if not msg.strip().lower() in [x.lower() for x in markov.keys()]:
        for word in msg.split():
            word = variables.REMOVE_CHARS.sub('',word)
            if word not in variables.OMIT:
                markov[msg.strip()].append(word)