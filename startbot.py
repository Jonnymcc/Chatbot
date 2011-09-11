import os
import time
import random
import english
from collections import defaultdict

markov = defaultdict(list)
STOP_WORD = "\n"

class bot():
	def __init__(self, chain_length = 1, chattiness = 1.0, max_words = 10000):
		self.chain_length = chain_length
		self.chattiness = chattiness
		self.max_words = max_words
	
	def remember(self, msg):
		add_to_brain(msg, self.chain_length, write_to_file=True)
	
	def reply(self, msg):
		s = generate_sentences(msg, self.chain_length, self.max_words)
		print "Nagisa: " + s.strip()

def add_to_brain(msg, chain_length, write_to_file=False):
	if write_to_file:
		f = open('training_text.txt', 'a')
		f.write(msg + '\n')
		f.close()
	buf = [STOP_WORD] * chain_length
	for word in msg.split():
		markov[tuple(buf)].append(word)
		del buf[0]
		buf.append(word)
	markov[tuple(buf)].append(STOP_WORD)	

def generate_sentences(msg, chain_length, max_words=10000):
	buf = msg.split()[:chain_length]
	if len(msg.split()) > chain_length:
		message = buf[:]
	else:
		message = []
		for i in xrange(chain_length):
			message.append(random.choice(markov[random.choice(markov.keys())]))
	for i in xrange(max_words):
		try: 
			next_word = random.choice(markov[tuple(buf)])
		except IndexError:
			continue
		if next_word == STOP_WORD:
			break
		message.append(next_word)
		del buf[0]
		buf.append(next_word)
	return ' '.join(message)
	

if __name__ == "__main__":
	if os.path.exists('training_text.txt'):
		f = open('training_text.txt', 'r')
		for line in f:
			add_to_brain(line, chain_length=1)
		print 'Brain Reloaded'
		f.close()
	
	nagisa = bot()
	
	user_msg = "start"
	
	while user_msg.lower().split()[0] != "goodbye":
		user_msg = raw_input(">")
		
		nagisa.remember(user_msg)
		
		if user_msg != "goodbye":
			nagisa.reply(user_msg)
		else:
			print "Nagisa: Goodbye!"
			time.sleep(2)
	
	
	
	
	
	