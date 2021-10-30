def isLeap(year):
    judge = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
    return judge

def yearNumbers(judge):
    if judge:
        ret=366
    else:
        ret=365
    return ret

def monthNumbers(judge,month):
    ret=[31,28,31,30,31,30,31,31,30,31,30,31]
    if judge:
        ret[1]=29
    return int(ret[month])

year,month,day = map(int,input().split('.'))
sumYear=0
sumMonth=0
for i in range(2000,year):
    sumYear+=yearNumbers(isLeap(i))
else:
    for j in range(0, month-1):
        sumMonth += int(monthNumbers(isLeap(year), j))
sumDay=day
print(sumDay+sumMonth+sumYear)