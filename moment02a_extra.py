#Inlämningsuppgift moment 02a. Filippa Börjesson. TK21.



nummer = input("Hej! Detta program är till att beräkna omkrets samt area av en cirkel utifrån radien du anger! \n Är radien ett heltal eller decimaltal?: ")


if (nummer == "heltal"):
    radie= int(input('Okej! Vad är cirkelns radie i cm?: '))
    pi = 3.14
    area = radie**2 * pi
    omkrets= radie * 2 * pi
    print("Radien av cirkeln är " + f"{radie:10.0f}" + "cm.")
    print("Arean av cirkeln är " + f"{area:10.0f}" + "cm\u00b2.")
    print("Omkretsen av cirkeln är " + f"{omkrets:10.0f}" + "cm.")
else:
    radie= float(input('Okej! Vad är cirkelns radie i cm?: '))
    pi = 3.14
    area = radie**2 * pi
    omkrets= radie * 2 * pi
    print("Radien av cirkeln är " + f"{radie:10.5f}" + "cm.")
    print("Arean av cirkeln är " + f"{area:10.5f}" + "cm\u00b2.")
    print("Omkretsen av cirkeln är " + f"{omkrets:10.5f}" + "cm.")