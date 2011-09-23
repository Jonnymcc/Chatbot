"""Initializes bot profile, essentially a second markov dict"""

import os
import re 
import cPickle
from collections import defaultdict
from variables import markov
import variables

profile = defaultdict(list)

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
                
                

# Loads profile from flat txt of statements about self.
if os.path.exists('profile.pkl'):
    f = open('profile.pkl', 'rb')
    profile = cPickle.load(f)
    f.close()

elif os.path.exists('profile.txt'):
    f = open('profile.txt', 'r')
    for line in f:
        memorize(line, False)
    f.close()
    
print profile

# dump markov to pkl for quicker load next time
f = open('profile.pkl', 'wb')
cPickle.dump(profile, f)
f.close()