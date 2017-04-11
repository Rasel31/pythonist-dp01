import os
'''
for i in os.listdir():
    print(i)

file = 0
for i in os.walk("D:/"):
    print(i)
    file += 1
print(file)

'''


for i in os.listdir():
    if i.startswith('Picture'):
        print(i)
        os.chdir(i)
        #for i in range(100):
       #     os.mkdir('My dir '+ str(i))
        for i in os.listdir():
            print('->', i)
        break
    #print(type(i))

