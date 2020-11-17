print("\tWorld Wide Locations Started")
locationDatabase = open("worldcities.csv", "r")
locations = locationDatabase.readline()
# print(locations)
locations = locationDatabase.readlines()
locationList = []
for line in locations:
    line = line.strip()
    index = line.find(",")
    city = line[1:index-1]
    if(city not in locationList):
        locationList.append(city)
    # print(city)
    
    line = line[index+1:]
    index = line.find(",")
    city = line[1:index-1]
    # print(city)
    if(city not in locationList):
        locationList.append(city)

    for i in range(2):
        index = line.find(",", index+1)
    line = line[index+2:]
    index = line.find(",", 0)
    country = line[:index-1]
    # print(country)
    if(country not in locationList):
        locationList.append(country)

mFile = open("location_data_world.txt","w")

for loc in locationList:
    mFile.write(loc + "\n")