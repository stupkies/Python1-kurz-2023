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
mnozstvi_na_skladu=int(input("Kolik kusů:"))
#Pokud zadaný kód není ve slovníku, není součástka skladem.
if kod_soucastky not in sklad:
     print("Součástka není skladem")
else:
     print("Součástka je skladem")
#Součástka na skladě je, ale je jí méně, než požaduje zákazník
pozadovany_pocet=sklad[kod_soucastky]
if pozadovany_pocet < mnozstvi_na_skladu:
     print(f"Máme jenom {pozadovany_pocet} ks {kod_soucastky}")
     #pokud se sníží požadovaný počet ks na 0 (protože se prodal zákazníkovi) vymazat se skladu
     del sklad[kod_soucastky]
else:
     #součástek je dostatek, sníží se množství na skladu
     print("Součástek máme dostatek")
     sklad.pop(kod_soucastky)


  
 
     


