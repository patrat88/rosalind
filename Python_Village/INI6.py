#!/usr/bin/python

# Dictionaries
# http://rosalind.info/problems/ini6/


string = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"


def countStrWords(string):
    # Initialize dictionary
    spl_dict = {}

    # Split string
    spl_str=string.split()

    # Iterate over splited string
    for element in spl_str:
        # Check if key exist if not add it to a dictionary with value 1
        if not spl_dict.has_key(element):
            spl_dict[element] = 1
        # If key exist add 1 to value 
        else:
            spl_dict[element]+=1

    return spl_dict

	
# Print output 
for k, v in countStrWords(string).items():
    print k, v
