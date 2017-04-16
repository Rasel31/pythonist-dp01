def C_to_F(c):
    return c * (9 / 5) + 32


def C_to_K(c):
    return c + 273.15


C = eval(input("Enter Temperature in °C: "))

F = C_to_F(C)

print('\n' + str(C)+"°C = {0:.1f}°F".format(F))

print()

K = C_to_K(C)

print('\n' + str(C)+ "°C = {0:.2f}°K".format(K))
