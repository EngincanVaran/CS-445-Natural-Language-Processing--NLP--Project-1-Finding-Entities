filem = open("top.txt","r")

org = filem.readlines()

orgList = []

lineNumber = 1
for line in org:
    if(line != "\n"):
        orgList.append(line)

outFile = open("organization_top_companies.txt","w")

for i in range(len(orgList)):
    if i % 7 == 1:
        outFile.write(orgList[i].strip() + "\n")