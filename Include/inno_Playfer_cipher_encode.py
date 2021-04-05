a=[ ['c','t','f','a','b',],['d','e','g','h','i'],['k','l','m','n','o'],['p','q','r','s','u'],['v','w','x','y','z']]
s = "Innopolis Open Information Security"
s = (s).lower()
temp = [i for i in s.split()]
s = ''.join(temp)
ans=""
print(s)
for i in range(0,len(s),2):
    first_i=-1
    first_j=-1
    second_i=-1
    second_j=-1
    for j in range(5):
        for z in range(5):
            if a[j][z]==s[i]:
                first_i=j
                first_j=z
            if a[j][z]==s[i+1]:
                second_i=j
                second_j=z
    if first_i==second_i:
        ans+=a[first_i][(first_j+1)%5]
        ans+=a[second_i][(second_j+1)%5]
    elif second_j==first_j:
        ans += a[(first_i+1)%5][first_j]
        ans += a[(second_i+1)%5][second_j]
    else:
        ans+=a[first_i][second_j]
        ans+=a[second_i][first_j]
print(ans.upper())