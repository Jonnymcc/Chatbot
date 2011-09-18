import os
import re
import cPickle
from collections import defaultdict

profile = defaultdict(list)

# Variables
OMIT = ['is','are','that']
REMOVE_CHARS = re.compile("""[?'",.]""")
    
def add_to_brain(msg):    
    if not msg.strip().lower() in [x.lower() for x in profile.keys()]:
        for word in msg.split():
            word = REMOVE_CHARS.sub('',word)
            if word not in OMIT:
                profile[msg.strip()].append(word)

# Loads profile from flat txt of statements about self.
if os.path.exists('profile.pkl'):
    f = open('profile.pkl', 'rb')
    profile = cPickle.load(f)
    f.close()

elif os.path.exists('profile.txt'):
    f = open('profile.txt', 'r')
    for line in f:
        add_to_brain(line)
    f.close()

### Use this for a method for learning about self...
#
#user_msg = "start"
#
#while user_msg.lower().split()[0] != "goodbye":
#	user_msg = raw_input(">")
#	
#	if user_msg != "goodbye":
#		nagisa.reply(user_msg)
#		nagisa.remember(user_msg)
#	else:
#		print "Nagisa: Goodbye!"
#		time.sleep(1)	

# dump markov to pkl for quicker load next time
f = open('profile.pkl', 'wb')
cPickle.dump(profile, f)
f.close()