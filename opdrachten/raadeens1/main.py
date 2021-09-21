import random
line = "-"
ronde = 1
poging = 1
randomgetal = random.randrange(1, 1000)
spelen = True
print(randomgetal)

print("Bij dit spel probeer je een getal te raden tussen 1 en duizend!")
print(f"Ronde {ronde}")
while spelen:
    Geraden = float(input(f"[{poging}] raad een getal: "))
    if Geraden > 1000 or Geraden < 1:
        print("het moet een getal zijn tussen de 1 en duizend!")
        exit()
    else:
        print(line)
        if Geraden > randomgetal:
            print("Lager!")
        else:
            print("Hoger!")

        if abs(Geraden - randomgetal) <= 20:
            print("Je bent gloeiend heet!")
        elif abs(Geraden - randomgetal) <= 50:
            print("Je bent in de buurt!")
    print(line)
    poging += 1
    if poging > 10:
        opnieuw = input("Helaas heb je dit potje niet gewonnen! wil je nog een keer proberen typ dan: opnieuw, om af te sluiten typ: quit.\n")
        if opnieuw == "quit":
            spelen = False
        elif opnieuw == "opnieuw":
            poging = 1
            ronde = 1
            print(f"Ronde {ronde}")
            randomgetal = random.randrange(1, 1000)
        else:
            print("je hebt niet het goede ingetypt en het programma kan je niet begrijpen!")
            spelen = False
    if ronde > 20:
        print("Je hebt het maximaal aantal potjes bereikt!")
        spelen = False
    if Geraden == randomgetal:
        for i in range(10):
            print("")
        print("Je hebt het getal Geraden!")
        poging = 1
        ronde += 1
        print(f"Ronde {ronde}")
        randomgetal = random.randrange(1, 1000)