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