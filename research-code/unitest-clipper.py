import os

mypath = '../code/batch-2/dn14 - zoge/'
newpath = '../code/batch-2/vse-naloge-brez-testov/'
dn_n = "DN14"

for file in os.listdir(mypath):
    write = True
    with open(mypath + file, 'r', encoding="utf-8") as input:
        print(file)

        file_id = file.split("-")[1][2:]
        file_gender = file.split("-")[0]
        newfile = dn_n + "-" + file_gender + "-" + file_id + ".py"

        with open(newpath + newfile, 'w', encoding="utf-8") as output:
            for line in input:
                if line == 'import unittest\n':
                    write = False
                if write:
                    output.write(line)
