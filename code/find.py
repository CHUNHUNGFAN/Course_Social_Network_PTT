file = open("output3.txt",'r')
fileR = file.readlines()

for line in fileR:
    line = line.split()
    if int(line[1]) >= 100:
        _string = line[0] + " " + line[1]
        print(_string)