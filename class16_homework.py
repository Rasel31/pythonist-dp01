mo = ''

while len(mo) != 11:

    mo = (input("Enter Your Mobile Number: "))

    if len(mo) == 11:

        if mo[0:3] == "017":

            print("You have Grameen Phone Mobile Operator")

        elif mo[0:3] == "018":

            print("You have Robi Mobile Operator")

        elif mo[0:3] == "016":

            print("You have Airtel Mobile Operator")

        elif mo[0:3] == "019":

            print("You have Banglalink Mobile Operator")

        elif mo[0:3] == "011":

            print("You have Citycell Mobile Operator")

        elif mo[0:3] == "015":

            print("You have Teletalk Mobile Operator")

        else:
            print("Invalid Operator!!!")

    else:

        print("Invalid Number!!! Try Again...")

