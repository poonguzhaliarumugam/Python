#bubble sort
my_list=[8,10,6,2,4]
swapped=True
while swapped:
    swapped=False
    for i in range(len(my_list)-1):
       if (my_list[i] > my_list[i+1]):
         my_list[i],my_list[i+1]=my_list[i+1],my_list[i]
         swapped = True
print(my_list)         