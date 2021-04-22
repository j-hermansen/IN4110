#!/usr/bin/env python3

import sys
import os

tab = "\t"
print("\nLINES", tab, "WORDS", tab, "CHARS", tab, "FILENAME")
print("--------------------------------------------------")

def readFile(file):
    numberOfLines = 0
    numberOfWords = 0
    numberOfCharacters = 0

    currentFile = open(file)
    for line in currentFile:
        numberOfLines += 1
        numberOfWords += len(line.split())
        numberOfCharacters += len(line) - line.count(' ')
    print(numberOfLines, tab, numberOfWords, tab, numberOfCharacters, tab, os.path.basename(file))
    currentFile.close()

if sys.argv[1] == "*":
    for file in os.listdir():
        readFile(file)
    print()
else:
    filename = sys.argv[1]
    readFile(filename)




