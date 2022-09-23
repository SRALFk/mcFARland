#input
print("kalkulator digital")
A=int(input("Masukan nilai A: "))
B=int(input("Masukan nilai B: "))

#program
import math as m
A += B
print("jumlah: ",A)
A-=B
selisih = A-B
kali = A*B
sisa_bagi = B%A
log= m.log10(A)
pangkat = A**B
Sisa2= B%A
mat = m.log10(A)

#hasil

print("selisih: ",selisih)
print("perkalian: ",kali)
print("sisa bagi: ",sisa_bagi)
print("pangkat: ",pangkat)
print("sisa bagi B ke A: ",Sisa2)
print("math: ",mat)