import random

def terulet (a, b):
    return int(round((a*b)/3.6,0))

telkekSzama = int(input("Add meg a telkek számát! "))

for i in range(telkekSzama):
    a = random.randrange(20,100)
    b = random.randrange(20,100)
    negyszogol = terulet(a,b)
    print(f"{i+1}. telek:")
    print(f"\toldalai: {a} és {b} m")
    print(f"\tterülete: {negyszogol} négyszögöl")
    if negyszogol < 1000:
        print(f"\tTúl kicsi a telek!")