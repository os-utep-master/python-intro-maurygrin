# Mauricio Roberto Hidalgo
# Intro to Python Lab
# September 1, 2019

import sys

inputFile = open(sys.argv[1], 'r')
outputFile = open(sys.argv[2], 'w')
speech = inputFile.read()
outputFile.write('%s' % speech)
