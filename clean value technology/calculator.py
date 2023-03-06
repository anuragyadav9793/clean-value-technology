def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
while True:
    num1 = input("enter the first parameter")
    if(num1 == "exit"):
        break
    else:
        num1=int(num1)
        op = input("enter operator")
        num2 = float(input("enter the second parameter"))
        if(op=='+'):
            print(add(num1,num2))
        elif(op=='-'):
            print(subtract(num1,num2))
        elif(op=='*'):
            print(multiply(num1,num2))
        elif(op=='/'):
            print(divide(num1,num2))
        else:
            print("invalid operator")                