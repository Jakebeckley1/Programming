#!/usr/bin/env python
# TEST #1
# 4-19-2019
codeInitial = input('Enter your message: ')
codeLength = len(codeInitial)
counter = 1
finalString = ""
currentCharacter = codeInitial [:1]
for counter in range(1,codeLength+1):
    currentCharacter = codeInitial [counter-1:counter]
    currentCharacter = currentCharacter*2
    finalString = finalString + currentCharacter
    counter = counter + 1
print(finalString)
