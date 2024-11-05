def hitung_luas_lingkaran(jari_jari):
    luas = (jari_jari ** 2)
    return luas

# meminta input dari penguna
jari_jari = float(input("masukan jari-jari lingkaran"))
luas = hitung_luas_lingkaran(jari_jari)

print(f"luas lingkaran dengan jar-jari{jari_jari} adalah {luas:.2f}")