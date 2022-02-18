#Method1
from unicodedata import name


def old_macdonald(name):
  i=0
  namelist=[]
  for x in name:
    if i==0 or i==3:
       namelist.append(x.upper())
    else:
       namelist.append(x)
    i+=1   
  return ''.join(namelist)  
print(old_macdonald('macdonald'))

#Method2
def old_macdonald2(name):
  first_half=name[0:3]
  second_half=name[3:]
  name=first_half.capitalize()+second_half.capitalize()
  return name
print(old_macdonald2('macdonald'))  

#Method3
def old_macdonald3(name):
  first_letter=name[0]
  second_half=name[1:3]
  third_half=name[3:4]
  fourth_half=name[4:]
  name=first_letter.upper()+second_half+third_half.upper()+fourth_half
  return name
print(old_macdonald3("macdonald"))