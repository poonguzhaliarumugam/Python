#Collatz's hypothesis
c0=int(input("Enter positive non-zero no: "))
step_ct=0
while c0!=1:
   if c0%2==0:
      c0/=2
   else: 
      c0=3*c0+1
   step_ct+=1
   c0=int(c0)
   print(c0)
print("steps = ",step_ct)   