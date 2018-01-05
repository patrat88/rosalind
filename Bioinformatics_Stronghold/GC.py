#!/usr/bin/python


# Rabbits and Recurrence Relations
# http://rosalind.info/problems/fib/

from __future__ import division


def createDict():
    # Helper variables
    dictionary = {}

    # Open file
    with open("GC.txt") as fasta_file:
        for line in fasta_file:
            if line.startswith(">Rosalind"):
                label = (line.split(">")[1]).rstrip()
                dictionary[label] = ""
            else:
                dictionary[label] += line.rstrip()


    # Return dictionary
    return dictionary


def computeCGinString(inputStr):
    # Helper variables
    lenStr = len(inputStr)
    charCounter = 0

    for character in inputStr:
        if character == "C" or character == "G":
            charCounter += 1

    # Compute % of GC
    gcContent = (charCounter / lenStr ) * 100
    return round(gcContent,6)


def searchMax(collection):
    # Helper variables
    dictionary = {}

    for k, v in collection.iteritems():
        dictionary[k] = computeCGinString(v)

    maxValKey = max(dictionary, key=dictionary.get)
    return maxValKey, dictionary[maxValKey]


print searchMax(createDict())