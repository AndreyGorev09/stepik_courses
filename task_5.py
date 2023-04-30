s = input().split(' ')
st = []

for i in range(0, len(s)):
    if len(s)!=1:
        if i == len(s)-1:
            st.append(int(s[i-1]) + int(s[0]))
        elif i == 0:
            st.append(int(s[-1]) + int(s[1]))
        else:
            st.append(int(s[i-1]) + int(s[i+1]))
    else:
        st.append(s[i])
for i in st:
    print(i, end=' ')
            