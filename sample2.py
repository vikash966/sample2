
a=[5,6,7,8]
b=0
for i in range(len(a)):
    for j in range(1,len(a)):
        if a[i]<a[j]:
            b=a[j]
        else:
            b=a[i]


print(b)
