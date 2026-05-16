"""
1. feladat - Szintaktikai hibas kod javitasa (5 pont)
TODO:
- Javitsd ki az 5 szintaktikai hibat ugy, hogy a program hiba nelkul fusson.
- A program celja:
  1. szamokat kell beolvasni egy listabol,
  2. aritmetikai muveleteket vegezni,
  3. ertekelni az eredmenyeket.
- A program logikajat ne valtoztasd meg, csak a szintaktikai hibakat javitsd.
- Minden javitas 1 pont.
Elvart kimenet a javitas utan:
- Szamok osszege: 45
- Szamok szorzata: 3024 //a jelen számokkal 102.060-nak kellene lennie
- Szamok atlaga: 9.0 //a jelen számokkal 7.5-nek kellene lennie
- Max szam: 12
- Min szam: 3
"""

szamok = [3, 7, 9, 12, 5, 9]

def osszeg_szamitas(lista):
    osszeg = 0
    for szam in lista:
        osszeg = osszeg + szam
    return osszeg

def szorzat_szamitas(lista):
    szorzat = 1
    for szam in lista:
        szorzat *= szam
    return szorzat

def atlaga_szamitas(lista):
    if not lista:
        return 0
    return osszeg_szamitas(lista) / len(lista)

def max_szam(lista):
    if not lista:
        return None
    legnagyobb = lista[0]
    for szam in lista[1:]:
        if szam > legnagyobb:
            legnagyobb = szam
    return legnagyobb

if __name__ == "__main__":
    print("Szamok osszege:", osszeg_szamitas(szamok))
    print("Szamok szorzata:", szorzat_szamitas(szamok))
    print("Szamok atlaga:", atlaga_szamitas(szamok))
    print("Max szam:", max_szam(szamok))
    print("Min szam:", min(szamok))