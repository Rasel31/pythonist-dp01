import calendar
import datetime
import urllib.request

now = datetime.datetime.now()

time = datetime.time(12, 4, 6)
date = datetime.date(1996, 3, 31)

print(time)
print(date)
print(now)

#print(calendar.isleap(2017))
#print(calendar.calendar(2018))

url = 'http://4.bp.blogspot.com/-SCLLWg2D0jg/VYEPRtKlpCI/AAAAAAAAB_I/7JlOV6LmXUk/s1600/DIU-Logo.png'

urllib.request.urlretrieve(url, 'daffodil.png')
