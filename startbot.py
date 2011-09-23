import os, re , time, cPickle, random
from collections import defaultdict
# import additional modules
import response_handler, memory_handler
from variables import markov

class bot():
	
	def remember(self, msg):
		memory_handler.memorize(msg, write=True)
	
	def reply(self, msg):
		s = response_handler.generate_reply(msg)
		print "Nagisa: %s" % s


# Starts program, not very interesting...
if __name__ == "__main__":
    if os.path.exists('markov.pkl'):
        f = open('markov.pkl', 'rb')
        markov = cPickle.load(f)
        f.close()

    elif os.path.exists('training_text.txt'):
        f = open('training_text.txt', 'r')
        for line in f:
            memory_handler.memorize(line, False)
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
    
	
	
	