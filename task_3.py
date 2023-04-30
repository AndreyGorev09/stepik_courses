# 'aaaabbсaa' преобразуется в 'a4b2с1a2'
s = 'abс'
d = 1
l = len(s)-1
t = ''
if s != '':
    for i in range(0, l):
        if s[i] == s[i+1]:
            d+=1
        elif s[i] != s[i+1]:
            t = t+s[i]+str(d)
            d = 1
    for j in range(l, l+1):
        if s[-1] == s[-2]:
            t = t+s[j]+str(d)
        elif s[-1] != s[-2]:
            t = t+s[j]+str(d)
            d = 1
    print(t)






