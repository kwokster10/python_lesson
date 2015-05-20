# Create a command line app that will take a string and returns it printed in all caps and in pig latin if the word starts with the letter 'p'. If the word is "Crawford", print "Hey Hey Hey". Otherwise print it in reverse one letter at a time. Hint, Python's equivalent of process.argv[2] is sys.argv[1].

import sys
import re
# setting user input to word
word = sys.argv[1]
# checking to see if the word starts with a p followed by a vowel
vowels = re.match('(p[aeiouy].)', word, flags=re.I)
# checking to see if the word starts with a p followed by consonant
consonant = re.match('(p[^aeiouy].)', word, flags=re.I)

# condition checks for p first, then crawford then others
if vowels:
	print word[1:] + word[0:1] + 'ay'
elif consonant:
	print word[2:] + word[:2] + 'ay'
elif word.lower() == "crawford":
	print "Hey " * 3
else:
	for letter in word[::-1]:
		print letter
