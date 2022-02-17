def animal_crackers(text):
  text=text.split()
  i=0
  
  for splittext in text:
     if i==0: 
       y=splittext[0]
       i+=1
     elif splittext[0]==y:
        return True
     else:
        return False

print(animal_crackers('Levelheaded Llama'))