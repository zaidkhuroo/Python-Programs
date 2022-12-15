


# List of numbers
list1 = [10, 20, 4, 45, 99]
 
# new_list is a set of list1
new_list = set(list1)
 
# Removing the largest element from temp list
new_list.remove(max(new_list))
 
# Elements in original list are not changed
# print(list1)
print(max(new_list))
print(new_list)