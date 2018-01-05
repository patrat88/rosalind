#!/usr/bin/python


# Counting DNA Nucleotides


def countDnaString(dna_string):
    # Char list:
    chars = ['A', 'C', 'G', 'T']
    
    # Counters 
    aCounter = 0
    cCounter = 0
    gCounter = 0
    tCounter = 0

    for char in dna_string:
        if char == "A":
            aCounter += 1
        elif char == "C":
            cCounter += 1
        elif char == "G":
            gCounter += 1
        elif char == "T":
            tCounter += 1

    return "%s %s %s %s" % (aCounter, cCounter, gCounter, tCounter)
     

