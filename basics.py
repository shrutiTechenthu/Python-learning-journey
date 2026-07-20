// Python calculator 

// 1st method
a=int(input("1st number:"))
b=int(input("2nd number:"))
print(a,b)
print("PYTHON CALCULATOR ")
print("Operations available: +,-,*,/,**")
option=input("enter the arithmetic operation ")
if option== "+":
    Add=a+b
    print(Add)
elif option== "-":
    Sub=a-b
    print(Sub)
elif option=="*":
    Multi=a*b and b*a
    print(Multi)
elif option== "/":
    Divi=a/b and b/a
    print(Divi)
elif option== "**":
    Expo=a**b and b**a
    print(Expo)
else:
    print("Operation not available ")



//2nd method
a=int(input("1st number:"))
b=int(input("2nd number:"))
print(a,b)
print("PYTHON CALCULATOR ")
print("Operations available: +,-,*,/,**")
option=input("enter the arithmetic operation ")
if option== "+":
    result=a+b
elif option== "-":
    result= a-b
elif option=="*":
    result=a*b and b*a
elif option== "/":
    result=a/b and b/a
elif option== "**":
    result=a**b and b**a
else:
    print("Operation not available ")
print(result)    
    
  
