# https://www.gencayyildiz.com/blog/ms-sql-server-ulke-sehir-ilce-semt-ve-mahalle-veritabani/
locationList = []
print("\tWorld Wide Locations Started")
locationDatabase = open("location_data_world.txt", "r")
text = locationDatabase.readlines()
for line in text:
    locationList.append(line.strip())

locationDatabase = open("countries.txt", "r")
text = locationDatabase.readlines()
for line in text:
    for i in range(3):
        index = line.find(",")
        line = line[index+1:]
    line = line[3:].strip()
    index = line.find(",")
    line = line[:index-1]
    # print(line)
    if(line not in locationList):
        locationList.append(line.capitalize().strip())

locationDatabase = open("location_data_world.txt", "w")

for i in locationList:
    locationDatabase.write(i + "\n")