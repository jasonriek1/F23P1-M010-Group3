import pandas as pd
#task 1 



#task 2


#task 3


#task 4 work in progress
def readncreate(p1: str):
    #reading in file and then closing it
    txt = open("textfile.txt")
    readin = txt.read()
    txt.close()
    #use function 2 which idk what it looks like to go through all the text in the text fil
    '''funcfromtask2(readin)
    for value in range(len(outputfromfuncfromtask2)):
        length += len(outputfromtask2[value])
    
    '''
    #writing D.B
    '''
    wrt = (length.outputfromtask2)
    bins = open("BinOutput.txt")
    wrt.write("BinOutput.txt")
    bins.close()
   ''' 

#task 5 work in progress

def task5(p1: str):
    # reading in file and then closing it
    bins = open("BinOutput.txt")
    readin = bins.read()
    bins.close()

    # have to write in quotes bc don't actually have function from task 3.
    '''task3pt1(readin)
    task3pt2(outputfromtask3)

    text = open("TextOutput.txt.")
    outputfromtask3pt2.write("TextOutput.txt")
    text.close()
'''

#task 6
#Returns true if both text files are equal
#opens both files and puts them into a variable
#evaluates both to see if they are equal in the return statement
def areFilesEqual(fileName1, fileName2): #files names must be inputed in double qoutes. ex. areFilesEqual("placeholder1.txt", "placeholder2.txt")
    f = open(fileName1) #opens file one
    s1 = f.read() #turns contents of file one into string
    f.close()
    f = open(fileName2) #opens file two
    s2 = f.read() #turns contents of file two into string
    f.close()
    return s2==s1 #true if equal false otherwise
