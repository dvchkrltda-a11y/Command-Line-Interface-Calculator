print("Kalkulator Sederhana")
def tambah(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def kali(a, b):
    return a * b

def pembagian(a, b):
    if b == 0:
        return "Error: Tidak bisa membagi dengan nol!"
    return a / b

print("\nPilih operasi:")
print("1. Tambah (+)")
print("2. Kurang (-)")
print("3. Kali (*)")
print("4. Bagi (/)")

pilihan = input("Masukkan pilihan (1/2/3/4): ")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

if pilihan == "1":
    print("Hasil:", tambah(angka1, angka2))
elif pilihan == "2":
    print("Hasil:", pengurangan(angka1, angka2))
elif pilihan == "3":
    print("Hasil:", kali(angka1, angka2))
elif pilihan == "4":
    print("Hasil:", pembagian(angka1, angka2))
else:
    print("Pilihan tidak valid!")