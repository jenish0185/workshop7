inputfile = open("inp.txt", "r")
outputfile = open("out.txt", "w")

for line in inputfile : 
    outputfile.write(' '.join(line.split()))

inputfile.close()
outputfile.close()
