class Person:
    def __init__(self,Initialage):
        if(Initialage < 0):
            self.age=0
            print("Age is not valid, setting age to 0.")
        self.age=Initialage
    def yearPasses(self):
        self.age+=1
    def amIOld(self):
        if(self.age<13):
            print("You are young")
        elif(self.age >=13 and self.age < 18):
            print("You are a teenager")
        else:
            print("You are old")
t = int(input())
inp=[]
for i in range(0,t):
    age = int(input()) 
    inp.append(str(age))
for i in inp:
    p = Person(int(i))  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    
    print(" ")

