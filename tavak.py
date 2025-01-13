SzotarLista = []

with open ("alloviz.txt", "r", encoding="utf-8") as filebe:
    sorok = filebe.read().splitlines()
    for i in range(1,len(sorok)):
        adat = sorok[i].strip().split("\t")
        SzotarLista.append({"nev":adat[0], "tipus":adat[1], "terulet":adat[2], "vizgyujto":adat[3]})

print("3.a feladat")
print(f"{i} tó adatait olvastuk be.")
print("\n")

OsszTerulet = 0
for i in range(len(SzotarLista)):
    OsszTerulet += float(SzotarLista[i]["terulet"])
print("3.b feladat")
print(f"Magyarország {round((OsszTerulet/93036)*100,2)} %-át fedik le a tavak.")
print("\n")

LegnagyobbToIndex = 0
LegnagyobbTo = 0
for i in range(len(SzotarLista)):
    if LegnagyobbTo < int(SzotarLista[i]["vizgyujto"]):
        LegnagyobbTo = int(SzotarLista[i]["vizgyujto"])
        LegnagyobbToIndex = i

print("3.c feladat")
print(f"A legnagyobb vízgyűjtő területű állóvíz: {SzotarLista[LegnagyobbToIndex]['nev']}")
print(f"\tTípusa: {SzotarLista[LegnagyobbToIndex]['tipus']}")
print(f"\tVízfelszíne: {SzotarLista[LegnagyobbToIndex]['terulet']} km2")
print(f"\tVízgyűjtő területe: {SzotarLista[LegnagyobbToIndex]['vizgyujto']} km2")
print("\n")

with open ("kozepes.txt", "w", encoding="utf-8") as fileki:
    for i in range(len(SzotarLista)):
        if float(SzotarLista[i]["terulet"]) >= 3 and float(SzotarLista[i]["terulet"]) <= 10:
            fileki.write(f"{SzotarLista[i]['nev']};{SzotarLista[i]['tipus']}\n")
