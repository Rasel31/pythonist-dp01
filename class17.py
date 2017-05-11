class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Hi {}, your age {}".format(name, age))

    def sleeping_time(self, hour):
        self.hour = hour
        print('{} Sleep = {}hr'.format(self.name, hour))

    def __str__(self):
        return 'Name : {}\nAge : {}\nSleep Time : {}hr'.format(self.name, self.age, self.hour)


#rasel = Human('Rasel', 22)
#rasel.sleeping_time(10)

#print(type(rasel))

class Student(Human):

    def __init__(self, name, age, sec, phn, email, university = 'Daffodil', dept = 'SWE'):
        self.name = name
        self.age = age
        self.dept = dept
        self.sec = sec
        self.phn = phn
        self.email = email
        self.university = university

    def __str__(self):
        return 'Name : {}\nAge : {}\nDept : {}\nSec : {}\nPhone : {}\nEmail : {}\nUniversity : {}'.format(self.name, self.age, self.dept, self.sec, self.phn, self.email, self.university)

rasel = Student('Rasel', 22, 'B', '01684768264', 'russel35-1170@diu.edu.bd',)
rasel.sleeping_time(6)

print(rasel)