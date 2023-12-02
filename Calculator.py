#Function to add two numbers

def add(x,y):
    return x + y

#Function to subtraction two numbers

def subtract(x,y):
    return x - y

#Function to multiplication two numbers

def multiplication(x,y):
    return x * y

#Function to divition two numbers

def divition(x,y):
    if y == 0:
        return "Syntax Error"
    return x / y

print("Chose which arithmetic operation you want to do :")
print("Press 1 for addition.")
print("Press 2 for subtraction.")
print("Press 3 for multiplication.")
print("Press 4 for division.")

while True:
    c = (input("Enter your choice : "))

    if c in('1','2','3','4'):
        a = float(input("Enter First Number : "))
        b = float(input("Enter Second Number : "))
        if(c=="1"):
            print("The addition of Two numbers is : ",add(a, b))
            
        elif(c=="2"):
            print ("The subtraction of Two numbers is : ",subtract(a, b))
            
        elif(c=="3"):
            print ("The multiplication of Two numbers is : ",multiplication(a,b))
            
        elif(c=="4"):
            print ("The divition of Two numbers is : ",divition(a,b))
        break
    else:
        print("Invalid Input")
   


