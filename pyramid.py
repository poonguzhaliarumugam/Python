#to bulid a pyramid with blocks and to find the height of the pyramid
blocks = int(input("Enter the number of blocks: "))
total_block=0
next_block=0
height=0
for i in range(blocks):
   next_block+=1
   total_block+=next_block
   if total_block<=blocks:
      height+=1
      continue
   else: 
      break 

print("The height of the pyramid:", height)
