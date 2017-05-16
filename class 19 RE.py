import re

demo_str = '''python programming class
Today is our 18th class
my name is Rasel. Noyon vai is my senior.
3Jibon2 vai read in SWE dept'''

'''find_our = re.findall('[A-Z]{3}[a-z]{1,10}', demo_str)

for i in find_our:
    print(i)
    '''
'''
pattern = re.compile('[A-Z]{3}')  #SWE can be fixed

#pattern = re.compile('[CS]{1}[A-Z]{2}')

#pattern = re.compile('[CSW]{2}E')

find = re.sub(pattern, 'Software', demo_str)

print(find)
'''
demo = 'PYTHON'

str_demo = '''I am Python 3
I am the best Programming language      
in the world. Java, c also best
and popular programming language'''

#find Java,  c, Python    

find_python = re.match('Python', demo, re.I)

if find_python:

    print('Match Found: ', find_python.group())
else:
    print("No Match Found")

    

find_python = re.search('python', str_demo, re.I)

if find_python:
    for i in find_python.group():
        print(i)
    
else:
    print("No Match Found")
