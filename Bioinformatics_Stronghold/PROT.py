#!/usr/bin/python


# Translating RNA into Protein
# http://rosalind.info/problems/prot/


# Global dictionary with RNA codon table
rnaCodonTable = {"UUU" : "F",    "CUU" : "L", "AUU" : "I", "GUU" : "V",
               "UUC" : "F",    "CUC" : "L", "AUC" : "I", "GUC" : "V",
               "UUA" : "L",    "CUA" : "L", "AUA" : "I", "GUA" : "V",
               "UUG" : "L",    "CUG" : "L", "AUG" : "M", "GUG" : "V",
               "UCU" : "S",    "CCU" : "P", "ACU" : "T", "GCU" : "A",
               "UCC" : "S",    "CCC" : "P", "ACC" : "T", "GCC" : "A",
               "UCA" : "S",    "CCA" : "P", "ACA" : "T", "GCA" : "A",
               "UCG" : "S",    "CCG" : "P", "ACG" : "T", "GCG" : "A",
               "UAU" : "Y",    "CAU" : "H", "AAU" : "N", "GAU" : "D",
               "UAC" : "Y",    "CAC" : "H", "AAC" : "N", "GAC" : "D",
               "UAA" : "Stop", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
               "UAG" : "Stop", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
               "UGU" : "C",    "CGU" : "R", "AGU" : "S", "GGU" : "G",
               "UGC" : "C",    "CGC" : "R", "AGC" : "S", "GGC" : "G",
               "UGA" : "Stop", "CGA" : "R", "AGA" : "R", "GGA" : "G",
               "UGG" : "W",    "CGG" : "R", "AGG" : "R", "GGG" : "G"}


def translateRna(inStr):
    # Helper variables
    outStr = []
    translatedRna = ""

    # Split into different 3 - lenhgt elements 
    while inStr:
        outStr.append(inStr[:3])
        inStr = inStr[3:]

    # Iterate over new list
    for element in outStr:
        # Iterate over dictionary 
        for k, v in rnaCodonTable.items():
            # Compare element with key
            if element == k:
                # If value == "Stop" break the loop
                if v == "Stop":
                    break
                # If element == k then add to translatedRna
                translatedRna += v

    # Return value
    return translatedRna

toTranslate = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
print translateRna(toTranslate)
