import re

SECOND_PERSON = ["you","your","yours","youre"]

# A start to handling pronouns... may be harder than I anticipate.
def possesion_handler(msg):
    words = msg
    
    # Not sure if this is useful yet    
    if ("my" or "mine") in words:
        try: msg.remove("my"); msg.append("your"); 
        except: pass
        try: msg.remove("mine"); msg.append("yours"); 
        except: pass
        option = 1
        #print "possession handler: path 1"
    
    elif [True] in [[a in words] for a in SECOND_PERSON]:
        try: msg.remove("you"); msg.append("I"); 
        except: pass
        try: msg.remove("youre"); msg.append("I"); 
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
	first_per = ["i"]
	second_per = ["you"]
	third_per = ["he","she","they"]
	
	words = msg
	if first_per in words:
		msg = msg.replace()
	
	
	return