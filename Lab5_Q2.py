import string
import sys
import re

filepath = 'G:\\GIS_501\\Labs\\Lab_5\\HP_Lovecraft.txt'
inp = open(filepath)
sentences = inp.read()


#longest sentence
text = ''.join(open('G:\\GIS_501\\Labs\\Lab_5\\HP_Lovecraft.txt').readlines())
sent = re.split(r' *[\.\?!][\'"\)\]]* *', text)

max_length, longest_element = max([(len(x), x) for x in (sent)])

#shortest sentence
textfile = ''.join(open('G:\\GIS_501\\Labs\\Lab_5\\HP_Lovecraft.txt').readlines())
short = re.split(r' *[\.\?!][\'"\)\]]* *', textfile)

min_length, shortest_element = min([(len(x), x) for x in (short)])

print "Shortest sentence is:" + " " + min(short, key=len)
print "Longest sentence is:" + " " + max(sent, key=len)

