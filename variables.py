import re
from collections import defaultdict

markov = defaultdict(list)

OMIT = ['is','are','that']
REMOVE_CHARS = re.compile("""[?'",.]""")