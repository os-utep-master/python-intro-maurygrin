# Mauricio Roberto Hidalgo
# Intro to Python Lab
# September 1, 2019

import sys

inputFile = open(sys.argv[1], 'r')
outputFile = open(sys.argv[2], 'w')
speech = inputFile.read()
speech = speech.lower()
punctuation = ",;:.-"
speech = speech.split()
final = {}

for word in speech:
    word = word.strip(punctuation)
    if word in final:
        final[word] += 1
    else:
        final[word] = 1

for word in sorted(final):
    outputFile.write('%s %s \n' % (word, final[word]))
