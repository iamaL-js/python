a,n = map(int,input().split())
s=0
for i in range(1,n):
    s+=a
    a+=a*10**i
print(s)