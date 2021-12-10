import csv
import os

dataFile = open("PO.csv", "r")
dataDict = csv.DictReader(dataFile)
dataList = list(dataDict)

acties = 0
ontheffingen = 0
gemiddelde = 0

os.system('cls')
print(f"Welkom bij de parkeer uiheffingen.!")

for ontheffing in dataList:
    acties += int(ontheffing["acties"])
    ontheffingen += 1

gemiddelde += acties / ontheffingen

print(f"Er zijn gemiddeled {gemiddelde} gemiddelde acties per ontheffing.")
