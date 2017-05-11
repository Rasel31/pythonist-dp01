'''
l = []
a =[]
for i in range(5):
    l.append(i + 1)

print()
print(l)

a = l[1] + l[2]

b = a + l[-1]

print(b)

print()

a = (l[::-1])

print(a)

v = a[1] +a[2]

c = v + a[-1]

print(c)


print('EVEN 1 to 50')

for i in range(2,51,2):

    if 25 <= i <= 35:

        continue

    else:

        print(i)


print('ODD 1 to 50')

i = 1

while i < 51:

    if 25 <= i <= 35:

        pass

    else:

        print(i)

    i += 2


print("EVEN\t\tODD")

for i in range(1,101):
    if i % 2 == 1:
        print(i, end='\t\t\t')

    if i % 2 == 0:
        print(i )

print('EVEN\t\tODD')
i = 1
while i <= 100:
    print(i, end = '\t\t\t')
    i += 1
    print(i)
    i += 1
'''
a = []
for i in range(10):
    c = input("Enter your name: ")
    a.insert(i, c)

    if i >= 1:
         if c == a[i-1]:
            continue

    print("Hi...",c)

