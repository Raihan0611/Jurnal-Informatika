def tahun():
    tahun = int(input("Masukkan tahun: "))
    if tahun % 400 == 0:
        print(tahun, "adalah tahun kabisat.")
    elif tahun % 100 == 0:
        print(tahun, "bukan tahun kabisat.")
    elif tahun % 4 == 0:
        print(tahun, "adalah tahun kabisat.")
    else:
        print(tahun, "bukan tahun kabisat.")
    print()

def segitiga():
    a = float(input("Masukkan angka A: "))
    b = float(input("Masukkan angka B: "))
    c = float(input("Masukkan angka C: "))
    if a == b == c:
        print("Merupakan segitiga sama sisi")
    elif a == b != c:
        print("Merupakan segitiga sama kaki")
    elif b == c != a:
        print("Merupakan segitiga sama kaki")
    elif c == a != b:
        print("Merupakan segitiga sama kaki")
    else:
        print("Merupakan segitiga sembarang")
    print()

def operasi():
    angka1 = float(input("Masukkan angka ke 1: "))
    angka2 = float(input("Masukkan angka ke 2: "))
    while True:
        operasi = input("Masukkan operasi (+ - x : ) atau (tambah, kurang, kali, bagi): ")
        if (operasi == "+") or (operasi == "tambah"):
            print(angka1, operasi, angka2, "adalah", angka1+angka2)
            break
        elif (operasi == "-") or (operasi == "kurang"):
            print(angka1, operasi, angka2, "adalah", angka1-angka2)
            break
        elif (operasi == "x") or (operasi == "kali"):
            print(angka1, operasi, angka2, "adalah", angka1*angka2)
            break
        elif (operasi == ":") or (operasi == "bagi"):
            try:
                print(angka1, operasi, angka2, "adalah", angka1/angka2)
            except:
                print("tidak terdefinisi")
            break
        else:
            print("Operasi tidak valid")
        print()

while True:
    pilihan = input("1. tahun\n2. segitiga\n3. operasi\n4. keluar\nMasukkan pilihan: ")
    if (pilihan == "1") or (pilihan == "tahun"):
        print()
        tahun()
    elif (pilihan == "2") or (pilihan == "segitiga"):
        print()
        segitiga()
    elif (pilihan == "3") or (pilihan == "operasi"):
        print()
        operasi()
    elif (pilihan == "4") or (pilihan == "keluar"):
        break
    else:
        print("Pilihan tidak valid")
    print()