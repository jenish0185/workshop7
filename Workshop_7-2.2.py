f = open('GFG.txt', 'r')
content = f.readlines()
for line in content:
    for i in line:
        if i.isdigit() == True:
            a=i

print("The sume is:", a)