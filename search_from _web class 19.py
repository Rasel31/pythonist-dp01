import re, urllib

try:
    import urllib.request
except:
    pass

site = 'academy.denarycomputing google yahoo cnn'.split()

for s in site:

    print('Searcing: ', s)

    try:
        req = urllib.request.urlopen('http://'+s+'.com')

    except:
        req = urllib.request.urlopen('http://'+s+'.com')

    data = req.read()

    title = re.findall(r'<tittle>+.*</tittle>+', str(data), re.I)

    for t in title:

        print(t)
