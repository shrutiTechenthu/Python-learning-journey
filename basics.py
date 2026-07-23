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
    


// Last digit of a number 
num=int(input("enter the number "))
last_digit=num%10
print(last_digit)


//Even no
num=int(input("enter the number "))
remainder=num%2
if remainder==0:
    print("Given number is even ")
else:
    print("Given number is odd and it's remainder is", remainder) 


//vowel
char=input("enter single character ")
if char in ("a","e","i","o","u"):
    print("vowel")
else:
    print("Consonant ")
  
