a,b,c = map(float,input().split())
p=a+b+c
s=(p/2*(p/2-a)*(p/2-b)*(p/2-c))**0.5
judge=a**2+b**2==c**2 or a**2+c**2==b**2 or a**2==b**2+c**2
print(f"{int(p)} {round(s,5)} {judge}")


