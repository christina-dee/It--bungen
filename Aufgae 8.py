zahl1 = int(input("Erste Zahl: \n"))
zahl2 = int(input("Zweite Zahl: \n"))
zahl3 = int(input("Dritte Zahl: \n"))

if zahl1 < zahl2 < zahl3:
    print("die reihenfolge der zahlen lautet", zahl1, "," ,zahl2, "," ,zahl3)
elif zahl1 < zahl3 < zahl2:
    print("die reihenfolge der zahlen lautet", zahl1, "," ,zahl3, "," ,zahl2)
elif zahl2 < zahl1 < zahl3:
    print("die reihenfolge der zahlen lautet", zahl2, "," ,zahl1, "," ,zahl3)
elif zahl2 < zahl3 < zahl1:
    print("die reihenfolge der zahlen lautet", zahl2, "," ,zahl3, "," ,zahl1)
elif zahl3 < zahl1 < zahl2:
    print("die reihenfolge der zahlen lautet", zahl3, "," ,zahl1, "," ,zahl2)
elif zahl3 < zahl2 < zahl1:
    print("die reihenfolge der zahlen lautet", zahl3, "," ,zahl2, "," ,zahl1)
