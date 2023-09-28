import pandas as pd
#task 1 



#task 2



#task 3


#task 4


#task 5


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
