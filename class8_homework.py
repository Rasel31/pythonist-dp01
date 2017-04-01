my_number = 35

counter = 5

a = eval(input("Enter Your Number: "))

while counter != 0:

    if a == my_number:
        print("\nCongrates.You Won!!!")
        break

    counter -= 1

    if counter == 0:
        break

    if a > my_number:

        print("Your Number IS Greater Than My Number. Your Chance Is Left ", counter)
    elif a < my_number:
        print('Your Number IS Less Than My Number. Your Chance Is Left ', counter)

    a = eval(input("Enter Your Number: "))

if counter == 0 and a != my_number:
    print("\nOops.You Loose!!!")



