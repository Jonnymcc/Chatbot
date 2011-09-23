import re, random
import english
from collections import defaultdict
from profile import profile
from variables import markov
import variables

# Generates a reply message based on list of words in user msg
def generate_reply(msg):
    
    buf = [variables.REMOVE_CHARS.sub('',x) for x in msg.split()]
    response = []
	
    (buf, option) = english.possesion_handler(buf)
    
    choices = defaultdict(int)
    
    # Create list of choices of repsonses
    if option != 2:
        for x in buf:
            results = [(a,b) for a,b in markov.items() if x.lower() in [c.lower() for c in b]]
            for d,e in results:
                choices[d] = 1 + choices[d]
    elif option == 2:
        for x in buf:
            results = [(a,b) for a,b in profile.items() if 
                            x.lower() in [c.lower() for c in b]]
            for d,e in results:
                choices[d] = 1 + choices[d]
    
    # removes user msg from results    
    if len(choices) > 1:
        for cut in [x for x in choices.keys() if x.lower() == msg.lower()]:
            del choices[cut]
    
    # Choose response from choices   
    try:
        response = random.choice([x for x,y in choices.items() if y >= 
                    choices[max(choices, key=choices.get)]])
    except:
        response = random.choice(['Um...','What?',
                                  "I don't understand. Can you be more specific?"])
        
    return response
