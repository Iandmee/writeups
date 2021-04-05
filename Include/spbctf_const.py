flag=[str(i) for i in "Flag{This_is_definetly_a_flag}"]
def kek():
    v0 = flag[5]
    flag[5] = flag[14]
    flag[14] = v0
    v1 = flag[20]
    flag[20] = flag[21]
    flag[21] = flag[7]
    flag[7] = v1
    v2 = flag[19]
    flag[19] = flag[20]
    result =v2
    flag[20] = v2
    return result
kek()
print(''.join(flag))