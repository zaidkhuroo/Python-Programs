myList = [5, 7, 8, 3, 4, 2, 9]

c = 0
while c < len(myList):
    element = myList[c]
    if element % 2 == 0:
        print('even')
    else:
        print('odd') 
    c+= 1
