def liters_100km_to_miles_gallon(liters):
    one_km=(1/1.609)#km to miles
    one_ltr=(1/3.785411784)#liters to gallon
    gal=one_ltr*liters#finding no of gallons for the liters parameter
    milles=one_km*100#converting 100km to miles
    mpg=milles/gal
    return mpg
    
def miles_gallon_to_liters_100km(miles):
    miles_to_km=1.609*miles#converting miles to km
    
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))


