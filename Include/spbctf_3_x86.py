s = "_A_m_aFneSuyn_w_IypvSr_ahIEwp_gitrnMhaetevT_so!"
a=[i for i in s]
for i in range(1,10):
    for j in range(len(s)//(i+1)*(i+1)-1,-1,-1*(i+1)):
        if j-i<0:
            break
        t = a[j]
        a[j] = a[j-i]
        a[j-i] = t
for i in a:
    print(i,end="")