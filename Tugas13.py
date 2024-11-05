# Soal ke 1
harga_belanja = float(input("Masukkan harga: "))
status = str(input("member atau non-member? "))

if status == "member" :
    if harga_belanja > 1000000 :
        diskon1 = harga_belanja*0.20
        print("Selamat, anda mendapatkan diskon 20%!")
        print("Total belanja anda menjadi Rp,",harga_belanja - diskon1)
    elif harga_belanja >= 500000 :
        diskon2 = harga_belanja*0.15
        print("Selamat, anda mendapatkan diskon 15!")
        print("Total belanja anda menjadi Rp,", harga_belanja - diskon2)
    else:
        diskon3 = harga_belanja*0.10
        print("Selamat, anda mendapatkan diskon 10%!")
        print("Total belanja anda menjadi Rp,", harga_belanja - diskon3)

elif status == "non-member" :
    if harga_belanja > 1000000 :
        diskon1 = harga_belanja*0.10
        print("Selamat, anda mendapatkan diskon 10%!")
        print("Total belanja anda menjadi Rp,",harga_belanja - diskon1)
    elif harga_belanja >= 500000 :
        diskon2 = harga_belanja*0.05
        print("Selamat, anda mendapatkan diskon 5%!")
        print("Total belanja anda menjadi Rp,", harga_belanja - diskon2)
    else:
        print("Tidak ada diskon!")
        print("Total belanja anda menjadi Rp,", harga_belanja)
else:
    print("Member tidak Valid")
print("Terima kasih telah berbelanja, selamat datang kembali!")


# Soal ke 2
jenis_kendaraan = str(input("Motor atau Mobil?: "))
durasi_parkir = float(input("Berapa lama anda akan parkir?: "))

if jenis_kendaraan == "motor" :
    if durasi_parkir <= 2 :
        print("Tarif parkir anda adalah Rp,", 2000)
    else:
        print("Tarif parkir anda adalah Rp,", 2000+(durasi_parkir-2)*1000)
elif jenis_kendaraan == "mobil" :
    if durasi_parkir <= 2 :
        print("Tarif parkir anda adalah Rp,", 5000)
    else:
        print("Tarif parkir anda adalah Rp,", 5000+(durasi_parkir-2)*2000)
else:
    print("Kendaraan tidak Valid")
        
