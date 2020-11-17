# nameDatabase = open("Common_Surnames_Census_2000.csv","r")
nameDatabase = open("SSA_Names_DB.csv","r")

nameList = []

for line in nameDatabase:
    index = line.find(";")
    line = line[:index]
    # print(line)
    nameList.append(line)

nameFile = open("names_data_english.txt", "a")

for name in nameList:
    nameFile.write(name + "\n")