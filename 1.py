#!/usr/bin/python3
import os
import re
import itertools
def StringToList(string):
        list_result= list(string.split("\n"))
        return list_result

def pairwise(iterable):
        "s -> (s0,s1), (s1,s2), (s2, s3), ..."
        a, b = itertools.tee(iterable)
        next(b, None)
        return zip(a, b)

temp=" "
with open('domains.txt') as f:
        lines = f.readlines()

for line in lines:
        line = line.strip()
        temp+=(os.popen('nslookup '+ line).read())

re.split('; |, |\*|\n',temp)


l=StringToList(temp)

mylist =[]
for a,b in pairwise(l):
        if b=='Address: 217.16.95.36':
                mylist.append(a)

out = open('final.txt','w')

for item in mylist:
        out.write("%s\n" % (item.strip("Name:  ")).strip())

print("Done!")
