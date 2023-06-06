month = input("Enter month name :")
a=0
for i in month:
    if i == 'r':
        a += 1
if a > 0:
    print("True")
else:
    print("False")