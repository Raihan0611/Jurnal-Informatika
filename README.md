# Jurnal-TIK Part 2
---
## Jurnal 6
#### Rabu, 9 Oktober 2024
*Deskripsi*  
Pada hari Rabu saya belajar bersama Bu Dila tentang materi baru yaitu:
- True (benar)
- False (salah)

Kemudian belajar tentang operasi komparasi yaitu:
- \> : Lebih besar dari
- < : Lebih kecil dari
- \>= : Lebih besar sama dengan dari
- <= : Lebih kecil sama dengan dari
- == : Sama dengan
- != : Tidak sama dengan

Setelah mempelajarinya kita diminta untuk latihan membuat kodenya 
### Preview Code
[Lihat kode lengkap di Tugas6.py](./Tugas6.py)
```python
hasil = ganyang < fufufafa
print(ganyang, '<', fufufafa, hasil)
hasil = ganyang > fufufafa
print(ganyang, '>', fufufafa, hasil)
```
---
## Jurnal 7
#### Selasa, 15 Oktober 2024
*Deskripsi*  
Pada hari itu saya dan teman teman saya ditugaskan untuk mempelajari operasi komparasi dari video, Kemudian setelah istirahat diminta untuk membuat kelompok yang berisi 2 orang. Dan saya sekelompok dengan Dean lalu Bu Dila memberi waktu 10 menit untuk menyiapkan bahan presentasi. Kemudian di spin kelompoknya siapa yang akan maju kedepan untuk menjelaskan tentang operasi komparasi.

### Preview Video
[Klik link ini untuk melihat Video](https://youtu.be/Kv_lDWq8kCc?si=9_js_NG4Ip-g2q9A)  

<img src="https://raw.githubusercontent.com/Raihan0611/Jurnal-Informatika/refs/heads/main/Gambar/Jurnal7.png" width="65%" style="max-width: 600px; height: auto;" />

---
## Jurnal 8
#### Rabu, 16 Oktober 2024
*Deskripsi*  
Pada hari Rabu ini saya dan beberapa kawan saya izin untuk mengikuti kegiatan GID. Tetapi saya bertanya ke teman saya apa saja tugas yang ada di hari itu dan saya hanya mendapatkan sebuah code program python tentang Passwoard, itu berarti sudah masuk materi if.

### Preview Code
[Lihat kode lengkap di Tugas8.py](./Tugas8.py)
```python
passwoard = int(input("Masukkan Passwoard: "))
if passwoard == 1234:
    print("Passwoard Benar")
else:
    print("Passwoard Salah")
```

### Bukti Foto GID

<img src="https://github.com/Raihan0611/Jurnal-Informatika/blob/main/Gambar/GID.jpg" width="65%" style="max-width: 600px; height: auto;" />

---
## Jurnal 9
#### Selasa, 22 Oktober 2024
*Deskripsi*  
Pada hari ini saya belajar fungsi **if else**:

- If: digunakan buat ngecek kondisi tertentu. Misalnya, "Kalau cuacanya bagus, jalan-jalan".
- Else: digunakan kalau kondisi if tidak terpenuhi, alias "Selain itu". Misalnya, "Kalau cuacanya hujan, berarti nonton bioskop".

Setelah itu Bu Dila memberikan 4 Soal if else untuk dikerjakan yaitu tentang:  
cek angka positif negatif, cek angka ganjil genap, cek umur, dan cek diskon.

### Preview Code
[Lihat kode lengkap di Tugas9.py](./Tugas9.py)
```python
# Soal nomor 3
umur =  float(input("Masukkan Umur: "))
if umur >= 17:
    print("Sudah cukup umur untuk membuat KTP")
else:
    print("Belum cukup umur untuk membuat KTP")
```
---
## Jurnal 10
#### Rabu, 23 Oktober 2024
*Deskripsi*  
Pada hari Rabu, saya belajar informatika bersama Bu Dila. Hari ini agendanya ngebahas soal-soal yang udah dikerjain kemarin. Sebelum masuk ke soal, kita disuruh ngerjain flowchart dulu. Setelah itu, lanjut deh bahas soal bareng-bareng. Bu Dila minta tiap soal dijelasin sama dua orang, satu buat programnya, satu lagi buat flowchart-nya. Selesai bahas soal, kita disuruh nyelesain program, dan akhirnya selesai juga pembelajaran informatika hari ini.

---
## Jurnal 11
#### Selasa, 29 Oktober 2024
*Deskripsi*  
Pada hari itu Saya belajar tentang **Elif** singkatan dari **"else if"** dalam bahasa pemrograman. Jadi, selain if dan else, kita juga bisa pakai elif buat ngecek lebih dari satu kondisi sebelum sampai ke else.

Misalnya gini, kita mau cek beberapa kondisi:  
- Kalau nilai lebih dari 80, hasilnya "Bagus"
- Kalau nilainya di antara 60-80, hasilnya "Cukup"
- Kalau di bawah 60, "Kurang"

Kode-nya bisa ditulis pakai elif:

### Preview Code
[Lihat kode lengkap di Tugas11.py](./Tugas11.py)
```python
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
```
---

## Jurnal 12
#### Rabu, 30 Oktober 2024
*Deskripsi*  
Pada hari itu saya belajar tentang **Nested if** yaitu kondisi if yang ada di dalam kondisi if lain, alias if bertingkat. Biasanya sering dipakai kalau kita mau ngecek beberapa kondisi dalam satu kondisi utama.  

Misalnya, kamu mau cek apakah nilai seorang siswa memenuhi syarat kelulusan. Tapi, di dalam kelulusan itu, kita juga mau cek apakah presentase kehadirannya tinggi atau biasa saja.


### Preview Code
[Lihat kode lengkap di Tugas12.py](./Tugas12.py)
```python
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
```

---

#
> Catatan: Untuk melihat kode lengkap dan lebih detail, silakan kunjungi file yang bersangkutan melalui tautan yang tersedia di setiap tugas.



### Langkah Akhir:
1. Ganti *penjelasan singkat* dengan deskripsi yang sesuai untuk setiap tugas.
2. Sesuaikan *preview code* berdasarkan isi dari tiap file .py (seperti beberapa fungsi atau bagian penting).
3. Setelah itu, *simpan* sebagai README.md di repositori GitHub-mu.

Dengan ini, setiap tugas akan menampilkan preview kecil dari kodenya, serta link untuk melihat isi lengkapnya.

anjayy template, males ngetik
