from pwn import *
import string
io = connect("imaginary.ml",10069)
alph = string.ascii_letters+string.digits+'{}@#$%^&*()_+-!?./'
print(io.recvline())
r = io.recvline()
io.recvline()
for i in alph:
    io.sendline(i)
    io.recvline()
    character = io.recvline()[:-1]
    io.recvline()
    r =  r.replace(character,i.encode())
print(r.decode())