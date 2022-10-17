#Inlämningsuppgift moment 02a. Filippa Börjesson. TK21.
import math

nummer = input("Hej! Detta program är till att beräkna omkrets samt area av en cirkel utifrån radien du anger! \n Är radien ett heltal eller decimaltal?: ")
nummer = nummer[0]
nummer = nummer.upper()

if (nummer == "H"):
    radie= int(input('Okej heltal! Vad är cirkelns radie i cm?: '))
    area = radie**2 * math.pi
    omkrets= radie * 2 * math.pi
    print("Radien av cirkeln är " + f"{radie:10.0f}" + "cm.")
    print("Arean av cirkeln är " + f"{area:10.0f}" + "cm\u00b2.")
    print("Omkretsen av cirkeln är " + f"{omkrets:10.0f}" + "cm.")
    print(math.pi)

if (nummer == "D"):
    radie= float(input('Okej decimaltal! Vad är cirkelns radie i cm?: '))
    pi = 3.14
    area = radie**2 * math.pi
    omkrets= radie * 2 * math.pi
    print("Radien av cirkeln är " + f"{radie:10.5f}" + "cm.")
    print("Arean av cirkeln är " + f"{area:10.5f}" + "cm\u00b2.")
    print("Omkretsen av cirkeln är " + f"{omkrets:10.5f}" + "cm.")