# ověří telefónní číslo
def verify_number (number):
    if len(number) == 9:
        return True
    elif len(number) == 13 and number [:4] == "+420":
        return True
    else:
        return False
phone_number= input ("Zadej telefónní číslo")

if not verify_number (phone_number):
    print ("Špatný formát")
else:
    print ("Správný formát")

# cena sms
SMS_PRICE = 3
# cena sms závisí na délce zprávy
def total_price (sms_lenght):
    cena = (sms_lenght // 180+1) * SMS_PRICE
    return cena
SMS= input("Zadej text zprávy.")
price = total_price (len(SMS))
print (f'Cena SMS je {price} Kč')



    