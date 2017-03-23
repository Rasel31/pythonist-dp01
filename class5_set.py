s = set()

s = {}

s = {1, 2, 3}

s.add(5)
print(s)
s.clear()
print(s)

even = {2, 4, 6, 8, 10}
odd = {1, 3, 5, 7, 9, 11}
prime = {2, 3 , 5, 7, 11}
fibonacci = {1, 1, 2, 3, 5, 8}

p_i_e = prime.intersection(even)

print(p_i_e)

o_i_f = odd.intersection(fibonacci)

print(o_i_f)

e_u_o = even.union(odd)

p_u_f = prime.union(fibonacci)

print(e_u_o.difference(p_u_f))

print(e_u_o - p_u_f)

