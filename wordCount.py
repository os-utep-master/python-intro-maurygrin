# Mauricio Roberto Hidalgo
# Python-Intro Lab
# 09/01/2019
# CS4375 - Theory of Operating Systems

import sys
import os

# Check if the number of arguments is correct
if len(sys.argv) != 3:
    print('Wrong number of arguments')
    exit()

# Input file to count words  
inputFile = sys.argv[1]

#Check if the file exist in the folder
if not os.path.exists(inputFile):
    print('The file does not exist in this folder')
    exit()

inputFile = open(sys.argv[1], 'r')
# Output file to write the counting of words
outputFile = open(sys.argv[2], 'w')
# Read the input file, lowercase, remove punctiation marks, and converts the input file into a list
speech = inputFile.read()
speech = speech.lower()
speech = speech.replace('.', "").replace(",","").replace(";","").replace(":","").replace("\"", "").replace("-"," ").replace("'"," ")
speech = speech.split()
# List with the content to be written in the output file
final = {}

# Obtain words in the file without duplicates and counts how many times are written in the file
for word in speech:
    if word in final:
        final[word] += 1
    else:
        final[word] = 1

# Sorts the final list in alphabetical order and writes the list of words into the output file
for word in sorted(final):
    outputFile.write('%s %s \n' % (word, final[word]))
