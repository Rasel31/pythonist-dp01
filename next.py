#import program

#print(__name__)
#p.main()
#print(p.__name__)
#p.others()

#program.main()
#program.others()

class first:
    def name(a):
        print("f")

class second(first):

    def name():
        print('d')

    name()

    first.name("dsd")
