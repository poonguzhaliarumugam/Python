def fib(n):
    if n<1:
       return None
    if n<3:
       return 1
       
    num1=1
    num2=1
    fib=0
    for i in range(3,n+1):
        fib=num1+num2
        num1,num2=num2,fib
    return fib
for i in range(1,100):    
    print("fib of ",i,": ",fib(i))    
        