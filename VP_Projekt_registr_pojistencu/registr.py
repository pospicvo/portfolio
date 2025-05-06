from pojistenec import Pojistenec

class Registr:
    def __init__(self):
        self.seznam_pojistencu = []

    def pridat_pojistence(self, pojistenec):
        self.seznam_pojistencu.append(pojistenec)

    def vypis_pojistence(self):
        for pojistenec in self.seznam_pojistencu:
            print(pojistenec)

    def najit_pojistence(self, jmeno, prijmeni,):
        nalezeni = [pojistenec for pojistenec in self.seznam_pojistencu if pojistenec.jmeno == jmeno and pojistenec.prijmeni == prijmeni]
        if nalezeni:
            for pojistenec in nalezeni:
                print(pojistenec)
            else:
                print("Pojištěný nebyl nalezen.")