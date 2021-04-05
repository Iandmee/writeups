s = "497 1207 1273 871 476 884 1615 475 2233 231 505 1919 190 2755 231 561"
a = [int(i) for i in s.split()]
for i in a:
    for j in range(1,10000):
        if i%j==0:
            print(str(j)+" ",end="")

    print("###############")