
# To find compound interest 

p = float(input('Enter principle amount: '))  
t = float(input('Enter time: '))  
r = float(input('Enter rate: ')) 

# calculates the compound interest
a=p*(1+(r/100))**t  # formula for calculating amount
ci=a-p  # compound interest = amount - principal amount

# printing compound interest value
print('The compound interest is', ci)

#To find simple interest
si = (p * t * r)/100 
print('The Simple Interest is', si)
