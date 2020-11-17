filem = open("banks.txt","r")

banks = filem.readlines()
bankList = []

for line in banks:
    index = line.find("(")
    line = line[:index-1]
    bankList.append(line)
    # print(line)

resultFile = open("organization_turkish_banks.txt","w")

for bank in bankList:
    resultFile.write(bank + "\n")