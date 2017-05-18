import re

str_demo = '''I am Python 3
              I am the best Programming language
              in the world. Java, c also best
              and popular programming language
              '''

# pattern = re.compile('[p]\w{4}[n] | [J]\w{2}[a] | [c]$')

find_python = re.search(r'[p][a-z]{4}[n]', str_demo, re.I)
find_java = re.search(r'[j][a-z]{2}[a]', str_demo, re.I)
find_c = re.search(r'[c]', str_demo, re.I)

if find_python:
    for i in find_python.group():
        print(i, end="")

print()

if find_java:
    for i in find_java.group():
        print(i, end="")

print()

if find_c:
    for i in find_c.group():
        print(i, end="")
