#while loop
# i = 1
# while i <= 1_000:
#     print(i)
#     i = i + 1
#    
# i = 1
# while i <= 10:
#     print(i * "*")
#     i = i + 1

#lists
# schools = ["Legon", "UCC", "KNUST", "UEW", "Ashesi"]
# print(schools)

#printing with index
#print(schools[2] or [-3])

#updating in lists
# schools = ["Legon", "UCC", "KNUST", "Ashesi", "Mines"]
# schools[-1] = "IPMC"
# print(schools)

#selecting ranges
# print(schools[1:3])

#list methods
values = [1, 2, 3, 4, 5, 6, 7]
values.append(8)
print(values)

#inserting a value in the middle 
values = [1, 2, 3,  5, 6, 7,8]
values.insert(3, 4)
print(values)

#removing a value
values = [1, 2, 3,  5, 6, 7,8]
values.remove(6)
print(values)


#removing all values
values = [1, 2, 3,  5, 6, 7,8]
values.clear()
print(values)

#checking for an item in the range
values = [1, 2, 3, 4, 5, 6]
print(6 in values)

#length of function
print(len(values))



# for loops
values = [1, 2, 3, 4, 5, 6]          #i = 0
for number in values:                #while i < len(values):
    print(number)                           #print(values[i])
                                            #i = i +1