# program konversi celcius ke satuan lainnya
print("\n---PROGRAM KONVERSI CELCIUS---\n")
celcius = float(input("masukkan suhu dalam celcius = "))
print("suhu adalah = ", celcius, "C")

# reamur
reamur = (4/5) * celcius
print("suhu dalam remaur adalah = ", "R")

# fahrenheit
fahrenheit = (9/5) * celcius + 32
print("suhu dalam fahrenheit adalah = ", "F")

# kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah = ", "K")