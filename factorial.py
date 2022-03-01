def factorial_fun(n):
    if n<0:
       return None
    if n<2:
       return 1
    
    fact=1
    for i in range(2,n+1):
       fact*=i
    return fact
    
for i in range(1,11):
    print("Factorial of ",i,": ",factorial_fun(i))    