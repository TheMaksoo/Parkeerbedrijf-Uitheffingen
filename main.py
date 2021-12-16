import csv
import os
from datetime import datetime
import operator


dataFile = open("PO.csv", "r")
dataReader = csv.DictReader(dataFile)
dataList = list(dataReader)

results = open("results.txt", "w")

isRunning = True
os.system('cls')

while isRunning:
    print(f"Welkom bij de parkeer uiheffingen.!") 
    print("1 = Gemiddelde acties per ontheffing.") #DONE
    print("2 = Top 10  oudste ontheffingen.") #DONE
    print("3 = Bepaalde aantal ontheffingen met `reden`.") #DONE
    print("4 = Top 5 redenen voor ontheffingen.") #DONE
    print("5 = Drukste jaar met de meeste acties.") #DONE
    print("6 = Aantal niet effciente uitheffingen.")  # 
    print("7 = Meest aangevraagde plaats voor ontheffingen.")  #DONE
    print("8 = Persoon met de meeste aanvragingen.") #DONE
    print("9 = Stop programma.")
    print("-----------------------")
    choice = input("Keuze 1, 2, 3, 4, 5, 6, 7, 8 of 9: ")
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
            results.write(f"\n-----Gemiddelde acties per ontheffing.-----\nEr zijn gemiddeled {int(avarage)} acties per ontheffing.\n")

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
            print(f"Top 10 oudste ontheffingen.\n{list}")
            results.write(f"-----Top 10 oudste ontheffingen.-----\n{list}")

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
            results.write(f"\n-----Bepaalde aantal ontheffingen met `reden`.-----\nEr zijn {amount} ontheffingen met de reden parkpop 2019.")

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
            results.write("\n-----Top 5 redenen voor ontheffingen.-----")
            for i in range(5):
                print(f"{i + 1}: {sorted_data[i][0]} with {sorted_data[i][1]} uses.")
                results.write(f"{i + 1}: {sorted_data[i][0]} with {sorted_data[i][1]} uses.\n")
                     
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
            results.write(f"\n-----Drukste jaar met de meeste acties.-----\nThe busiest year is {sorted_data[0][0]} with {sorted_data[0][1]} uses.")
 
        # uitheffingen met minder dan 3 keer gebruik van is gemaakt.
        if choice == "6":
            print("-!-!-!-!-! NOT WORKING !-!-!-!-!-")
                    
                         
        #meest gebruikte plaats.
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
            results.write(f"\n-----Meest aangevraagde plaats voor ontheffingen.-----\nMost requested street is {sorted_data[0][0]} with {sorted_data[0][1]} requests.")

        # zoekt de persoon met de meeste aanvragingen.
        if choice == "8":
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
            results.write(f"\n-----Persoon met meeste aanvragingen.-----\nPerson with the most requests is {sorted_data[0][0]} with {sorted_data[0][1]} requests.")

        # Stop programma of laat de keuze opniew afspelen.
        if choice == "9":
            isChoiceRunning = False
            isRunning = False
        else:
            results.write("\n")

            print("----------------------------")
            stop = input(" typ 'X' om door te gaan \n")
            
            os.system('cls')
            if stop.lower() == "x":
                isChoiceRunning = False
        print("einde van het bestand")



dataFile.close()
results.close()