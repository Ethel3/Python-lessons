#exercise
W = int(input("Weight: "))
U = input("(K)g or (L)bs: ") 
if U.upper() == "K":
    converted = W / 0.45
    print("Weight in Lbs: " + str(converted))  
else:
    converted = W * 0.45
    print("W in kgs: " + str(converted))

