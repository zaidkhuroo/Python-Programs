 # input string
 
 
n="hey$"
n.split()
c=0
s='[@_!#$%^&*()<>?/\|}{~:]'  # special character set
for i in range(len(n)):
    # checking if any special character is present in given string or not
    if n[i] in s:
      c+=1   # if special character found then add 1 to the c
 
# if c value is greater than 0 then print no
# means special character is found in string     
if c:
    print("string is not accepted")
else:
    print("string accepted")
 
