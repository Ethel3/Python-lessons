# use the slice trick to reverse the string
def is_palindrome(teststr):
    if teststr == teststr[::-1]:
        return True
    return False
run = True
while (run):
    teststr = input ("Enter string to test for palindrome or 'exit':")
    
    # if the "user"types exist then quit the program
    if teststr == exit:
        run = False
        break
    
    # convert the string to all lower case
    teststr = teststr.lower()
    
    # strip all the spaces and punctuation from the string
    newstr = ""
    for x in teststr:
        if x.isalnum():
            newstr += x
    # print("Palindrome test:", is_palindrome(newstr))
    
    # new challenge
import os 
    
totalbytes = 0

# get a list of all the files in the current directory
dirlist = os.listdir()
for entry in dirlist:
    # make sure it's a file!
if os.path.isfile(entry):
    # add the file size to the total
    filesize = os.path.getsize(entry)
    totalbytes += filesize
# create  a subdirectory called "results"
os.mkdir("results")

# create the output file 


    
    