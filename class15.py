def square(a, b):
    return (a + b) * (a + b)

def queeb(a, b):
    return (a - b) ** 3

a = eval(input("Enter Value of A: "))
b = eval(input("Enter Value of B: "))

print()

print('('+str(a),'+',str(b)+')'+'^2','=',a ,'*', a,'+ 2','*', a,'*', b, '+', b, '*', b, '=', square(a,b))

print()

print('('+str(a),'-',str(b)+')'+'^3','=',a ,'*', a,'*', a, '+ 3','*', a,'*',a,'*', b, '+ 3','*', a, '*', b, '*', b, '=', queeb(a,b))
