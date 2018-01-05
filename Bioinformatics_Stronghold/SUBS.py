#!/usr/bin/python


# Finding a Motif in DNA
# http://rosalind.info/problems/subs/
    
def subs(inputStr, searchStr):
    # Helper index
    firstIdx = 0
    
    # Empty list for found indexes
    idxList = []

    summary = 0
    
    while True:
        
        # Search subs in str
        # Because idx in Python starts from 0 not 1
        idx = inputStr.find(searchStr) + 1
        
        # Cut string
        inputStr = inputStr[idx:]
        
        # Break the loop after reach the end of inputStr
        firstIdx += idx

        if idx == 0:
            break

        
        # Append to list
        idxList.append(idx)

        
    return idxList

def countElements(elementsList):
    # Helper variables
    summary = 0
    summaryList = []

    # Iterate and add to list 
    for element in elementsList:
        summary += element
        summaryList.append(summary)

    return summaryList


inputStr = "CCACTACTTGTGGATGAGCCACTACCCACTACCCACTACTGGCGTCATATCCACTACTCCACTACCCACTACCTTCACCACTACGCCACTACCCACTACAGGCCACTACACCACTACCAACCACTACTTACCACTACGGTCCACTACCCCACTACCCCCCCACTACGCTCCACTACCCCACTACGGCGTCCACTACCCACTACCCACTACCCACTACTCCTCGCCACTACCCGACCACTACCCACTACAGATGCCACTACGTCCACTACCCACTACACCACTACGCCACTACGGCCACTACCCACTACCCACTACCCACTACCCACTACACCACTACTGCCACTACCCACTACTCCACTACAACCACTACCCCACTACTCCCACTACCCACTACCGGCACCACTACAACCACTACCCACTACCCACTACCTGCCCCACTACCCACTACCGCGATACCACTACCCCACTACACTAACCCCACTACCCACTACTAGGCCACTACCCACTACTCCACTACGCCACTACTCCACTACACCACTACAGTCCACTACCCCACTACATTTAACCACTACACCCACTACACCACTACATATTGTGCCACTACGTCCACTACCACCCCACTACCCCACTACGCCACTACCCACTACCCACTACCCACTACTCTCACCACTACCCCACTACTCTTCCACTACTCCACTACTACGCCCACTACCCCCCACTACTGCCACTACGCCACTACTCCACTACACCCGCCACTACCTACCCCGATCGCCACTACATAGGTACCCACTACCCCACCACTACTCCCTTTCCACTACGGAGCCCCACTACGACCTCACCACTACCCACTACTA"
searchStr = "CCACTACCC"

print countElements(subs(inputStr, searchStr))





