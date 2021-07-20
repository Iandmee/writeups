from pwn import *
import string
import sys
HOST = sys.argv[1]

io = remote(HOST, 6789)
io.sendline("mjtezmjtezmjtez")
print(io.recvuntil('That\'s it!',timeout=2).decode())