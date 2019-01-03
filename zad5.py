import math
from abc import ABC, abstractmethod
class Figura(ABC):
    def __init__(self, nazwa, podstawa, wysokosc):
        self.nazwa=nazwa
        self.podstawa=podstawa
        self.wysokosc=wysokosc

    @abstractmethod  # tutaj wymuszamy implementację tej metody w klasach pochodnych
    def nazwa_figury(self):
        pass
    def opis(self):
        print("Jestem", self.nazwa_figury(), "moja podstawa = ",self.podstawa,", ","moja wysokosc = ", self.wysokosc)
    def pole(self):
        pole=self.podstawa*self.wysokosc
        print("Moje pole wynosi", pole)
    def obwod(self):
        obwod=2*(self.podstawa+self.wysokosc)
        print("Moj obwod wynosi", obwod)
        print(end='\n')
class Kwadrat(Figura):
    def nazwa_figury(self):
        return "Kwadrat"


class Prostokat(Figura):
    def nazwa_figury(self):
        return "Prostokat"

class Trojkat(Figura):
    def nazwa_figury(self):
        return "Trojkąt"
    def __init__(self, nazwa, podstawa, wysokosc, typ):
        super().__init__(nazwa, podstawa, wysokosc)
        self.typ = typ
    def pole(self):
        pole=self.podstawa*self.wysokosc*0.5
        print("Moje pole wynosi", pole)
    def obwod(self):
        if self.typ == "prostokątny":
            przeciwp=math.sqrt(self.wysokosc*self.wysokosc+self.podstawa*self.podstawa)
            obwod = self.wysokosc + self.podstawa + przeciwp
            print("Moj obwod wynosi", obwod)
        elif self.typ == "równoramienny":
            podst=self.podstawa*0.5
            pomo=math.sqrt(self.wysokosc*self.wysokosc+podst*podst) # pomo -> ramie
            obwod =self.podstawa + 2*pomo
            print("Moj obwod wynosi", obwod)
        elif self.typ == "równoboczny":
            obwod=self.podstawa*3
            print("Moj obwod wynosi", obwod)
print(end='\n')
class Kolo(Figura):

    def nazwa_figury(self):
        return "Koło"

    def __init__(self, nazwa, podstawa, wysokosc, promien):
        super().__init__(nazwa, podstawa, wysokosc)
        self.promien = promien

    def opis(self):
        #super().opis()
        print(end='\n')
        print("Jestem", self.nazwa_figury(),"moj promien to: ", self.promien)
    def pole(self):
        pole=math.pi*self.promien*self.promien
        print("Moje pole wynosi", pole)
    def obwod(self):
        obwod=2*math.pi*self.promien
        print("Moj obwod wynosi", obwod)


def main():

    fig1 = Prostokat("figura1", 5, 4)
    fig1.opis()
    fig1.pole()
    fig1.obwod()

    fig2= Kwadrat("figura2", 6, 6)
    fig2.opis()
    fig2.pole()
    fig2.obwod()

    fig3 = Trojkat("figura3", 3, 4, "prostokątny")
    fig3.opis()
    fig3.pole()
    fig3.obwod()

    fig4 = Kolo("figura4", 3, 3, 3)
    fig4.opis()
    fig4.pole()
    fig4.obwod()

if __name__ == "__main__":
    main()
