import re

def pronoun_handler(msg):
	first_per = ["i"]
	second_per = ["you"]
	third_per = ["he","she","they"]
	
	words = msg
	if first_per in words:
		msg = msg.replace()
	
	
	return

# A start to handling pronouns... may be harder than I anticipate.
def possesion_handler(msg):
	words = msg

	if ("my" or "mine") in words:
		try: msg.remove("my"); msg.append("your"); 
		except: pass
		try: msg.remove("mine"); msg.append("yours"); 
		except: pass
		print "path 1"

	elif ("your" or "yours") in words:
		print "path 2"
		try: msg.remove("your"); msg.append("my"); 
		except: pass
		try: msg.remove("yours"); msg.append("mine"); 
		except: pass	 
	
	return msg