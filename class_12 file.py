'''f = open("rasel.python", "a")
f.write("\nDenary Computing Academy")
f.close()

f = open("rasel.python", "r")
b = f.read()
f.close()

s = open("C:\\Users\\DOL\\Desktop\\rasel.python", "a")
s.write(b)
s.close()


with open ("rasel.python","r") as f:
    data = f.read()
    
with open ("C:\\Users\\DOL\\Desktop\\rasel.python", 'w') as f:
    f.write(data)
'''

#******************************************************************



with open ("C:\\Users\\Public\\Videos\\Sample Videos\\Wildlife.wmv", "rb") as f:
    
    video = f.read()

with open ('C:\\rkn\\video file\\Wildlife.video', "wb") as f:

    f.write(video)
