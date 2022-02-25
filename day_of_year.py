def is_year_leap(year):
    if year%400==0:
       return True
def days_in_month(year, month):
    dom=[31,28,31,30,31,30,31,31,30,31,30,31]
    is_year_leap(year)
    if is_year_leap:
       dom[1]=29
       print(dom)
    i=0
    no_days=0
    while i<month:
       no_days+=dom[i]
       i+=1
    return no_days   
def day_of_year(year, month, day):
    result=days_in_month(year, month)
    cor_day=day+result
    print("corresponding day of the year: ",cor_day)
        
  
print(day_of_year(2000, 12, 31))
