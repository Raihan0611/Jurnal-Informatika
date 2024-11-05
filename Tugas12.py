while True:
    usia = int(input("Masukkan umur: "))
    if usia <= 0 :
        print("Belum lahir")
    elif usia < 13 :
        print ("Kategori: Anak-anak")
    elif usia <= 18 :
        print ("Kategori: Remaja")
    elif usia <= 50 :
        if usia < 30 :
            print ("Kategori: Dewasa Muda")
        else:
            print ("Kategori: Dewasa")
    else:
        print ("Kategori: Lansia")

    nilai = int(input("Masukkan nilai: "))
    hadir = int(input("Masukkan presentase kehadiran: "))
    if (nilai >= 75) and (hadir >= 80):
        print("Lulus")
    elif nilai < 75 :
        if hadir > 90 :
            print("Perbaiki nilai ujian")
        else:
            print("Tidak Lulus")
    else:
        print("Tingkatkan kehadiran")
