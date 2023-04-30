s = input().split(' ')
ls = []
for i in range(0, len(s)):
    if s[i] in s[i+1:]:
        if s[i] in ls:
            continue
        else:
            ls.append(s[i])
    else:
        None
for i in ls:
    print(i, end=' ')


