import string
import os
from time import sleep
s = string.ascii_letters
for i in s:
    for j in s:
        print(f"echo {i} {j}")
        os.system(f"./task2.out {i} {j} >> aaaaa")