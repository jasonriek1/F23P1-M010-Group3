import pandas as pd

# task 1
# reads Excel file and makes it into a list of bins and chars, also changes \\n to \n
wb = pd.read_excel('F23P1-M010-Group3.xlsx', dtype=str)
bins = list(wb["Bin"])  # set the column 2 list (Bin) = to the variable "bins"
chars = list(wb["Char"])  # set the column 1 list (Char) = to the variable "chars"

if "\\n" in chars:  # if you find \\n in the chars list...
    chars[chars.index("\\n")] = "\n"  # set \\n = to \n

# task 2
'''
This function takes a string and checks the length of the string 
and then checks to see if it  matches anything in the chars list
Then, uses its index to find the corresponding binary
'''
def string_to_binary(p1: str):
    # checks for char of length 3, we have 3 in our Excel file
    if len(p1) >= 3:
        working_string = p1[0:3]  # takes first 3 characters
        for i in range(len(chars)):
            if chars[i] == working_string:  # if we have those 3 characters in our character list
                p1 = p1[3:]  # cut out the first 3 chars
                bin_value = bins[i]  # find corresponding bin value
                return bin_value, p1

    # checks for char of length 2, we have 4 in our Excel file
    if len(p1) >= 2:
        working_string = p1[0:2]  # We only care about the first two characters
        for i in range(len(chars)):
            if chars[i] == working_string:  # if we have those 3 characters in our character list
                p1 = p1[2:]  # Take out the first 2 characters we were working with
                bin_value = bins[i]  # find corresponding bin value
                return bin_value, p1
    # checks for char of length 1, ie. single letters, numbers, or punctuation
    if len(p1) >= 1:
        working_string = p1[0:1]
        for i in range(len(chars)):
            if chars[i] == working_string:
                if len(p1) > 1:
                    p1 = p1[1:]
                else:
                    p1 = ''
                bin_value = bins[i]
                return bin_value, p1


# task 3a (from slides)
# This function cuts apart the input into either short or long bits
def first_binary(p1: str):
    ourlist = []
    while p1:
        flag = p1[0]  # checks whether it's a short character or long (short start w/ 0, long w/ 1)
        if flag == "0":
            # short characters = 5 bits
            working_bin = p1[0:5]  # cuts out the first 5 bits
            ourlist.append(working_bin)
            p1 = p1[5:]  # this is what is left
        else:
            # long characters = 7 bits
            working_bin = p1[0:7]
            ourlist.append(working_bin)
            p1 = p1[7:]
    return ourlist


# task 3b
# This function takes the binary number we cut out and uses its index from
# our list to match it to the corresponding char
def binary_to_string(p1: str):
    i = bins.index(p1)
    return chars[i]


# task 4
# This converts the text file to binary and writes it to BinOutput
def func4(p1: str):
    # opens the file and reads in values and then closes it
    o = open(p1)
    r = o.read()
    o.close()
    # run a loop through r, every time we run we use string_to_binary, add the first part to our values, then take away the first
    # part of r, until r is empty.
    values = ""
    while r:
        holder = string_to_binary(r)
        values += holder[0]
        if len(holder) >= 2:
            r = holder[1]
        else:
            r = ""
    # Here we make our D.B output for the output file by counting the bits and then adding a ., we have to make it a string
    # so we don't get an int there.
    firstnum = str(len(values)) + "."
    writing = firstnum + values

    # here we just write out d.b output into BinOutput
    opening = open("BinOutput.txt", "w")
    opening.write(writing)
    opening.close()


# task 5
# This takes our BinOutput and converts it back into text and writes it to TextOutput
def func5(p1="BinOutput.txt"):
    # Opening and reading in the file
    o = open(p1)
    r = o.read()
    o.close()
    # Slicing off the beginning part that tells us how many bits we use so it doesn't give us an error.
    b = r.find(".")
    r = r[b + 1:]
    # Here we use the functions from 3 to get the chars back from our binary values.
    a = ""
    lofbins = first_binary(r)
    for n in range(len(lofbins)):
        a += binary_to_string(lofbins[n])

    # here we just write our chars, the stuff in a, into text output
    opening = open("TextOutput.txt", "w")
    opening.write(a)
    opening.close()


# task 6
# Returns true if both text files are equal
# opens both files and puts them into a variable
# evaluates both to see if they are equal in the return statement
def areFilesEqual(fileName1, fileName2="TextOutput.txt"):  # files names must be inputed in double-quotes. ex. areFilesEqual("placeholder1.txt", "placeholder2.txt")
    f = open(fileName1)  # opens file one
    s1 = f.read()  # turns contents of file one into string
    f.close()
    f = open(fileName2)  # opens file two
    s2 = f.read()  # turns contents of file two into string
    f.close()
    return s2 == s1  # true if equal false otherwise


# This just runs our thing and makes sure it's right.
def checker(p1):
    func4(p1)
    func5()
    return areFilesEqual(p1, "TextOutput.txt")
