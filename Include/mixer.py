s = "abcdefghijklmnopqrstuvwxyz_{}0123456789"
s1 = "wmf9slha2r}v7te_13kby8ug4c{oz5j0idp6nqx"
s2 = "k_mfblobadb{udp{idp4{iaxz"
for i in s2:
    for j in range(len(s1)):
        if s1[j]==i:
            print(s[j],end="")
