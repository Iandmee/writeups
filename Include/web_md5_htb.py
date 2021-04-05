from requests import *
import hashlib
url = 'http://178.62.0.100:31374'
s = Session()
while 1:
    r = s.get(url)
    ind = r.text.find('</h3>')
    print(r.text)
    if ind!=-1:
        tec=ind
        while r.text[tec]!='>':
            tec-=1
        string = r.text[tec+1:ind]
        print(string)
        hash = hashlib.md5(string.encode())
        print(str(hash.hexdigest()))
        s.post(url,data={"hash":str(hash.hexdigest())})
    else:
        print(r.text)
