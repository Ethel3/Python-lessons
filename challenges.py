# use the slice trick to reverse the string
# def is_palindrome(teststr):
#     if teststr == teststr[::-1]:
#         return True
#     return False
# run = True
# while (run):
#     teststr = input ("Enter string to test for palindrome or 'exit':")
    
    # if the "user"types exist then quit the program
    # if teststr == exit:
    #     run = False
    #     break
    
    # convert the string to all lower case
    # teststr = teststr.lower()
    
    # strip all the spaces and punctuation from the string
    # newstr = ""
    # for x in teststr:
    #     if x.isalnum():
    #         newstr += x
    # print("Palindrome test:", is_palindrome(newstr))
    
    # new challenge
# import os 
    
# totalbytes = 0

# get a list of all the files in the current directory
# dirlist = os.listdir()
# for entry in dirlist:
    # make sure it's a file!
    # if os.path.isfile(entry):
        # add the file size to the total
        # filesize = os.path.getsize(entry)
        # totalbytes += filesize
# create  a subdirectory called "results"
# os.mkdir("results")

# create the output file 
# resultsfile = open("results/results.txt", "w+")
# if resultsfile.mode == "w+":
#     resultsfile.write("Total bytecount:" + str(totalbytes) + "\n")
#     resultsfile.write("Files list:\n")
#     resultsfile.write("--------------\n")
    
    # write the results into the file
    # for entry in dirlist:
    #     if os.path.isfile(entry):
            # write the file name to the results ledger
            # resultsfile.write(entry + "\n")
    # close file
    # resultsfile.close()
    
# #challenge: Date and Time
import calendar 

# This function counts specific number of the given weekdayfor the spcific month
# def countdays(theyear, themonth, whichday):
#     daycount = 0
#     weekslist = calendar.monthcalendar(theyear, themonth)
#     for week in weekslist:
#         if week[whichday] != 0:
#             daycount += 1
#     return daycount

# print("--Day counter program--\n")

# run = True
# while(run):
#     try:
#         print("Which day of the week do you want to count?")
#         print("0: Monday")
#         print("1: Tuesday") 
#         print("2: Wednesday") 
#         print("3: Thursday") 
#         print("4: Friday") 
#         print("5: Saturday") 
#         print("6: Sunday") 
#         print("Or 'exit' to quit")     
        
#         theday = input("? ")
#         if theday == "exit":
#             run = False
#             break 
#         day = int(theday)
        
#         yearstr = input("Enter year: ")
#         year = int(yearstr)
        
#         monthstr = input("Enter month: ")
#         month = int(monthstr)
        
#         result = countdays(year, month, day)
#         print("There are" + str(result) + "of those days in the month and year specified")
#         print("---------\n")
#     except Exception as e:
#         print(e)
#         print("Sorry, that's not a valid input")