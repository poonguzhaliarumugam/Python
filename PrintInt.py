#to print integers 1to100, print fizz for multiples of 3 buzz for 5 fizzbuzz for 3 and 5
intlist=[x for x in range(101)]
print(intlist)
for num in intlist:
 if num%3==0:
  print(num,'fuzz')
 elif num%5==0:
  print(num,'buzz')
 if num%3==0 and num%5==0:
  print (num,'fuzzbuzz')
