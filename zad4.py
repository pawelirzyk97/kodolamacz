import math
class FunkcjaKwadratowa:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def Rozwiaz(self):
        wspl_a = self.a
        wspl_b = self.b
        wspl_c = self.c

        delta = (wspl_b*wspl_b)-4*(wspl_a*wspl_c)
        print("Delta=", delta)
        if delta>0:
            iks1 = (-wspl_b - math.sqrt(delta))/2*wspl_a
            iks2 = (-wspl_b + math.sqrt(delta))/2*wspl_a
            print("Miejsce zerowe x1=", iks1)
            print("Miejsce zerowe x2=", iks2)
        elif delta==0:
            iks1 = (-wspl_b - math.sqrt(delta)) / 2 * wspl_a
            print("Miejsce zerowe x1=", iks1)
            iks1 = iks1 = (-wspl_b - math.sqrt(delta)) / 2 * wspl_a
        else:
            print("Funkcja nie posiada miejsc zerowych")

class Zespolona:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def print(self):
        if self.im < 0:
            print(f"{self.re}{self.im}i")
        else:
            print(f"{self.re}+{self.im}i")

    def modul(self): # zaookrąglona do 4 miejsc po przecinku
        print("Moduł: ",round(math.sqrt(self.re**2 + self.im**2), 4))

    @staticmethod
    def dodaj(z1, z2):
        return Zespolona(z1.re + z2.re, z1.im + z2.im)

    @staticmethod
    def mnoz(z1, z2): # (a+bi)*(c+di) = ac-bd + (bc+ad)i
        return Zespolona(z1.re*z2.re-z1.im*z2.im, z1.im*z2.re + z1.re*z2.im)

class Ulamek:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def print(self):
        print(f"({self.a}) / ({self.b})")

    def Skroc(self):
        nwd = math.gcd(self.a, self.b)
        self.a //= nwd  # dzielenie
        self.b //= nwd  # bez reszty

    @staticmethod
    def Dodaj( u1, u2):
        wynik = Ulamek(u1.a * u2.b + u2.a * u1.b, u1.b * u2.b)
        wynik.Skroc()
        return wynik

    @staticmethod
    def Odejmij(u1, u2):
        wynik = Ulamek(u1.a *u2.b - u2.a * u1.b, u1.b*u2.b)
        wynik.Skroc()
        return wynik

    @staticmethod
    def Mnozenie(u1, u2):
        wynik= Ulamek(u1.a * u2.a, u1.b * u2.b)
        wynik.Skroc()
        return wynik

    @staticmethod
    def Dzielenie (u1, u2):
        wynik= Ulamek(u1.a * u2.b,u2.a * u1.b)
        wynik.Skroc()
        return wynik




def main():
    #region Kwadratowa
    kwadrat = FunkcjaKwadratowa(1,4,2)
    kwadrat.Rozwiaz()
    #region EndRegionowa

    # region Zespolona
    Z1 = Zespolona(3, 4)  # 3+4i
    Z2 = Zespolona(2, -1)  # 2-1i

    print("Z1: ", end="")
    Z1.print()
    Z1.modul()

    print("Z2: ", end="")
    Z2.print()
    Z2.modul()

    print("Suma: ", end="")
    Zespolona.dodaj(Z1, Z2).print()
    print("Iloczyn: ", end="")
    Zespolona.mnoz(Z1, Z2).print()

    # endregion

    #region Ulamek
    x = Ulamek(2,4)
    y = Ulamek(3,4)
    print("Ulamek bez skrocenia")
    x.print()
    x.Skroc()
    print("Ulamek po skroceniu")
    x.print()
    print("Pierwszy ulamek=")
    x.print()
    print("Drugi ulamek=")
    y.print()
    print("Iloczyn=")
    Ulamek.Mnozenie(x,y).print()
    print("Suma=")
    Ulamek.Dodaj(x,y).print()
    print("Różnica=")
    Ulamek.Odejmij(x,y).print()
    print("Iloraz=")
    Ulamek.Dzielenie(x,y).print()
    #endregion
if __name__ == "__main__":
    main()