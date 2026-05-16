"""
4. feladat – Új programrész implementálása (5 pont)

Feladat:
Készíts egy CSV fájlt feldolgozó programot, amely környezetvédelmi adatokat kezel.

A CSV fájl szerkezete a következő:
- varos (szöveg)
- ev (szám)
- szennyezettseg_szint (0–100 közötti szám)
- vizszennyezettseg (igen/nem)

Minden függvény 1 pontot ér.

---

1. adatok_beolvasasa(fajlnev)
- Olvasd be a megadott CSV fájl tartalmát (az első sor fejléc).
- A visszatérési érték egy lista legyen, amely sorokat tartalmaz.
  Minden sor egy szótár (dict) az oszlopokkal vagy lista az oszlopok értékeivel.
- Hiba esetén térj vissza üres listával.

---

2. szures_varos_szerint(adatok, varos_nev)
- Szűrd ki azokat a sorokat, amelyek a megadott városhoz tartoznak.
- Példa:
  szures_varos_szerint(adatok, "Budapest") → csak a budapesti sorok

---

3. atlag_szennyezettseg(adatok)
- Számold ki a szennyezettseg_szint értékek átlagát.
- A visszatérési érték egy szám legyen (pl. 45.5).
- Ügyelj arra, hogy az értékeket számként kezeld.

---

4. vizszennyezetseg_statisztika(adatok)
- Számold meg, hány "igen" és hány "nem" szerepel a vizszennyezettseg oszlopban.
- A visszatérési érték egy szótár legyen:
  {"igen": 3, "nem": 5}

---

5. szurt_csv_mentes(adatok, fajlnev, minimum_szint)
- Mentsd ki egy új CSV fájlba azokat a sorokat, ahol:
  szennyezettseg_szint >= minimum_szint
- A kimeneti fájl első sora legyen a fejléc:
  varos,ev,szennyezettseg_szint,vizszennyezettseg

---

"""

import csv


def adatok_beolvasasa(fajlnev):
    # 1. pont: Beolvasás és hiba kezelése üres listával
    adatok = []
    try:
        with open(fajlnev, mode='r', encoding='utf-8', newline='') as f:
            # A DictReader automatikusan az első sor alapján kulcs-érték párokat csinál
            reader = csv.DictReader(f)
            for sor in reader:
                # Érdemes a szám típusokat rögtön átalakítani a könnyebb matekhoz
                sor['ev'] = int(sor['ev'])
                sor['szennyezettseg_szint'] = float(sor['szennyezettseg_szint'])
                adatok.append(sor)
        return adatok
    except Exception:
        # Bármilyen hiba (pl. nem létező fájl) esetén üres listával tér vissza
        return []


def szures_varos_szerint(adatok, varos_nev):
    # 2. pont: Szűrés város név alapján
    szurt = []
    for sor in adatok:
        if sor['varos'] == varos_nev:
            szurt.append(sor)
    return szurt


def atlag_szennyezettseg(adatok):
    # 3. pont: Átlagos szennyezettségi szint kiszámítása
    if not adatok:
        return 0.0

    osszeg = 0
    for sor in adatok:
        osszeg += float(sor['szennyezettseg_szint'])

    return osszeg / len(adatok)


def vizszennyezetseg_statisztika(adatok):
    # 4. pont: Igen/Nem számlálás
    statisztika = {"igen": 0, "nem": 0}
    for sor in adatok:
        statusz = sor['vizszennyezettseg'].strip().lower()
        if statusz in statisztika:
            statisztika[statusz] += 1
    return statisztika


def szurt_csv_mentes(adatok, fajlnev, minimum_szint):
    # 5. pont: Szűrt adatok mentése új CSV fájlba a megfelelő fejléccel
    fejlec = ['varos', 'ev', 'szennyezettseg_szint', 'vizszennyezettseg']

    try:
        with open(fajlnev, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fejlec)
            # Fejléc kiírása
            writer.writeheader()

            # Csak azokat a sorokat írjuk ki, amelyek elérik a minimum szintet
            for sor in adatok:
                if float(sor['szennyezettseg_szint']) >= minimum_szint:
                    writer.writerow(sor)
    except Exception as e:
        print(f"Hiba történt a mentés során: {e}")


# --- Tesztelési lehetőség (opcionális, a ZH-ba nem kötelező, de ellenőrzésre jó) ---
if __name__ == "__main__":
    # Teszt adatok létrehozása egy ideiglenes fájlba
    teszt_fajl = "kornyezet.csv"
    with open(teszt_fajl, "w", encoding="utf-8") as f:
        f.write("varos,ev,szennyezettseg_szint,vizszennyezettseg\n")
        f.write("Budapest,2023,65.5,igen\n")
        f.write("Szeged,2023,30.0,nem\n")
        f.write("Budapest,2024,45.0,nem\n")
        f.write("Debrecen,2024,70.2,igen\n")

    # 1. Beolvasás teszt
    adatok = adatok_beolvasasa(teszt_fajl)
    print("Beolvasott adatok:", adatok)

    # 2. Szűrés város szerint teszt
    bp_adatok = szures_varos_szerint(adatok, "Budapest")
    print("Budapesti adatok:", bp_adatok)

    # 3. Átlag számítás teszt
    print("Átlagos szennyezettség:", atlag_szennyezettseg(adatok))

    # 4. Statisztika teszt
    print("Vízszennyezettség statisztika:", vizszennyezetseg_statisztika(adatok))

    # 5. Mentés teszt
    szurt_csv_mentes(adatok, "sulyos_szennyezes.csv", 50.0)
    print("Szűrt fájl (>=50.0) elmentve 'sulyos_szennyezes.csv' néven.")