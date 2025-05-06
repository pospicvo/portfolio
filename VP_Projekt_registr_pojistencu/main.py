# pojištěnci = []
#
# print("------------------------------")
# print("Evidence pojistenych")
# print("------------------------------")
# vstup = 0
# while vstup != 4:
#     vstup = int(input("Vyber si akci: \n 1 - Pridat nového pojistného \n 2 - Vypsat všechny pojistné \n 3 - Vyhledat pojistného \n 4 - Konec\n"))
from pojistenec import Pojistenec
from registr import Registr


def main():
    registr = Registr()

    while True:
        print("------------------------------")
        print("Evidence pojistenych")
        print("------------------------------")

        try:
            vstup = int(input("Vyber si akci: \n 1 - Pridat nového pojistného \n 2 - Vypsat všechny pojistné \n 3 - Vyhledat pojistného \n 4 - Konec\n"))
        except ValueError:
            print("Zadejte prosím číslo od 1 do 4.")
            continue

        if vstup == 1:
            jmeno = input("Zadejte jméno: ")
            prijmeni = input("Zadejte příjmení: ")

            while True:
                try:
                    vek = int(input("Zadejte věk: "))
                    break
                except ValueError:
                    print("Věk musí být číslo")

            telefonni_cislo = int(input("Zadejte telefonní číslo:"))
            pojistenec = Pojistenec(jmeno, prijmeni, vek, telefonni_cislo)
            registr.pridat_pojistence(pojistenec)

        elif vstup == 2:
            registr.pridat_pojistence()

        elif vstup == 3:
            jmeno = input("Zadejte jméno: ")
            prijmeni = input("Zadejte přijmení: ")
            registr.najit_pojistence(jmeno,prijmeni)

        elif vstup == 4:
            print("Ukončuji program.")
            break

        else:
            print("Neplatná volba, zkuste to znovu.")

if __name__ == "__main__":
    main()