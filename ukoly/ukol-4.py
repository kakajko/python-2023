def overeni(telefonni_cislo):
    if len(telefonni_cislo) == 9 or (len(telefonni_cislo) == 13 and telefonni_cislo[:4] == "+420"):
        return True
    else:
        return False
def cena_zpravy(zprava):
    pocet_znaku = len(zprava)
    cena = (pocet_znaku // 180) * 3 
    cena += 3 
    return cena

telefonni_cislo = input("Zadejte číslo: ")
if overeni(telefonni_cislo):
    zprava = input("Napište zprávu: ")
    cena = cena_zpravy(zprava)
    print(f"Cena: {cena} Kč")
else:
    print("Neplatné číslo.")