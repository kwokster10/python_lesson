# Create a command line app that will take a string and returns it printed in pig latin if the word starts with the letter 'p'. If the word is "Crawford", print "Hey Hey Hey". Otherwise print it in reverse one letter at a time in all caps. Hint, Python's equivalent of process.argv[2] is sys.argv[1].

import sys
import re
# setting user input to word
word = sys.argv[1]
# checking to see if the word starts with a p followed by a vowel
vowels = re.match('(p[aeiouy].)', word, flags=re.I)
# checking to see if the word starts with a p followed by a consonant
consonant = re.match('(p[^aeiouy].)', word, flags=re.I)

# condition checks for crawford, then p words, then others
if word.lower() == "crawford":
	print "Hey " * 3
elif vowels:
	print word[1:] + word[0:1] + 'ay'
elif consonant:
	print "%s%say" % (word[2:], word[:2])
else:
	for letter in word[::-1]:
		print letter.upper()

# The last else is an extended slice syntax. It works by doing [begin:end:step] - by leaving begin and end off and specifying a step of -1, it reverses a string.
# Check out https://docs.python.org/2/whatsnew/2.3.html#extended-slices to read more

