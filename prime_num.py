def is_prime(num):
   i=2 
   while i<=num:
       if i<num:
           if num%i==0:
              return False
       elif num==i:
            if num%i==0:
               return True
       i+=1              
       
for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
