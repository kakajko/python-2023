
sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

def prodej_soucastky():
    kod_soucastky = input("Kód:")
    
    if kod_soucastky in sklad:
        mnozstvi = int(input("Množství:"))
        skladove_mnozstvi = sklad[kod_soucastky]
        
        if skladove_mnozstvi >= mnozstvi:
            print("Poptávku lze uspokojit v plné výši.")
            sklad[kod_soucastky] -= mnozstvi
        else:
            print("Lze prodat pouze omezené množství kusů.")
            del sklad[kod_soucastky]
    else:
        print("Součástka není skladem.")

prodej_soucastky()

