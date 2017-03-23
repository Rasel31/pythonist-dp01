'''
for i in range (2000):
   print(i,"-",chr(i))

i = 0

while i<= 100:
    
    print(i,"-",chr(i))
    i+=1

h = int(input())


sum =0
for i in range(3):
    for j in range(5):
        sum+=1
        print(sum, end="\t")
    print()

    
print()


i = 0
sum=0
while i<3:
    j = 0
    while j<=4:
        sum+=1
        print(sum, end="\t")
        j += 1
    print()
    i += 1

print()
  
count = 0
for i in range(15):
    
    if count == 5:
        count = 0
        print()
    print(i+1, end='\t')
    count+=1

print()

for i in range(1, 16):
    print(i, end= '\t')
    if i%5 == 0:
        print()

print()

for i in range(1, 26):
    print(i, end= '\t')
    if i%5 == 0:
    
        print()
'''
print('Triangle')

for i in range(5):
    for j in range(i+1):
        print('*', end='\t')
    print()
    

