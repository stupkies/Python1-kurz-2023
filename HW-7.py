
    
        
    #def _str_(self):
        #return f"Auto s registrační značkou{self.registracni_znacka} je {self.typ_vozidla}."


        


class Auto: 
    def __init__(self, registracni_znacka, typ_vozidla, najete_km): # konstruktor tridy - specialni metoda
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True
       

    def info(self):
        return f"Auto s registační značkou {self.registracni_znacka} je {self.typ_vozidla}."
    
    def pujc_auto(self):
        if self.dostupne:
            self.dostupne = False
            return f"Potvrzuji zapůjčení vozidla."
        else:
            return f"Vozidlo není k dispozici."

car1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534) 
car2 = Auto("1P3 4747", "Škoda Octavia", 41253)

zadana_znacka = input("Jakou značku si přejete půjčit - Peugeot/Škoda?")

if zadana_znacka == "Peugeot":
    car = car1
if zadana_znacka == "Škoda":
    car = car2
else:
    exit=()

print(car.info())
print(car.pujc_auto()) 
print(car2.pujc_auto())








  

   



