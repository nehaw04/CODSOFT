def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    if n2!=0:
        return n1/n2
    else:
        return "Error:division by zero not allowed"


while True:
    print("Select Operation")
    print(
        "1.Addition\n"
        "2.Subtraction\n"
        "3.Multiplication\n"
        "4.Division\n"
        "5.Exit")
    ch=int(input("enter your choice of operation"))
    if ch==5:
        break
    n1=int(input("enter the fisrts number"))
    n2=int(input("enter the second number"))
    print("-----------------------------")
    if ch==1:
        print("result of addition:")
        print(n1,"+",n2,"=",add(n1,n2))
       
    elif ch==2:
        print("result of Subtraction:")
        print(n1,"-",n2,"=",subtract(n1,n2))
        
    elif ch==3:
        print("result of multiplication:")
        print(n1,"*",n2,"=",multiply(n1,n2))
        
    elif ch==4:
        print("result of Division:")
        print(n1,"/",n2,"=",divide(n1,n2))
    else:
        print("Invalid Imput ,enter valid numbers")
    print("-----------------------------")
    



