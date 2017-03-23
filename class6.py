#                  if....else
'''
a =eval(input("Enter 1st Number: "))
print()
b =eval(input("Enter 2nd Number: "))
print()
c =eval(input("Enter 3rd Number: "))

if a > b:
    if a > c:
        print(a,"is greater than",b,c)

    else:
        print(c,"is greater than",a,c)
    
elif b > a:
    if b > c:
    
        print(b,"is greater than",a, c)
    else:
        print(c,"is greater than",a, b)
else:
    if c > a:
        print(c,"is greater than",a, b)
    else:
        print(a,"is greater than",b , c)
    
'''

