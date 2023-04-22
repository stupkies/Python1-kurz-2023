import json

# načtení slovníku do souboru
with open ('Python1-kurz-2023/body.json', encoding='utf-8') as soubor:
      body=json.load(soubor)
print(body)

# Pass = alespoň 60, Fail míň než 60
prospech = {}
for jmeno, body in body.items():
    if body >= 60:
        prospech[jmeno] = "Pass"
    else:
        prospech[jmeno] = "Fail"
print (prospech)

# chci mít slovník pod vypsaný pod sebou
#for jmeno, body in prospech.items():
    #print (jmeno + ": " + body)

# výsledný seznam uložit do souboru prospěch.json
with open("prospech.json", mode="w", encoding='utf-8') as soubor:
    json.dump(prospech, soubor, ensure_ascii=False)
