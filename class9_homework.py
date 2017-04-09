def my_len(m):
    flag = 0
    for i in m:

        a = m[i]
        flag += 1
        
    return flag


a = input("Enter anything: ")

print(my_len(a))
