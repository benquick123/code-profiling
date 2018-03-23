import os

mypath = 'path'

for file in os.listdir(mypath):
    write = True
    with open(mypath + file, 'r', encoding = 'UTF-8') as input:
        with open(mypath + file, 'w', encoding = 'UTF-8') as output:
            for line in input:
                if line == 'import unittest\n':
                    write = False
                if write:
                    output.write(line)
