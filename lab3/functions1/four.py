def isprime(n):
    cnt=0
    if n<2:
        return False
    for i in range(2, n):
        if n%i==0:
            cnt=+1
    if cnt>0:
        return False
    else:
        return True
a=[2,3,4,5,6,7,8]
for i in a:
    print(f"{i}: {isprime(i)}")
