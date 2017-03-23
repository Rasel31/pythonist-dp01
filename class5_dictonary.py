'''
d = dict()

d['name'] = "RAsel"
d['Name'] = 'Khyan'
d[1] = 'Khyan'

print(d)

d2 = dict(first = 'Rasel',      # dict is constructor
      sccond = "Khan")

d = {'Name' : 'Rasel',
     'Phone' : '01740399036',
     'email' : "noyonmassive@gmail.com",
     'location': 'DIU'}

d['section'] = 'B'

print(d.get('email'))
      
'''



info = dict(name = "Rasel",
            phone = "01684768264",
            email = "russel35-1170@diu.edu.bd",
            Section = "B",
            Batch = "17",
            Dept = "SWE",)

print(info.get('email'))

print(info.keys())

print(info.values())

info1 = dict(location = 'DIU',
             Address = 'Dhaka')

info.update(info1)
print(info)

info['new dict'] = {'n' : 'Name', "E" : "Email"}
print(info)
