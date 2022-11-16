#functions
# def main():
#     x, y = 10, 100
#     #conditional flow uses if, elif, else
#     # if x < y:
#     #     result = "x is less than y"
#     # elif x == y:
#     #     result = "x is the same as y"
#     # else:
#     #     result = "x is greater than y"
#     # print(result)
    
#     # conditional statements  let you use "a if c else b"
#     # result = "x is less than y" if x < y else "x is greater or equal to y"
#     # print(result)
    
#     # match-case makes it easy to compare multiple values 
#     value = "two"
#     match value:
#         case "one":
#             result = 1
#         case "two":
#             result = 2
#         case "three" | "four":
#             result = (3,4)
#         case _:
#             result= -1
#     print(result)
# if __name__== "__main__":
#     main()
    
    # classes
# class Vehicle():
#     def __init__(self, bodystyle):
#         self.bodystyle = bodystyle
        
#     def drive(self, speed):
#         self.mode = "driving"
#         self.speed = speed
        
# class Car(Vehicle):
#     def __init__(self, enginetype):
#         super().__init__("Car")
#         self.wheels = 4
#         self.doors = 4
#         self.enginetype = enginetype
        
#     def drive(self, speed):
#          super().drive(speed)
#          print("Driving my", self.enginetype, "Car at", self.speed)
    
        
# class Motorbike(Vehicle):
#     def __init__(self, enginetype, hassidecar):
#         super().__init__("Motorbike")
#         if (hassidecar):
#             self.wheels = 3
#         else:
#             self.wheels = 2
#         self.doors = 0
#         self.enginetype = enginetype
        
#     def drive(self, speed):
#          super().drive(speed)
#          print("Driving my", self.enginetype, "Motorbike at", self.speed)
        
# car1 = Car("gas")
# car2 = Car("electric")
# mb1 = Motorbike("gas", True)

# print(mb1.wheels)
# print(car1.enginetype)
# print(car2.doors)

# car1.drive(40)
# car2.drive(50)
# mb1.drive(70)


# parsing and processing html
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print("Encountered a comment:", data)
        pos = self.getpos()
        print("At line:", pos[0], "position",pos[1])
        
    
    def handle_starting(self, tag, attrs):
        pass
    
    def handle_data(self, data):
        if data.isspace():
            return
        print("Encountered text data:", data)
        pos = self.getpos()
        print("At line:", pos[0], "position",pos[1])
        
    
def main(): 
    # feeding the parser with html
    parser = MyHTMLParser()
    
    f = open("samplehtml.html")
    if f.mode == "r":
        contents = f.read() #read the entire file
        parser.feed(contents)
        
        
if __name__== "__main__":
    main()
    