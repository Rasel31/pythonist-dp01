import sys

import getpass

print(sys.version)

#print(dir(sys))

sys.stderr.write("Rasel with stderr\n")
sys.stdout.write('Khan with stdout\n')

#for i in dir(sys):
  #  print(i)

print(sys.getprofile())

print(getpass.getuser())
