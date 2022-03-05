def fact(n):
    if n<1:
       return None
    if n<2:
        return 1
    i=0
    result=0
    while i<=n:
        result=n*fact(n-1)
        i+=1 
    return result

for i in range(1,11):
    print("Factorial of ",i,fact(i))                   