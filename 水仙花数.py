for i in range(100,1000):
    a=i%10      #个位
    b=i//10%10  #十位
    c=i//100    #百位
    if a**3+b**3+c**3==i:
        print(i,end=' ')
