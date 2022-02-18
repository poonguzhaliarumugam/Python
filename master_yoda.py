def master_yoda(text):
  i=0
  templist=[]
  mylist=text.split()
  listlen=len(mylist) 
  while(i<listlen):
    i+=1
    templist.append(mylist[listlen-i])
    
  return " ".join(templist)

print (master_yoda('We are ready'))


       