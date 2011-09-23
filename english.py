import re

FIRST_PERSON = ['i', 'me', 'my', 'mine']
SECOND_PERSON = ["you","your","yours","youre"]

# A start to handling pronouns... may be harder than I anticipate.
def possesion_handler(msg):
    
    # Not sure if this is useful yet    
    if [True] in [[a in msg] for a in FIRST_PERSON]:
        try: msg.remove("i"); msg.append("you"); 
        except: pass
        try: msg.remove("me"); msg.append("you"); 
        except: pass
        try: msg.remove("my"); msg.append("your"); 
        except: pass
        try: msg.remove("mine"); msg.append("your"); 
        except: pass
        option = 1
        print "possession handler: path 1"
    
    elif [True] in [[a in msg] for a in SECOND_PERSON]:
        try: msg.remove("you"); msg.append("i"); 
        except: pass
        try: msg.remove("youre"); msg.append("i"); 
        except: pass
        try: msg.remove("your"); msg.append("my"); 
        except: pass
        try: msg.remove("yours"); msg.append("mine"); 
        except: pass
        option = 2	 
        print "possession handler: path 2"
    
    else: option = 3
    
    return [msg, option]
    


# Come back to this maybe...
def pronoun_handler(msg):
	
	if first_per in msg:
		msg = msg.replace()
	
	return