class Pojistenec:
    def __init__(self, jmeno, prijmeni, vek, telefonni_cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefonni_cislo = telefonni_cislo

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}, {self.vek} let, Tel: {self.telefonni_cislo}"