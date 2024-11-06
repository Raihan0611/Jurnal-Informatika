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
Hari Rabu ini, saya dengan beberapa teman izin buat ikut kegiatan GID. Tapi saya sempet nanya ke teman soal tugas yang ada hari itu, dan ternyata ada satu code program Python tentang Password. Dari situ keliatan kalau udah mulai masuk ke materi if.

### Preview Code
[Lihat kode lengkap di Tugas8.py](./Tugas8.py)
```python
passwoard = int(input("Masukkan Password: "))
if passwoard == 1234:
    print("Password Benar")
else:
    print("Password Salah")
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
Pada hari itu saya belajar tentang **Nested if** yaitu kondisi **if** yang ada di dalam kondisi **if lain**, alias **if bertingkat / bersarang**. Biasanya sering dipakai kalau kita mau ngecek beberapa kondisi dalam satu kondisi utama.  

Misalnya, kita mau cek apakah nilai seorang siswa memenuhi syarat kelulusan. Tapi, di dalam kelulusan itu, kita juga mau cek apakah presentase kehadirannya tinggi atau biasa saja.


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

## Jurnal 13
#### Selasa, 5 November 2024
*Deskripsi*  
Hari ini aku dan teman-teman cuma lanjut materi dari minggu lalu. Tapi, Bu Dila kasih tugas tambahan tentang nested if, yaitu bikin program cek diskon berdasarkan member, sama program Python untuk cek parkir kendaraan motor dan mobil.


### Preview code
[Lihat kode lengkap di Tugas13.py](./Tugas13.py)
```python
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
```
## Jurnal 14
#### Rabu, 6 November 2024
*Deskripsi*  
Hari Rabu ini, saya dan teman-teman dikasih tugas latihan Python karena minggu depan ada tes informatika. Bu Dila kasih 5 soal latihan:

1. Tentuin huruf vokal atau konsonan.
2. Tentuin hari berdasarkan angka.
3. Tentuin prestasi berdasarkan nilai.
4. Tentuin harga tiket berdasarkan umur dan hari.
5. Tentuin potongan gaji berdasarkan jam telat dan status kontrak atau tetap.

Tapi setelah ngerjain beberapa soal, Bu Dila meminta saya buat gantian ke Dean biar dia juga belajar dan siap buat ngerjain tes minggu depan.






### Preview code
[Lihat kode lengkap di Tugas14.py](./Tugas14.py)
```python
```
#
> Catatan: Untuk melihat kode lengkap dan lebih detail, silakan klik link file yang disediakan melalui tautan yang tersedia di setiap tugas.



### Selesai~~~
- Azzam Fathur Raihan
- XI-C1
```
```
