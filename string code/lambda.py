numbers=[1, 2, 3]
even=filter(lambda n:n%2==0,numbers)
odd=filter(lambda n:n%2==1,numbers)
print(list(even))
print(list(odd))