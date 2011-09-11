import os
import time
import random
import english
import itertools
from collections import defaultdict

markov = defaultdict(list)
STOP_WORD = "\n"

class bot():
	def __init__(self, chain_length = 2, max_words = 10000):
		self.chain_length = chain_length
		self.max_words = max_words
	
	def remember(self, msg):
		add_to_brain(msg, self.chain_length, write_to_file=True)
	
	def reply(self, msg):
		s = generate_reply(msg, self.chain_length, self.max_words)
		# print "Nagisa: " + s.strip()
		print "Nagisa: %s" % s

def add_to_brain(msg, chain_length, write_to_file=False):
	if write_to_file:
		f = open('training_text.txt', 'a')
		f.write(msg + '\n')
		f.close()
		
	buf = []

	print msg
	for word in msg.split():
		print tuple(buf)
		markov[tuple(buf)].append(msg)
		# buf[0].pop()
		buf.append(word)
		# print buf
		# print markov



def generate_reply(msg, chain_length, max_words=10000):
	buf = msg.split()[:chain_length]

	if len(msg.split()) > chain_length:
		response = buf[:]e
	else:
		response = []
		for i in xrange(chain_length):
			response.append(random.choice(markov[random.choice(markov.keys())]))
	
	buf = english.possesion_handler(buf)
	
	for x in itertools.permutations(buf):
		try:
			response = random.choice(markov[tuple(x)])
		except:
			pass
	
	# Random is boring...
	# for i in xrange(max_words):
		# try: 
			# response = random.choice(markov[tuple(buf)])
		# except IndexError:
			# continue
		# if next_word == STOP_WORD:
			# break
		# response.append(next_word)
		# del buf[0]
		# buf.append(next_word)
	# return ' '.join(response)
	return response
	
	
# Starts program, not very interesting...
if __name__ == "__main__":
	if os.path.exists('training_text.txt'):
		f = open('training_text.txt', 'r')
		for line in f:
			add_to_brain(line, chain_length=3)
		f.close()
	
	print markov
	nagisa = bot()
	
	user_msg = "start"
	
	while user_msg.lower().split()[0] != "goodbye":
		user_msg = raw_input(">")
		
		if user_msg != "goodbye":
			# nagisa.remember(user_msg)
			nagisa.reply(user_msg)
		else:
			print "Nagisa: Goodbye!"
			time.sleep(2)
	
	
	
	
	
	