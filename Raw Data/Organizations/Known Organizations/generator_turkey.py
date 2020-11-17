filem = open("top_turkey.txt","r")

text = filem.readlines()

myList = []
count = 1
flag = False
for line in text:
    if flag:
        myList.append(line.strip())
        flag = False
    if(line.strip() == str(count)):
        count += 1
        flag = True

out = open("organization_turkey_top.txt","w")

for i in myList:
    out.write(i + "\n")
