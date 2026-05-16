"""
2. feladat - Logikai / szemantikai hibas kod javitasa (5 pont)
TODO:
- A kod fut, de pontosan 5 logikai hibat tartalmaz a feladatok megoldasaban.
- Javitsd ugy, hogy az eredmenyek helyesek legyenek.
- Minden javitas 1 pont.
Feladat:
- Egy vegremenyet statisztikai feldolgozasa.
- Minden vegzett tanulohoz tartozik: nev, szuletesi_ev, atlagpontszam, nyelv.
- Szamold ki:
  1. az atlagos szuletesi evet,
  2. az ossz atlagpontszam,
  3. a nyelvek gyakorisagat,
  4. a legmagasabb atlagpontszammal rendelkezo tanulonak a nevet,
  5. akik a 100-as atlagpontszamnak megfelelnek.

Elvart eredmenyek:
- Atlagos szuletesi ev: 2004
- Atlagos pontszam: 91.0
- Nyelvek gyakorisaga: {'angol': 3, 'nemet': 2}
- Legjobb tanulonak az atlaga: 100
- 100-as tanulok: ['Janos', 'Laszlo']
"""

tanulok = [
    {"nev": "Peter", "szuletesi_ev": 2003, "atlagpontszam": 78, "nyelv": "angol"},
    {"nev": "Maria", "szuletesi_ev": 2005, "atlagpontszam": 85, "nyelv": "angol"},
    {"nev": "Janos", "szuletesi_ev": 2004, "atlagpontszam": 100, "nyelv": "nemet"},
    {"nev": "Anna", "szuletesi_ev": 2004, "atlagpontszam": 92, "nyelv": "angol"},
    {"nev": "Laszlo", "szuletesi_ev": 2005, "atlagpontszam": 100, "nyelv": "nemet"},
]

def atlagos_szuletesi_ev(tanulok_lista):
    if not tanulok_lista:
        return 0
    osszeg = 0
    for tanulo_szuletesi_ev in tanulok_lista:
        # 1. hiba javítása: Nem az életkort (2026 - év) kell összeadni, hanem magát a születési évet
        osszeg += tanulo_szuletesi_ev["szuletesi_ev"]
    return osszeg // len(tanulok_lista)

def atlagos_pontszam(tanulok_lista):
    if not tanulok_lista:
        return 0.0
    osszeg = 0
    for tanulo_atlag in tanulok_lista:
        osszeg += tanulo_atlag["atlagpontszam"]
    # 2. hiba javítása: Átlaghoz osztani kell a darabszámmal, nem szorozni (*)
    return osszeg / len(tanulok_lista)

def nyelvek_gyakorisaga(tanulok_lista):
    gyakorisag = {}
    for tanulo_nyelv in tanulok_lista:
        nyelv = tanulo_nyelv["nyelv"]
        if nyelv in gyakorisag:
            # 3. hiba javítása: Ha már létezik a nyelv, növelni kell a számlálót (+), nem csökkenteni (-)
            gyakorisag[nyelv] += 1
        else:
            gyakorisag[nyelv] = 1
    return gyakorisag

def legjobb_tanulo(tanulok_lista):
    if not tanulok_lista:
        return None
    legjobb = tanulok_lista[0]
    for tanulo in tanulok_lista[1:]:
        # 4. hiba javítása: A legnagyobbat (maximumot) keressük, így '>' kell a '<' helyett
        if tanulo["atlagpontszam"] > legjobb["atlagpontszam"]:
            legjobb = tanulo
    return legjobb["atlagpontszam"]

def szazas_tanulok(tanulok_lista):
    eredmeny = []
    for tanulo in tanulok_lista:
        # 5. hiba javítása: Azokat keressük, akik egyenlőek (==) 100-zal, nem azokat, akik nem egyenlőek (!=)
        if tanulo["atlagpontszam"] == 100:
            eredmeny.append(tanulo["nev"])
    return eredmeny

if __name__ == "__main__":
    print("Atlagos szuletesi ev:", atlagos_szuletesi_ev(tanulok))
    print("Atlagos pontszam:", atlagos_pontszam(tanulok))
    print("Nyelvek gyakorisaga:", nyelvek_gyakorisaga(tanulok))
    print("Legjobb tanulo atlaga:", legjobb_tanulo(tanulok))
    print("100-as tanulok:", szazas_tanulok(tanulok))