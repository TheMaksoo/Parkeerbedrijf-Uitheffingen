import csv
import os

dataFile = open("..\\PO.csv", "r", encoding="UTF-8")
dataDict = csv.DictReader(dataFile)
dataList = list(dataDict)

os.system('cls')
print(f"Welkom bij de parkeer uiheffingen.!")
os.system('cls')