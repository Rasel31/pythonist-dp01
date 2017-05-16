a = int(input("Enter First Number (a): "))

b = int(input("Enter Second Number (b): "))

c = input('WHAT DO YOU WANT TO DO? ')

ev = eval(c)

print('''a = {}
b = {}
{} = {}'''.format(a, b, c, ev))
