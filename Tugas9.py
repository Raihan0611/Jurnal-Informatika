# Soal nomor 1
angka = float(input("Cek angka Positif atau Negatif: "))
if angka == 0:
    print("Angka nol bukan bilangan positif maupun negatif")
elif angka > 0:
    print("Angka adalah bilangan Positif")
else:
    print("Angka adalah bilangan Negatif")
print()

# Soal nomor 2
angka = float(input("Cek apakah angka termasuk Ganjil atau Genap: "))
if angka == 0:
    print("Angka nol bukan bilangan Ganjil maupun Genap")
elif angka % 2 == 0:
    print("Bilangan termasuk angka Genap")
else:
    print("Bilangan termasuk angka Ganjil")
print()

# Soal nomor 3
umur =  float(input("Masukkan Umur: "))
if umur >= 17:
    print("Sudah cukup umur untuk membuat KTP")
else:
    print("Belum cukup umur untuk membuat KTP")
print()

# Soal nomor 4
belanja = float(input("Cek diskon: "))
if belanja >= 500000:
    diskon = belanja*0.10
    print("Kamu dapat diskon 10% total belanja menjadi Rp",belanja - diskon)
else:
    diskon = belanja*0.05
    print("Kamu dapat diskon 5% total belanja menjadi Rp",belanja - diskon)