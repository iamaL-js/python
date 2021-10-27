n = int(input () )
if n==2:
    print("True")
else:
    for i in range(2,n):
        if n%i==0:
            print("False")
            break
        else:
            print("True")
