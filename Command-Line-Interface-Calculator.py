def pengurangan(a, b):
    return a - b

print("Hasil:", pengurangan(15, 6))

def pembagian(a, b):
    if b == 0:
        return "Error: Tidak bisa membagi dengan nol!"
    return a / b

print(pembagian(10, 2))
print(pembagian(8, 0))
