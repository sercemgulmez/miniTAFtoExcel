import csv
from os import listdir
from os.path import isfile, join

file = open("miniTAF.csv", 'w')
str = ""
mypath = "D:\\Users\\gulms\\PycharmProjects\\miniTAF"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)
i = 0
j = 0

str = ""
name = ""
suite = ""
for filename in onlyfiles:
    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        if line.find("Test-suite file") != -1:
            suite = ""
            for letter in line:
                if letter == '=':
                    i = i + 1
                if i == 2 and letter != '=' and letter != '-':
                    suite += letter
            file.write("\n"+suite+"\n")
            print(suite)
        if line.find("Testcase file") != -1:
            name = " "
            for letter in line:
                if letter == '=':
                    i = i + 1
                if i == 2 and (letter == ":" or (letter == "-" and j > 1)):
                    break
                if (i == 2 and letter == "-"):
                    j = j + 1
                else:
                    j = 0
                if i == 2 and letter != '=':
                    name += letter
        if line.find("TC;tc") != -1:
            str = ""
            if "PASSED" in line:
                str = ";PASSED\n"
            elif "FAILED" in line:
                str = ";FAILED\n"
            elif "INACTIVE" in line:
                str = ";INACTIVE\n"

            print(name + " -> " + str)
            file.write(name + str)
        i = 0
        j = 0
file.close()