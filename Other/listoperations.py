# program to find 2nd largest elemnt in a list
height = [] #declaring empty list
length = input("Enter Length for list: ") #size for height list

#taking inputs into height of type list
for i in range(int(length)):
    height.append(int(input(f"Enter elements for [{i}]")))


print(height)
height.sort()
print(height)

#code for 2nd largest element
secLarElement = len(height) - 2
print("Second Largest Element In The List Is ",height[secLarElement])

#OR by using negative indexing
secLargestElement = height[-2]
print("Sec lar element: ",secLargestElement) 