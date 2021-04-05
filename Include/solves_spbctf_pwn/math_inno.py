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
exe = context.binary = ELF('./allocator')

if exe.bits == 32:
    lindbg = "/root/linux_server"
else:
    lindbg = "/root/linux_server64"


# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141
host = args.HOST or 'ppc4.olymp.hackforces.com'
port = int(args.PORT or 9093)
    
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
print(io.recvuntil(b'\n').decode())
for i in range(53):
    print(io.recvuntil(b'\n').decode())
    k = io.recvuntil(b'\n').decode()
    print(k)
    a = []
    tec=""
    flag = 0
    for j in k:
        try:
            int(j)
            tec+=j
        except:
            if flag ==1 and tec!="":
                tec = "-"+tec
            a.append(tec)
            tec=""
            flag =0
        if j == '-':
            flag =1
    math = []
    for i in a:
        if i !="":
            math.append(int(i))
    print(math)
    ans =""
    if math[1]**2-4*math[0]*math[2]<0:
        ans+="0:"
    else:
        ans+="1:"
    if math[1]**2-4*math[0]*math[2]<0:
        ans+="0:"
    if math[1]**2-4*math[0]*math[2]==0:
        ans+="1:"
    if math[1]**2-4*math[0]*math[2]>0:
        ans+="2:"
    d = math[1]**2-4*math[0]*math[2]
    if d>=0 and sqrt(d) - int(sqrt(d))==0.0 and math[0]!=0:
        if (-math[1]+sqrt(d))/(2*math[0]) == int((-math[1]+sqrt(d))/(2*math[0])) and (-math[1]-sqrt(d))/(2*math[0]) == int((-math[1]-sqrt(d))/(2*math[0])):
            ans+="2"
        elif (-math[1]+sqrt(d))/(2*math[0]) == int((-math[1]+sqrt(d))/(2*math[0])) or (-math[1]-sqrt(d))/(2*math[0]) == int((-math[1]-sqrt(d))/(2*math[0])):
            ans+="1"
        else:
            ans+="0"
    else:
        if math[0]==0:
            if math[2]/math[1]-int(math[2]/math[1]) == 0:
                ans+="1"
            else:
                ans+="0"
        else:
            ans+="0"
    print(ans)
    io.sendline(ans)
io.interactive()