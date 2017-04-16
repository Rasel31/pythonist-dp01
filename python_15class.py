def tk_to_dollar(tk, dollar=78):
    return tk / dollar


tk = eval(input("Enter amount in Taka: "))

TD = tk_to_dollar(tk)

print('\n' + str(tk), "Taka = {0:.2f} $".format(TD))

print()


def dollar_to_tk(dollar, tk=78):
    return dollar * tk


dollar = eval(input("Enter amount in $: "))

DT = dollar_to_tk(dollar)

print('\n' + str(dollar) ,"$ = {0:.2f} BDT".format(DT))
