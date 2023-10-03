import pandas as pd
#task 1 



#task 2


#task 3

def func4(p1: str):
    #opens the file and read in values and then closes it
    o = open(p1)
    r = o.read()
    o.close()
    #run a loop through r, everytime we run we use func2, add the first part to our values, then take away the first
    #part of r, until r is empty.
    values = ""
    while r:
        holder = func2(r)
        values += holder[0]
        r = holder[1]
    # here we make our D.B out put for the output file by counting the bits and then adding a ., have to make it a string
    # so we don't get an int there.
    firstnum = str(len(values)) + "."
    writing = firstnum + values

    #here we just write out d.b output into BinOutput
    opening = open("BinOutput.txt", "w")
    opening.write(writing)
    opening.close()

def func5(p1 = "BinOutput.txt"):
    #opening and reading in the file
    o = open(p1)
    r = o.read()
    o.close()
    #slicing off the begginning part that tells us how many bits we use so it doesn't give us an error.
    b = r.find(".")
    r = r[b+1:]
    #here we use the functions from 3 to get the chars back from out binary values.
    a = ""
    lofbins = func3pt1(r)
    for n in range(len(lofbins)):
        a += func3pt2(lofbins[n])

    #here we just write our chars, the stuff in a, into textoutput
    opening = open("TextOutput.txt", "w")
    opening.write(a)
    opening.close()


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
