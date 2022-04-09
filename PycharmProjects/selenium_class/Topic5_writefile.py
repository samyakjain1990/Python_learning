# there is a new way  of reading the file 

from audioop import reverse


with open('ReadText.txt','r') as reader:
    content =reader.readlines()
    '''
    # reveresed content can never be printed
    rev_content = reversed(content)
    print(rev_content)

    '''
    # reverse content in a file
    #reversed(content)

    with open('WriteText.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)
            writer.write('\n')