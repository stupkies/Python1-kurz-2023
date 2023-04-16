#Povinný úkol:
#Klíč slovníku je kód součástky a hodnota klíče je počet součástek na skladě

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

#Software se nejprve zeptá na kód součástky a poté na množství, které si zákazník chce koupit
kod_soucastky=input("Zadej kod_soucastky")
počet=int(input("Kolik kusů:"))
#Pokud zadaný kód je ve slovníku, součástka je skladem.
if kod_soucastky in sklad:
     print("Součástka je skladem")
 #pokud chce víc než máme, dostane info o maximálním počtu
     if kod_soucastky in sklad and sklad[kod_soucastky] < počet:
          print(f'Bohužel této {kod_soucastky} máme jenom {sklad[kod_soucastky]} kusů') 
     # odpočet na skladu
     sklad[kod_soucastky] -= počet
     # když je 0, tak vymaže
     if sklad[kod_soucastky] ==0:
          del sklad[kod_soucastky]
else:
     print("Součástka není skladem")
print(sklad)

 
 