#!/usr/bin/python


# Function which iterate over file and write odd lines in new file
def oddLinesInFile(input_file, output_file):
    with open(output_file, 'w') as out_file:
        with open(input_file, 'r') as in_file:
            counter = 1
            for line in in_file:
                if counter % 2 == 0:
                    out_file.write(line)
                counter+=1
        return out_file


# Input and output files
input_file = "input.txt"
output_file = "output.txt"
oddLinesInFile(input_file, output_file)
