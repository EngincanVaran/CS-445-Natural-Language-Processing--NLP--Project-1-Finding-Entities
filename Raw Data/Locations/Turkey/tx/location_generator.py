print("\tTurkey Wide Locations (il) Started")

mFile = open("il.txt", "r")
# mFile = open("ilce.txt", "r")

text = mFile.readlines()

locationList = []

for line in text:
    line = line.strip()
    index = line.find(",")
    line = line[index+3:]
    index = line.find(",")
    line = line[:index-1]
    if(line not in locationList):
        locationList.append(line)

mFile = open("location_data_il.txt", "w")
# mFile = open("location_data_ilce.txt", "w")

for loc in locationList:
    mFile.write(loc + "\n")

# run this after
locationList = []
locationDatabase = open("location_data_ilce.txt", "r")
text = locationDatabase.readlines()
for line in text:
    locationList.append(line.strip())

locationDatabase = open("ilceler.txt","r")
text = locationDatabase.readlines()
for line in text:
    index = line.find(",")
    line = line[index+1:]
    index = line.find(",")
    line = line[index+4:]
    index = line.find(",")
    line = line[:index-1]
    if(line not in locationList and line != ""):
        locationList.append(line.upper().strip())
        print(line)

locationDatabase = open("location_data_ilce.txt","w")
for i in locationList:
    locationDatabase.write(i + "\n")