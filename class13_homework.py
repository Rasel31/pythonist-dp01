import os

import time

if os.path.exists(r"C:\New folder\class 13 homework file copy.py"):
    pass
else:
    with open (r"C:\rkn\python class\class13_homework.py", "r") as f:                           #r = regular expression
        file = f.read()

    with open (r"C:\New folder\class 13 homework file copy.py", "w") as f:
        f.write(file)

print(os.getcwd())

os.chdir("C:\\rkn\\13 homework")

while True:
    i = 0

    while True:

        if i == 10:

            break

        if os.path.exists("Rasel" + str(i+1)):

            pass

        else:

            os.mkdir("Rasel " + str(i+1))
            time.sleep(2)

        i += 1

    time.sleep(5)

    for i in os.listdir():

        os.rmdir(i)

        time.sleep(2)


