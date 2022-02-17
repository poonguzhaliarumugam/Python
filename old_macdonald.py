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