def fib(n):
    if n<1:
       return None
    if n<3:
       return 1
    i=0   
    while i<=n:   
       return fib(n-1)+fib(n-2)  
       i+=1

for i in range(1,11):
    print("Fibonnaci series of ",i,fib(i))
