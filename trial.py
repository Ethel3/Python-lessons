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
# values = [1, 2, 3, 4, 5, 6, 7]
# values.append(8)
# print(values)

#inserting a value in the middle 
# values = [1, 2, 3,  5, 6, 7,8]
# values.insert(3, 4)
# print(values)

#removing a value
# values = [1, 2, 3,  5, 6, 7,8]
# values.remove(6)
# print(values)


#removing all values
# values = [1, 2, 3,  5, 6, 7,8]
# values.clear()
# print(values)

#checking for an item in the range
# values = [1, 2, 3, 4, 5, 6]
# print(6 in values)

#length of function
# print(len(values))



# for loops
# values = [1, 2, 3, 4, 5, 6]          #i = 0
# for number in values:                #while i < len(values):
#     print(number)                           #print(values[i])
                                            #i = i +1
                                            
#range function
# values = range(6) # range(3, 9) # range(5, 10, 2)
# for value in values:
#     print(value)
    
    
#set is a collection with no duplicate. It does not support indexing.
# numbers = [1,2,2,3,3,4,5]
# uniques = set(numbers)
# print(uniques)

# numbers = [1,2,2,2,3,3,3,4]
# first = set(numbers)
# second = {2,3,5,6,6,7,8,9,10}
# print(first | second) 
# print(first & second)
# print(first - second)
# print(first ^ second)

# if 2 in first:
#     print("yes")

#Dictionary in python: collection that has key value pairs.
schools = {1: "legon", 2: "knust", 3:"ashesi", 4:"ucc"}
# print(schools)
print(schools.get(3))

# schools[2] = "Academic City"
# print(schools)
# print(schools.popitem())

mydictionary = dict(key1 = "legon", key2= "knust")
print(mydictionary)

num = { 1: 2, 2: 4, 3: 5,}
print(num.fromkeys(mydictionary))

#use case
