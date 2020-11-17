from timeit import default_timer as timer
import re
import sys

inputFileName = ""

if __name__ == "__main__":
    if(len(sys.argv)>1):
        inputFileName = sys.argv[1]
        # print(inputFileName)

# ***************** #
# read TXT database #
# ***************** #
def readNameDatabase(includeTurkish = True, includeEnglish = False):
    nameList = []
    # TURKISH NAMES
    # data retrieved from https://gist.github.com/ismailbaskin/1325813
    if(includeTurkish):
        # print("\tTurkish Names Started")
        nameFile = open("Databases/names_data_turkish.txt","r")
        for line in nameFile:
            if len(line)>2:
                nameList.append(line.strip())
        # print("\t\tTurkish Names Ended -> " + str(len(nameList)) +" entries.")
    
    # ENGLISH NAMES
    # data retrieved from: https://data.world/len/us-first-names-database
    if(includeEnglish):
        # oldLen = len(nameList)
        # print("\tEnglish Names Started")
        nameFile = open("Databases/names_data_english.txt","r")
        for line in nameFile:
            if len(line)>2:
                nameList.append(line.strip())
        # print("\t\tEnglish Names Ended -> " + str(len(nameList) - oldLen) +" entries.")
    
    return nameList

def readLocationsDatabase(includeWorldEnglish = True, includeWorldTurkish = True , includeTurkeyDetailed = True):
    locationList = []
    # WORLD-WIDE 
    # data retrieved from https://simplemaps.com/data/world-cities 
    if(includeWorldEnglish):
        # print("\tWorld Wide Locations Started")
        locationDatabase = open("Databases/location_data_world.txt", "r")
        text = locationDatabase.readlines()
        for line in text:
            locationList.append(line.strip())
        # print("\t\tWorld Wide Locations Ended -> " + str(len(locationList)) +" entries.")
    
    if(includeWorldTurkish):
        # print("\tWorld Wide Locations -Turkish- Started")
        locationDatabase = open("Databases/location_data_world_turkish.txt", "r")
        text = locationDatabase.readlines()
        for line in text:
            locationList.append(line.strip())
        # print("\t\tWorld Wide Locations -Turkish- Ended -> " + str(len(locationList)) +" entries.")
    
    # TURKEY-WIDE-DETAILED - İl
    # data retrieved from https://github.com/life/il-ilce-mahalle-sokak-cadde-sql
    # data retrieved from https://www.gencayyildiz.com/blog/ms-sql-server-ulke-sehir-ilce-semt-ve-mahalle-veritabani/
    if(includeTurkeyDetailed):
        # oldLen = len(locationList)
        # print("\tTurkey Wide Locations (il) Started")
        locationDatabase = open("Databases/location_data_il.txt", "r")
        text = locationDatabase.readlines()
        for line in text:
            locationList.append(line.strip())
        # print("\t\tTurkey Wide Locations (il) Ended -> " + str(len(locationList)-oldLen) +" entries.")

        # TURKEY-WIDE-DETAILED - İlçe
        # data retrieved from https://github.com/life/il-ilce-mahalle-sokak-cadde-sql
        # data retrieved from https://www.gencayyildiz.com/blog/ms-sql-server-ulke-sehir-ilce-semt-ve-mahalle-veritabani/
        # oldLen = len(locationList)
        # print("\tTurkey Wide Locations (ilçe) Started")
        locationDatabase = open("Databases/location_data_ilce.txt", "r")
        text = locationDatabase.readlines()
        for line in text:
            locationList.append(line.strip())
        # print("\t\tTurkey Wide Locations (ilce) Ended -> " + str(len(locationList)-oldLen) +" entries.")

    return locationList

def readOrganizations():
    orgList = []

    # retrieved from: https://ipfs.io/ipfs/QmR1gzPYUwxEUWHbeRggZzfYy5Fxsd8Qc7hXUUnJQwxrZq/wiki/Türkiye%27deki_bankalar_listesi.html
    organizationDatabase = open("Databases/organization_turkish_banks.txt", "r")
    text = organizationDatabase.readlines()
    for line in text:
        orgList.append(line.upper().strip())
    
    # retrieved from: https://www.forbes.com/global2000/#3a6123fb335d
    organizationDatabase = open("Databases/organization_top_companies.txt", "r")
    text = organizationDatabase.readlines()
    for line in text:
        orgList.append(line.upper().strip())

    # retrieved from: https://www.ab.gov.tr/_2926.html
    organizationDatabase = open("Databases/organization_turkish_kurum.txt", "r")
    text = organizationDatabase.readlines()
    for line in text:
        if line != "\n":
            orgList.append(line.upper().strip())
    
    # retrieved from: https://www.fortuneturkey.com/fortune500
    organizationDatabase = open("Databases/organization_turkey_top.txt", "r")
    text = organizationDatabase.readlines()
    for line in text:
        orgList.append(line.strip())

    manuelAcronymList = [
        "THY",
        "TBMM",
        "TÜPRAŞ",
        "TDK",
        "TTK",
    ]

    orgList += manuelAcronymList

    return orgList

def readDatabases(  isPrinted = False,
                    includeEnglishNames = True, includeTurkishNames = True,
                    includeWorldEnglishLocation = True, includeWorldTurkishLocation = True, includeTurkeyDetailedLocation = True):
    database_Organizations = []
    if isPrinted:
        print("*"*75)
        start = timer()
        print("Names:")
        database_Person = readNameDatabase(includeTurkish=includeTurkishNames, includeEnglish=includeEnglishNames)
        end = timer()
        print("Total " + str(len(database_Person)) + " entries in " + str(end-start) + " seconds.")

        print("*"*75)

        start = timer()
        print("Locations:")
        database_Location = readLocationsDatabase(includeWorldEnglish=includeWorldEnglishLocation, includeWorldTurkish=includeWorldTurkishLocation, includeTurkeyDetailed=includeTurkeyDetailedLocation)
        end = timer()
        print("Total " + str(len(database_Location)) + " entries in " + str(end-start) + " seconds.")

        database_Organizations = readOrganizations()
    else:
        database_Person = readNameDatabase(includeTurkish=includeTurkishNames, includeEnglish=includeEnglishNames)
        database_Location = readLocationsDatabase(includeWorldEnglish=includeWorldEnglishLocation, includeWorldTurkish=includeWorldTurkishLocation, includeTurkeyDetailed=includeTurkeyDetailedLocation)
        database_Organizations = readOrganizations()

    return database_Person, database_Location, database_Organizations

# *************** #
# *************** #


# *************** #
# manual datasets #
# *************** #
# retrieved from: https://yeniokul.net/4098/akademik-unvanlar-hangileridir-siralamasi-ve-kisaltmalari-nasil-yazilir-akademik-gorev-ve-unvanlarin-ingilizce-karsiliklari-nelerdir
unvanPrefixes = [
    r'Uz.',
    r'Öğr. Pl.',
    r'Çev.',
    r'Okt.',
    r'Öğr. Gör.',
    r'Öğr. Ü.',
    r'Arş. Gör.',
    r'Arş. Gör. Dr.',
    r'Yrd. Doç.',
    r'Yrd. Doç. Dr.',
    r'Dr. Öğr.',
    r'Doç. Dr.',
    r'Doç.',
    r'Yrd. Doç.',
    r'Yrd. Doç. Dr.',
    r'Prof.',
    r'Prof. Dr.',
    r'Ord. Prof. Dr.',
    r'Dr.',
    # self generated
    r'Sayın',
    r'Sevgili',
    r'Kral',
    r'Kraliçe',
    r'Prens',
    r'Prenses',
    r'Rahip',
    r'Hacı',
    r'Muhtar',
    r'Başkan',
    r'Lider',
    r'Belediye Başkan',
    r'Vali',
    r'Cumhurbaşkanı',
    r'Bakan',
]

suffixes = [
    r'Bey',
    r'Hanım',
    r'Abi',
    r'Abla',
    r'Amca',
    r'Teyze',
    r'Dede',
    r'Dayı',
    r'Hoca',
    r'Öğretmen',
]

# Belirli bir tarih bildiren ay ve gün adları büyük harfle başlar
monthsUpperCase = [
    r"Ocak",
    r"Şubat",
    r"Mart",
    r"Nisan",
    r"Mayıs",
    r"Haziran",
    r"Temmuz",
    r"Ağustos",
    r"Eylül",
    r"Ekim",
    r"Kasım",
    r"Aralık",
]

months = [
    r"[Oo]cak",
    r"[Şş]ubat",
    r"[Mm]art",
    r"[Nn]isan",
    r"[Mm]ayıs",
    r"[Hh]aziran",
    r"[Tt]emmuz",
    r"[Aa]ğustos",
    r"[Ee]ylül",
    r"[Ee]kim",
    r"[Kk]asım",
    r"[Aa]ralık",
    r'[İi]lkbahar',
    r'[Ss]onbahar',
    r'[Kk]ış',
    r'[Yy]az',
    r'[Gg]üz',
    r'[Bb]ahar',
]

days = [
    r"[Pp]azar\w*",
    r"[Ss]alı\w*",
    r"[Çç]arşamba\w*",
    r"[Pp]erşembe\w*",
    r"[Cc]uma\w*",
]

locationSuffixes = [
    r'İlçe',
    r'İl',
    # r'[Şş]ehir',
    # r'[Şş]ehri',
    r'Köy',
    r'Kasaba',
    r'Belde',
    r'Belediye',
    r'Sokak',
    r'Mahalle',
    r'Park',
    r'Cadde',
    r'Bulvar',
    r'Otoyol',
    r'Otoban',
    r'Yanyol',
    r'Dağ',
    r'Köprü',
    r'Saray',
    r'Kale',
    r'Mezarlı[kğ]',
]

organiationSuffixes = [
    r'A.?Ş.?',
    r'L.?T.?D.?',
    r'T.?A.?Ş.?',
    r'Holding',
    r'Üniversite',
    r'Kurum',
    r'Kuruluş',
    r'Vakıf',
    r'Federasyon',
    r'Enstitü',
    r'Banka',
    r'Okul',
    r'Kolej',
    r'Lise',
    r'İlkokul',
    r'Hastane',
    r'Anaokulu',
    r'Eczane',
    r'Site',
    r'Vakfı',
    r'Takım',
]

# *************** #
# *************** #
# *************** #

# this function put the result into deserved format
# isPrinted is for the CSV file
def printFormat(lineNumber, tip, out, isPrinted = False):
    print("Line " + str(lineNumber) + ": " + tip + " " + out)
    if isPrinted:
        result_file.write("{},{},{}\n".format(lineNumber, tip, out))

def findNames(lineNumber, line):
    tip = "PERSON"
    going2print = []

    if(re.search(r'[A-ZÇĞİÖŞÜ]\w+',line)):
        if(re.search(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s+[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]*', line)):
            if re.search(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s+[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]*(?:\s+[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]*){1,4}',line):
                result = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s+[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]*(?:\s+[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]*){1,4}',line)
                for out in result:
                    if out.split()[0] in database_Person and out.split()[0] not in database_Location and out.split()[0] not in unvanPrefixes:
                        going2print.append(out)
            else:
                result = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s+[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]*', line)
                for out in result:
                    if out in database_Person and out not in database_Location:
                    # printFormat(lineNumber, tip, out)
                        going2print.append(out)
                    elif out.split()[0] in database_Person and out.split()[0] not in database_Location and out.split()[0] not in unvanPrefixes and out.split()[1] not in suffixes and out.split()[1] not in locationSuffixes:
                        going2print.append(out)
        else:
            result = re.findall(r'[A-ZÇĞİÖŞÜ]\w+',line)
            for out in result:
                if out in database_Person and out not in database_Location and out not in unvanPrefixes:
                    # printFormat(lineNumber, tip, out)
                    going2print.append(out)        


    for unvan in unvanPrefixes:
        flag = re.search(r'(?<='+ unvan + r')\w*\s+[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s+[A-ZÇĞİÖŞÜ][a-zçğıöşü]*', line)
        if(flag):
            result = re.findall(r'(?<='+ unvan + r')\w*\s+[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s+[A-ZÇĞİÖŞÜ][a-zçğıöşü]*',line)
            for out in result:
                if(out.strip()+"." not in unvanPrefixes):
                    # printFormat(lineNumber,tip, out)
                    going2print.append(out.strip())
        else:
            result = re.findall(r'(?<='+ unvan + r')\w*\s+[A-ZÇĞİÖŞÜ][a-zçğıöşü]*',line)
            # print(result, unvan)
            for out in result:
                if(out.strip()+"." not in unvanPrefixes):
                    # printFormat(lineNumber,tip, out)
                    going2print.append(out.split()[-1])

    for suf in suffixes:
        result = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s+' + suf + r'\w*',line)
        for out in result:
            index = out.find(suf)
            out = out[:index]
            going2print.append(out)
    
    # finished the line print now
    for out in set(going2print):
        printFormat(lineNumber, tip, out)
        
def findLocations(lineNumber, line):
    tip = "LOCATION"
    going2print = []

    if(re.search(r'[A-ZÇĞİÖŞÜ]\w+',line)):
        if(re.search(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s+[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]*', line)):
            result = re.findall(r'(?:[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]*\s+){1,4}[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]*', line)
            for out in result:
                if out.strip() in database_Location:
                    going2print.append(out.strip())
        else:
            result = re.findall(r'[A-ZÇĞİÖŞÜ]\w+\s*',line)
            for out in result:
                if out.capitalize().strip() in database_Location:
                    going2print.append(out.strip())

    result = re.findall(r'[A-ZÇĞİÖŞÜ]\w+\s*',line)
    for out in result:
        if out.capitalize().strip() in database_Location:
            going2print.append(out.strip())
    
    result = re.findall(r'[A-ZÇĞİÖŞÜ]+\s*',line)
    for out in result:
        if out.strip() in database_Location:
            going2print.append(out.strip())

    for locsuf in locationSuffixes:
        result = re.findall(r'[A-ZÇĞİÖŞÜ]\w+\s*' + locsuf + r'\w*\s*',line)
        for out in result:
            # out = out.split()[0]
            going2print.append(out)


    # finished the line print now
    for out in set(going2print):
        printFormat(lineNumber, tip, out)

def findOrganizations(lineNumber, line):
    tip = "ORGANIZATION"
    going2print = []

    if(re.search(r'[A-ZÇĞİÖŞÜ]\w+',line)):
        if(re.search(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s+[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]*', line)):
            result = re.findall(r'(?:[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]*\s+){1,8}[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]*', line)
            for out in result:
                if out.upper().strip() in database_Organizations:
                    going2print.append(out.strip())
        else:
            result = re.findall(r'[A-ZÇĞİÖŞÜ]\w+',line)
            for out in result:
                if out.upper().strip() in database_Organizations:
                    going2print.append(out.strip())


    for suffix in organiationSuffixes:
        if(re.search(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s+' + suffix + r'\w*',line)):
            if(re.search(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s+[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s+' + suffix + r'\w*',line)):
                result = re.findall(r'(?:[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]*\s+){1,8}[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s+' + suffix + r'\w*',line)
                for out in result:
                    going2print.append(out)
            else:
                result = re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s+' + suffix + r'\w*',line)
                for out in result:
                    going2print.append(out)


    # finished the line print now
    for out in set(going2print):
        printFormat(lineNumber, tip, out)

def findTimeandDate(lineNumber, line):
    tip = "TIME"
    going2print = []

    # General
    result = re.findall(r'\d{1,2}[-,:/]\d{1,2}[-,:/]\d{2,4}',line)
    for out in result:
        going2print.append(out)
    
    # General time (clock)  --> XX:XX
    result = re.findall(r'\d{1,2}[:.]\d{1,2}',line)
    for out in result:
        going2print.append(out)

    # General time (clock)  --> XX AM PM
    result = re.findall(r'\d{1,2}\s*[AP][M]', line)
    for out in result:
        going2print.append(out)

    #finding days           --> DAY_NAME
    for day in days:
        result = re.findall(day,line)
        for out in result:
            # printFormat(lineNumber, tip, out)
            going2print.append(out)
    
    # finding months        --> MONTH_NAME
    for month in months:
        result = re.findall(month,line)
        for out in result:
            # printFormat(lineNumber, tip, out)
            going2print.append(out)
    
    # finding months & years--> MONTH_NAME XXXX
    for month in months:
        result = re.findall(month+r'\s+\d{4}\s*',line)
        for out in result:
            # printFormat(lineNumber, tip, out)
            going2print.append(out)

    # finding months        --> DD MONTH_NAME YYYY
    for month in monthsUpperCase:
        result = re.findall( r'\d{1,2} ' + month + r' \d{4}',line)
        for out in result:
            # printFormat(lineNumber, tip, out)
            going2print.append(out)

    # finding months        --> DD MONTH_NAME'XX
    for month in monthsUpperCase:
        result = re.findall( r'\d{1,2} ' + month + r'\'?\w*',line)
        for out in result:
            # printFormat(lineNumber, tip, out)
            going2print.append(out)

    # finding years         --> YYYY
    result = re.findall(r'\d{4}\'?\w+', line)
    for out in result:
        # printFormat(lineNumber, tip, out)
        going2print.append(out)

    # finding years         --> YYYY yıl
    result = re.findall(r'\d{4}(?=\s+yıl\w+)',line)
    for out in result:
        # printFormat(lineNumber, tip, out)
        going2print.append(out)
    
    # finding years         --> YY. yüzyıl
    result = re.findall(r'\d{1,2}\. [Yy]üzyıl\w*',line)
    for out in result:
        # printFormat(lineNumber, tip, out)
        going2print.append(out)
    
    # finding years         --> XXXX-XXXX
    result = re.findall(r'\d{4}[-/]\d{4}', line)
    for out in result:
        # printFormat(lineNumber, tip, out)
        going2print.append(out)
    
    # finding years         --> XXXX
    result = re.findall(r'\d{4}', line)
    for out in result:
        # printFormat(lineNumber, tip, out)
        going2print.append(out)
    
    # finding years         --> MÖ X...
    result = re.findall(r'MÖ \d+', line)
    for out in result:
        # printFormat(lineNumber, tip, out)
        going2print.append(out)
    
    # finished the line print now
    for out in set(going2print):
        printFormat(lineNumber, tip, out)

def findAll(S, includeNames = True, includeLocations = True, includeOrganizations = True, includeTimeandDate = True):
    count = 0
    if includeNames == includeLocations == includeOrganizations == includeTimeandDate == True:
        for line in S.splitlines():
            count += 1 
            findNames(count,line)
            findLocations(count, line)
            findOrganizations(count, line)
            findTimeandDate(count, line)
    else:
        for line in S.splitlines():
            count += 1
            if includeNames:
                findNames(count,line)
            if includeLocations:
                findLocations(count, line)
            if includeOrganizations:
                findOrganizations(count, line)
            if includeTimeandDate:
                findTimeandDate(count, line)

#**************************************#
#**************************************#
#**************************************#
#*****     FLOW STARTS HERE      ******#
#**************************************#
#**************************************#
#**************************************#

# choose the databases from here
'''
# Parameters:
# includeTurkishNames -> add Turkish Names to name_database
# includeEnglishNames -> add English Names to name_database

# includeWorldTurkishLocation -> add Turkish World Locations to location_database
# includeTurkeyDetailedLocation -> add Turkey's Locations detailed version to location_database
# includeWorldEnglishLocation -> add English World Locations to location_database

!!! English Names are not added to the list
!!! English World Locations are not added to the list
'''
database_Person, database_Location, database_Organizations = readDatabases( isPrinted=False,
                                                                            includeEnglishNames=False,
                                                                            includeWorldEnglishLocation=False,
                                                                            )

# SAMPLE_TEXT = "Sabancı Üniversitesi 1999 yılında Prof. Dr. Tosun Terzioğlu kurucu rektörlüğünde İstanbul, Tuzla ilçesinde kurulmuştur.\nŞimdiki rektörü Prof. Dr. Yusuf Leblebici’dir."
# test_file = open("basic_test.txt","r")

if(inputFileName == ""):
    inputFileName = "input.txt"

test_file = open(inputFileName,"r")
SAMPLE_TEXT = test_file.read()

result_file = open("NER Result.csv","w")
result_file.write("Line,Type,Word\n")

findAll(    SAMPLE_TEXT,
            includeNames=True,
            includeLocations=True,
            includeOrganizations=True,
            includeTimeandDate=True )

result_file.close()
test_file.close()