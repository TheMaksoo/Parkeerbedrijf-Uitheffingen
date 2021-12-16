import csv
import os
from datetime import datetime
import operator


dataFile = open("PO.csv", "r")
dataReader = csv.DictReader(dataFile)
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
                acties += int(x["#_acties"])
                ontheffingen += 1
                i += 1

            math = acties / ontheffingen
            avarage = round(math, 0)
            os.system("cls")
            print(f"Er zijn gemiddeled {int(avarage)} acties per ontheffing.")

        #Top 10 oudste ontheffingen
        if choice == "2":
            top10 = []
            i = 0
            timestamps = []
            list = ""

            for i in dataList:
                timestamps.append(i["datum_start"])
            
            dates = [datetime.strptime(ts, "%d-%m-%Y") for ts in timestamps]
            dates.sort()
            sorteddates = [datetime.strftime(ts, "%d-%m-%Y") for ts in dates]
            for x in range(10): 
                list += f"{sorteddates[x]}\n"
                os.system("cls")
            print(f"{list}")

        # Bepaalde aantal ontheffingen met `reden`.
        if choice == "3":
            i = 0
            amount = 0
            for x in dataList: 
                
                reasonData = (x["reden"])
                if reasonData.lower() == "parkpop 2019":
                    amount += 1
                i += 1
            os.system("cls")
            print(f"Er zijn {amount} ontheffingen met de reden parkpop 2019.")

        # de top 5 redenen
        if choice == "4":
            counterList = {}
            for data in dataList:
                dict = counterList.keys()
                if data["reden"] in dict:
                    counterList[data["reden"]] += 1
                else:
                    new = {data["reden"]: 1}
                    counterList.update(new)
            
            sorted_data = sorted(counterList.items(), key=operator.itemgetter(1), reverse=True)
            os.system("cls")
            for i in range(5):
                print(f"{i + 1}: {sorted_data[i][0]} with {sorted_data[i][1]} uses.")
                     
        # Drukste jaar
        if choice == "5":
            yearCounterList = {}
            for data in dataList:
                dict = yearCounterList.keys()
                date = datetime.strptime(data["datum_start"], '%d-%m-%Y')
                if date.year in dict:
                    yearCounterList[date.year] += int(data["#_acties"])
                else:
                    new = {date.year: int(data["#_acties"])}
                    yearCounterList.update(new)
            os.system("cls")
            sorted_data = sorted(yearCounterList.items(), key=operator.itemgetter(1), reverse=True)
            print(f"The busiest year is {sorted_data[0][0]} with {sorted_data[0][1]} uses.")
 
        # uitheffingen met minder dan 3 keer gebruik van is gemaakt.
        if choice == "6":
            counterList = {}
            for data in dataList:
                dict = counterList.keys()
                if data["reden"] in dict:
                    print(data)
                         
        #meest gebruikte plaats
        if choice == "7":
            counterList = {}
            for data in dataList:
                dict = counterList.keys()
                if data["locatie"] in dict:
                    counterList[data["locatie"]] += 1
                else:
                    new = {data["locatie"]: 1}
                    counterList.update(new)
            
            sorted_data = sorted(counterList.items(), key=operator.itemgetter(1), reverse=True)
            os.system("cls")

            print(f"Most requested street is {sorted_data[0][0]} with {sorted_data[0][1]} requests.")

        if choice == "9":
            counterList = {}
            for data in dataList:
                dict = counterList.keys()
                if data["aanvrager"] in dict:
                    counterList[data["aanvrager"]] += 1
                else:
                    new = {data["aanvrager"]: 1}
                    counterList.update(new)
            
            sorted_data = sorted(counterList.items(), key=operator.itemgetter(1), reverse=True)
            os.system("cls")

            print(f"Person with the most requests is {sorted_data[0][0]} with {sorted_data[0][1]} requests.")
        # Stop programma of laat de keuze opniew afspelen.
        if choice == "8":
            isChoiceRunning = False
            isRunning = False
        else:
            print("----------------------------")
            stop = input(" typ 'X' om door te gaan \n")
            
            os.system('cls')
            if stop.lower() == "x":
                isChoiceRunning = False
        print("einde van het bestand")

       

dataFile.close()