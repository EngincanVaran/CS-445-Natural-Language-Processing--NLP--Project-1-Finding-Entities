from googletrans import *

translator = Translator()

data_file = open("location_data_world.txt","r")
out_file = open("locations_data_world_turkish.txt", "r")

test = data_file.readlines()
test_2 = out_file.readlines()

print(len(test) == len(test_2))

for word in test:
    word = word.strip()
    translated = translator.translate(word, src="en", dest="tr")

    origin = translated.origin
    result = translated.text

    out_file.write(result + "\n")
