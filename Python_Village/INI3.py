#!/usr/bin/python


# Strings and Lists
# http://rosalind.info/problems/ini3/


def slicing(text,a,b,c,d):
    first = text[a:b+1]
    second = text[c:d+1]
    return first, second

	
string = "gzEYWRFMzUxWjBiBBDvB0DzHScdVR7lYJRCK8lJPxP4H7jFelisTIT1XZcA5nyecB6Jacanthinura2C4ZGHr5uz0dfiwbj5tVazOSivn7D2dHvILgdk5e4CpdLKkv8YnbruPervJ2ZQue3wrvivUCJIFSqqww9qYu9YSpH51.."
a = 46
b = 50
c = 67
d = 77


print slicing(string, a, b, c, d)
