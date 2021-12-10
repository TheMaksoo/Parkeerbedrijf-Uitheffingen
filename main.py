import csv
import os

dataFile = open("PO.csv")
dataReader = csv.reader(dataFile)
dataList = list(dataReader)

isRunning = True
os.system('cls')

while isRunning:
    print(f"Welkom bij de parkeer uiheffingen.!")
    print("1 = Gemiddelde acties per ontheffing.")
    print("2 = Top 10  oudste ontheffingen.")
    print("3 = Bepaalde aantal ontheffingen met `reden`.") # zoek functie voor reden
    print("4 = Top 5 redenen voor ontheffingen.") # top 5 redenen die gebuikt waren.
    print("5 = Drukste jaar met de meeste acties.") # jaar met de meeste acties.
    print("6 = Aantal niet effciente uitheffingen.")  # uitheffingen met minder dan 3 keer gebruik van is gemaakt. 
    print("7 = Meest aangevraagde plaats voor ontheffingen.")  
    print("8 = Stop programma.")
    print("-----------------------")
    choice = input("Keuze 1, 2, 3, 4, 5, 6, 7 of 8: ")
    isChoiceRunning = True

    while isChoiceRunning == True:
        # Gemiddelde acties per ontheffing berekening.\
        if choice == "1":
            acties = 0
            ontheffingen = 0
            avarage = 0
            i = 0

            for x in dataList: 
                line = dataList[i][0].split(";")
                acties += int(line[5])
                ontheffingen += 1
                i += 1

            math = acties / ontheffingen
            avarage = round(math, 0)
            print(f"Er zijn gemiddeled {int(avarage)} acties per ontheffing.")

        # Bepaalde aantal ontheffingen met `reden`.
        if choice == "3":
            i = 0
            amount = 0
            for x in dataList: 
                line = dataList[i][0].split(";")
                reasonData = (line[4])
                if reasonData.lower() == "parkpop 2016":
                    amount += 1
                i += 1
            print(f"Er zijn {amount} ontheffingen met de reden parkpop 2016.")

            #Top 10

        # Stop programma of laat de keuze opniew afspelen.
        if choice == "8":
            isChoiceRunning = False
            isRunning = False
        else:
            print("----------------------------")
            stop = input("Druk op enter om door te gaan of typ 'X'\n")
            
            os.system('cls')
            if stop.lower() == "x":
                isChoiceRunning = False