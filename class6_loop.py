'''
l = range(10)

print(l)

print(type(l))
for i in [2,4,5,10]:
    print(i)


a = "A"

b = ord(a)

print(b)


#for i in range(100):
#   print(ord(str(i)))


username = (input("Enter Username: "))
password = (input("Enter Password: "))

if len(password) < 6:
    print("Password Weak")
else:
    print("Password Strong")


name = ['rasel', 'khan', 'others']

print('rasel' in name)

