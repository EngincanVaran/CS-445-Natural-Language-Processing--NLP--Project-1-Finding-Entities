def readNames2CreateData():
    nameList = []
    nameDatabase = open("names_database_v1.txt", "r")
    for line in nameDatabase:
        index = 0
        for i in range(5):
            index = line.find("'", index+1)
        secondIndex = line.find("'",index+1)
        line = line[index+1:secondIndex]
        nameList.append(line)
    namesFile = open("names_data_turkish.txt","w")
    for name in nameList:
        namesFile.write(name + "\n")