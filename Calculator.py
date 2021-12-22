# Python program for simple calculator  


x = 2
while x > 1:
    x=int(input("What is your first integer?"))
    y=int(input("What is your second integer?"))

# Function to perform addition 
    def add(x,y ): 
        return x+y
 
# Function to perform subtraction
    def subtract(x,y):
        return x-y
  
# Function to perform multiplication
    def multiply(x,y): 
        return x*y
  
# Function to dividision 
    def divide(x,y): 
        return x/y
        
#Function to take module
    def module(x,y):
        return x%y
       
#Function to perform floordivision
    def floordivide(x,y):
        return x//y
       
#Operations to be perfomed  
    print("Please select operation -\n"
          "1. Add\n" 
          "2. Subtract\n" 
          "3. Multiply\n"
          "4. Divide\n" 
          "5. Modulus\n"
          "6. Floor Division\n") 
    
    
# Take input from the user  
    select = int(input("Select operations form 1 to 6 :")) 
 
    if select == 1: 
        print(x, "+", y, "=",  add(x,y)) 
  
    elif select == 2: 
        print(x, "-", y, "=",  subtract(x,y)) 

    elif select == 3: 
        print(x, "*", y, "=",  multiply(x,y)) 
  
    elif select == 4: 
        print(x, "/", y, "=",  divide(x,y)) 

    elif select == 5:
        print(x, "%", y, "=",  module(x,y))
     
    elif select == 6:
        print(x, "//", y, "=",  floordivide(x,y))
    
    answer=int(input("Would you like to continue? Press 1: "))

    if answer == 1:
        x == 2
          
    else:
        break