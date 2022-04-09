# Lets try to play with readlines to read the complete file in the list

file = open('ReadText.txt')

for item in file.readlines():
    print(item)

file.close()