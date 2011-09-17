import os
import re
import time
import random
import english
#import itertools
from collections import defaultdict

markov = defaultdict(list)

class bot():
	def __init__(self, chain_length = 2):
		self.chain_length = chain_length
	
	def remember(self, msg):
		add_to_brain(msg, write_to_file=True)
	
	def reply(self, msg):
		s = generate_reply(msg, self.chain_length)
		print "Nagisa: %s" % s

# Adds the users msg to the "brain"
def add_to_brain(msg, write_to_file=False):
    if write_to_file:
        f = open('training_text.txt', 'a')
        f.write(msg + '\n')
        f.close()
    
    OMIT = ['is','are','that']
    REMOVE_CHARS = re.compile("""[?'",.]""")
    
    if not msg.strip().lower() in [x.lower() for x in markov.keys()]:
        for word in msg.split():
            word = REMOVE_CHARS.sub('',word)
            if word not in OMIT:
                markov[msg.strip()].append(word)
    #print msg
    #print markov[msg]	

# Generates a reply message based on list of words in user msg
def generate_reply(msg, chain_length):
    buf = msg.split()
    response = []
    #print buf    
	
    buf = english.possesion_handler(buf)
    
    choices = defaultdict(int)
    for x in buf:
        #print x        
        
        results = [(a,b) for a,b in markov.items() if x.lower() in [c.lower() for c in b]]
        #print "%s \n" % results
        
        for d,e in results:
            choices[d] = 1 + choices[d]
    
    if len(choices) > 1:
        #try:
        for cut in [x for x in choices.keys() if x.lower() == msg.lower()]:
            del choices[cut]
        #except: pass
    
    #print "%s \n" % choices
    
    r_items = [x for x,y in choices.items() if y >= choices[max(choices, key=choices.get)]]
    #print r_items
       
    try:
        response = random.choice([x for x,y in choices.items() if y >= 
                    choices[max(choices, key=choices.get)]])
    except:
        response = random.choice(['Um...','What?',
                                  "I don't understand. Can you be more specific?"])
        
    return response
	
	
# Starts program, not very interesting...
if __name__ == "__main__":
	if os.path.exists('training_text.txt'):
		f = open('training_text.txt', 'r')
		for line in f:
			add_to_brain(line)
		f.close()
	
	print markov
	nagisa = bot()
	
	user_msg = "start"
	
	while user_msg.lower().split()[0] != "goodbye":
		user_msg = raw_input(">")
		
		if user_msg != "goodbye":
			nagisa.reply(user_msg)
			nagisa.remember(user_msg)
		else:
			print "Nagisa: Goodbye!"
			time.sleep(1)
	
	
	
	
	
	