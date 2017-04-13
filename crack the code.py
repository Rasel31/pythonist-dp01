lock = ['0', '4', '2']
ul = []

ui = input("Enter 3 digit code: ")

ul.extend(ui)

counter = 0
counter1 = 0
for i in range(3):
    if ul[i] in lock:
        if lock[i] == ul[i]:
            counter += 1
        else:
            counter1 += 1

if counter == 3:
    print("WELCOME!!!")
elif counter1 == 3:
    print("3 Numbers is correct but wrong placed")
elif counter == 2:
    print("2 Numbers is correct and well placed")
elif counter1 == 2:
    print( "2 Numbers is correct but wrong placed")
elif counter == 1:
    print("1 Numbers is correct and well placed")
elif counter1 == 1:
    print("1 Numbers is correct but wrong placed")

counter = 0
for i in range(3):
    for j in range(3):
        if ul[i] != lock[j]:
            counter += 1

if counter == 9:
    print("Nothing is correct")

