def function_sub(num1, num2):
    return num1 - num2

def function_multi(num1, num2):
    return num1 * num2

def function_div(num1, num2):
    return num1 / num2

def function_add(num1, num2):
    return num1 + num2

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))

print()

c = int(input("1. Sum\n2. Sub\n3. mul\n4. Div\n\nEnter choice: "))

print()

if c == 1:
    l = function_add(a, b)
    print('Summation:',a,'+',b,'=',l)
elif c == 2:
    m = function_sub(a, b)
    print('Subtraction:',a,'-',b,'=',m)
elif c == 3:
    n = function_multi(a, b)
    print('Multiplication:',a,'*',b,'=',n)
elif c == 4:
    o = function_div(a, b)
    print('Division:',a,'/',b,'=',o)







































'''number = int(input("Enter number: "))
end_num = int(input("Enter numbre: "))

k = number

x = int(input("Enter line number: "))

for i in range (1, x+1):
    for j in range (i):
        print(number, end=' ')
   

        if number == end_num:
            number = k
        else:
            number += 1
    print()
'''
