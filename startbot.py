import os
import re
import time
import cPickle
import atexit
import random
from collections import defaultdict
# import additional modules
import english
import profile as Profile

markov = defaultdict(list)

class bot():
	def __init__(self):
	   self.profile = Profile.profile  
	
	def remember(self, msg):
		add_to_brain(msg, write=True)
	
	def reply(self, msg):
		s = generate_reply(msg)
		print "Nagisa: %s" % s

# Variables
OMIT = ['is','are','that']
REMOVE_CHARS = re.compile("""[?'",.]""")
    
# Adds the users msg to the "brain"
def add_to_brain(msg, write=True):
    if write:
        f = open('training_text.txt', 'a')
        f.write(msg + '\n')
        f.close()
    
    if not msg.strip().lower() in [x.lower() for x in markov.keys()]:
        for word in msg.split():
            word = REMOVE_CHARS.sub('',word)
            if word not in OMIT:
                markov[msg.strip()].append(word)

# Generates a reply message based on list of words in user msg
def generate_reply(msg):
    buf = [REMOVE_CHARS.sub('',x) for x in msg.split()]
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
            results = [(a,b) for a,b in nagisa.profile.items() if 
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
	
	
# Starts program, not very interesting...
if __name__ == "__main__":
    if os.path.exists('markov.pkl'):
        f = open('markov.pkl', 'rb')
        markov = cPickle.load(f)
        f.close()

    elif os.path.exists('training_text.txt'):
        f = open('training_text.txt', 'r')
        for line in f:
            add_to_brain(line, False)
        f.close()

	#print markov
    nagisa = bot()
	
    user_msg = "start"
	
	# Chatting loop
    while user_msg.lower().split()[0] != "goodbye":
		user_msg = raw_input(">")
		
		if user_msg != "goodbye":
			nagisa.reply(user_msg)
			nagisa.remember(user_msg)
		else:
			print "Nagisa: Goodbye!"
			time.sleep(1)	
	
    # dump markov to pkl for quicker load next time
    f = open('markov.pkl', 'wb')
    cPickle.dump(markov, f)
    f.close()
    
	
	
	