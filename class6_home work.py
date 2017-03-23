

print("Name: Rasel")
print("Mobile: 01684768264")
a = eval(input("Result: "))

if a>=80 and a<=100:
    print("Grade: A+")
elif a>=70 and a<80:
    print("Grade: A")
elif a>=60 and a<70:
    print("Grade: A-")
elif a>=50 and a<60:
    print("Grade: B")
elif a>=0 and a<50:
    print("Grade: Fail")
else:
    print("Error!!!")
    
print("\n\n\n")

a = eval(input("a = "))
b = eval(input("b = "))
c = eval(input("c = "))

if a==b==c:
    print("All inputs are same")
    
elif a==b:
    
    if a>c:
        print("a is equal to b and both are greater than c")
        
    else:
        print("a is equal to b and c is greater than a, b")
        
elif a==c:
    
    if a>b:
        print("a is equal to c and both are greater than b")
        
    else:
        print("a is equal to c and b is greater than a, c")
        
elif b==c:
    
    if b>a:
        print("b is equal to c and both are greater than a")
        
    else:
        print("b is equal to c and a is greater than b, c")
        
elif a>b and a>c:
    print("a is greater than b, c")
    
elif b>a and b>c:
    print("b is greater than a, c")
    
elif c>a and c>b:
    print("c is greater than a, b")

