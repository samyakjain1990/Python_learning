# Lets try to play with readline to read the complete file

file = open('ReadText.txt')
line = file.readline()

while line != "":
    print (line)
    line = file.readline()

file.close()