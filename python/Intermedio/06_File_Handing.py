### Manejo de ficheros ###

# .txt file
# ver modo de archivos para ver que modo se pone (w+ lee y escribe)
import os

txt_file = open("python/Intermedio/fichero.txt", "r+")
txt_file.write("Pedro\nNiello\nHogwars Legacy\nDurazno \nSon of the forest")
# print(txt_file.read())
print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
print(txt_file.readlines())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nSon of the forest")
print(txt_file.readline())

txt_file.close()

# os.remove("python/Intermedio/fichero.txt")

#.json file

import json

json_file = open("python/Intermedio/file.json", "w+")

json_test = {
    "Name":"Pedro",
    "Surname":"Niello",
    "Age":"17",
    "Game":["Hogwars Legacy", "son of the forest", "atomic heart"],
    "Website":"https://Twitch.com"}

json.dump(json_test, json_file, indent= 4)

json_file.close()

with open("python/Intermedio/file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

#pasando de json a diccionario
json_dict = json.load(open("python/Intermedio/file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["Name"])

#.csv file
import csv

csv_file = open("python/Intermedio/file.csv","w+")

csv_write = csv.writer(csv_file)
csv_write.writerow(["Name","Surname","Age","Game","Website"])
csv_write.writerow(["Pedro","Niello","17","Son of The Forest","Twitch"])
csv_write.writerow(["Felipe","Error","00","Son of The Forest","404"])

csv_file.close()

with open("python/Intermedio/file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

#.xlsx file
#import xlrd #debe instalarse el modulo

#.xml file
import xml
