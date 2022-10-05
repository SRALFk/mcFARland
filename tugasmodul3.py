import math

a = int(input("Masukkan nilai A: "))
b = int(input("Masukkan nilai B: "))
c = int(input("Masukkan nilai C: "))

if (a == 0):
    print("Bukan merupakan persamaan kuadrat, karena nilai A: " + str(a))
else:
    D = pow(b, 2)-(4*a*c)
    if (D > 0):
        x1 = ((-b)+math.sqrt(D))/(2*a)     
        x2 = ((-b)-math.sqrt(D))/(2*a);
        print("Persamaan kuadrat " + str(a) + "x² + " + str(c))
        print("Determinannya: " + str(D))
        print("Memiliki akar berbeda")
        print("Akar x1 = " + str(x1))
        print("Akar x2 = " + str(x2))
    elif (D ==0):
        x1 = (-b)/(2*a)
        x2 = x1
        print("Persamaan kuadrat " + str(a) + "x² + (" + str(b) + ")x + " + str(c))
        print("Determinannya: " + str(D))
        print("Merupakan akar kembar")
        print("Akar = " + str(x2))
    elif (D < 0):
        print("Persamaan kuadrat " + str(a) + "x² + " + str(b) + "x + " + str(c))
        print("Merupakan akar imaginer")
        print("Akar x1 = -" + str(b) + " + " + str(D) + "/2*" + str(a))
        print("Akar x2 = -" + str(b) + " - √" + str(D) + "/2*" + str(a))
    else:
        print("Error, masukan angka yang valid")