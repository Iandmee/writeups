import requests
def f_y(y: str)->float:
    r = s.post(url + 'fire', data={'x': '0', 'y': y})
    return float(r.text.split()[7][:-1])
def f_x_y(x:str,y:str):
    r = s.post(url + 'fire', data={'x': x, 'y': y})
    return r
url = "https://battleship.q.2021.ugractf.ru/cb9cd032264d2056/"
s = requests.Session()
while 1:
    r = s.post(url+'reset')
    print(r.text)
    dist = f_y(str(0))
    print(dist)
    a={}
    for i in range(1,round(dist)):
        temp = (dist*dist-i*i)**0.5
        if float(temp-int(temp))>0.99 or float(temp-int(temp))<0.01:
            a[round(temp)]=i
    print(a)
    for key,value in a.items():
        if key in a.values():
            print("okey")
            ans = f_x_y(str(value),str(key)).text
            if "ugra" in ans:
                print(ans)
                exit(0)
            ans = f_x_y(str(value),str(-key)).text
            if "ugra" in ans:
                print(ans)
                exit(0)
            ans = f_x_y(str(-value), str(key)).text
            if "ugra" in ans:
                print(ans)
                exit(0)
            ans = f_x_y(str(-value), str(-key)).text
            if "ugra" in ans:
                print(ans)
                exit(0)