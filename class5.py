                    # CLASS 4 REVIEW
'''
l_even = [2,4,6,8]
l_odd = [1,3,5,7]

new_list = []

new_list = l_even + l_odd

new_list.reverse()

print(new_list)

new_list.sort()

print(new_list)

l_even.append(10)

l_odd.append(9)

print("Even =",l_even)
print("Odd =",l_odd)

l_odd.extend([11,13])

print("Odd =",l_odd)

new_list.insert(4, ['A', 'B', 'C'])

print(new_list)
'''
new_list =[1, 2, 3, 4, ['A', 'B', 'C'], 10]

print(new_list[4][1])

print(new_list.index(2))

print(new_list[4].index('A'))

new_list.clear()

print(new_list)
