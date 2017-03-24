print("By For Loop\n")

for i in range(1, 6):
    
    for j in range(1, 7 - i):
        
        print('*', end = ' ')
        
    print()

print()

for i in range(5):
    
    for j in range(4 - i):
        
        print(" ", end = ' ')
        
    for k in range(i + 1):
        
            print('*', end = ' ')
            
    print()

print()

c = 1

for i in range(1, 6):
    
    for j in range(i):
        
          print(c , end = ' ')
          
          c += 1
          
          if c > 5:
              
             c = 1        
    print()

print()

print("By While Loop\n")

i = 1

while i <= 5:
    
    j = 1
    
    while j <= 6 - i:
        
        print('*', end = ' ')
        
        j += 1
        
    print()
    
    i += 1

print()

i = 1

while i <= 5:

    j = 1
    
    while j <= 5 - i:
        
        print(" ", end = ' ')
        
        j += 1
        
    k = 1
    
    while k <= i:
        
        print("*", end = ' ')
        
        k += 1
        
    print()
    
    i += 1

print()

c = 1

i = 1

while i <= 5:
    
    j = 1
    
    while j <= i:
        
        print(c, end = " ")
        
        c += 1
        
        j += 1
        
        if c > 5:
            
            c = 1
            
    print()
    
    i += 1




    
