#remove duplicates
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9,10,67,100,9,6]
temp_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9,10,67,100,9,6]
new_list=[]

for num in my_list:
    if num in temp_list:
       if num not in new_list:    
          new_list.append(num) 
   
my_list=new_list[:]#[:]copies entire list
  
print("The list with unique elements only:")
print(my_list)
