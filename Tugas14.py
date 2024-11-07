# Soal ke 1
HURUF = str(input("Masukkan 1 huruf: "))
huruf = HURUF.lower()
if huruf == "a" or huruf == "i" or huruf == "u" or huruf == "e" or huruf == "o":
    print("Ini adalah huruf Vokal")
else:
    print("Ini adalah huruf Konsonan")

# Soal ke 2
hari = int(input("Masukkan angka 1-7: "))
if hari == 1:
    print("Senin")
elif hari == 2:
    print("Selasa")
elif hari == 3:
    print("Rabu")
elif hari == 4:
    print("Kamis")
elif hari == 5:
    print("Jum'at")
elif hari == 6:
    print("Sabtu")
elif hari == 7:
    print("Minggu")
else:
    print("Pilihan tidak tersedia")

# Soal ke 3
nilai = int(input("Masukkan nilai: "))
if nilai > 100:
    print("Kelebihan")
elif nilai >= 90:
    print("Prestasi sangat baik")
elif nilai >= 80:
    print("Prestasi baik")
elif nilai >= 70:
    print("Prestasi cukup")
elif nilai >= 60:
    print("Prestasi kurang")
else:
    print("Tidak memenuhi prestasi minimum")

# Soal ke 4
usia = int(input("Masukkan usia: "))
while True:
    HARI = str(input("Masukkan hari (Senin-Minggu): "))
    hari = HARI.lower()
    if usia < 12:
        if hari == "senin" or hari == "selasa" or hari == "rabu" or hari == "kamis" or hari == "jumat" or hari == "jum'at":
            print("Harga tiket adalah 5000")
            break
        elif hari == "sabtu" or hari == "minggu":
            print("Harga tiket adalah 10000")
            break
        else:
            print("Hari tidak Valid")
    else:
        if hari == "senin" or hari == "selasa" or hari == "rabu" or hari == "kamis" or hari == "jumat" or hari == "jum'at":
            print("Harga tiket adalah 15000")
            break
        elif hari == "sabtu" or hari == "minggu":
            print("Harga tiket adalah 20000")
            break
        else:
            print("Hari tidak Valid")

# Soal ke 5
STATUS = str(input("Status karyawan Tetap/Kontrak? "))
status = STATUS.lower()
if status == "tetap":
    terlambat = int(input("Jumlah jam terlambat? "))
    if terlambat > 5:
        print("Terkena potongan gaji 10%")
    elif terlambat >= 1:
        print("Terkena potongan gaji 5%")
    else:
        print("Tidak ada potongan gaji")
elif status == "kontrak":
    terlambat = int(input("Jumlah jam terlambat? "))
    if terlambat > 3:
        print("Terkena potongan gaji 15%")
    elif terlambat >= 1:
        print("Terkena potongan gaji 7%")
    else:
        print("Tidak ada potongan gaji")
else:
    print("Status tidak valid")