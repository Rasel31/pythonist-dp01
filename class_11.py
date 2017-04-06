def is_prime(a):
    
    b = int(a/2)
    b += 1

    if a == 2:
        return True
    elif a == 4 or a <= 1:
        return False
    
    for i in range(3, b, 2):
        
        if a%i == 0:
            return False
        
    return True
            

while True:
    
    user_input = eval(input("Enter Number: "))

    r = is_prime(user_input)

    print("\nIs",user_input,"A Prime Number: ", r)
    
    c = (input("\nYou Want to Do It Again? y/n -> "))
             
    if c == 'n' :
         break
