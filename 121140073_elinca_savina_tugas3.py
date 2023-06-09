# -*- coding: utf-8 -*-
"""121140073_Elinca Savina_Tugas3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OH20f9VubXAAfM82b8ULvHT4vMgt9KL8
"""

#no1
import random

class Kotak:
    def __init__(self):
        self.isi = 'bom' if random.random() < 0.25 else 'bukan bom'
        self.status = 'belum dibuka'
    
    def tampilkan(self):
        if self.status == 'belum dibuka':
            return '?'
        elif self.isi == 'bom':
            return 'x'
        else:
            return 'o'
    
    def buka_kotak(self):
        self.status = 'sudah'
        
dimensi = int(input("Masukkan dimensi area: "))
hitung = 0
area = []
for i in range(dimensi):
    row = []
    for j in range(dimensi):
        row.append(Kotak())
    area.append(row)

bom = sum(k.isi == 'bom' for row in area for k in row)
for row in area:
        print(' '.join(k.tampilkan() for k in row))
while True:
    
    nomor_kotak = int(input("Masukkan nomor (1-{}): ".format(dimensi**2)))
    
    row = (nomor_kotak-1) // dimensi
    col = (nomor_kotak-1) % dimensi
    
    kotak = area[row][col]
    kotak.buka_kotak()
    
    if kotak.isi == 'bom':
        print("Game over! anda terkena bom.")
        for row in area:
            print(' '.join(k.tampilkan() for k in row))
        break
    else:
        hitung = hitung + 1
        if hitung == dimensi*dimensi-1:
            print("Selamat! memenangkan game.")
            for row in area:
                print(' '.join(k.tampilkan() for k in row))
            break
        else:
            for row in area:
                print(' '.join(k.tampilkan() for k in row))

#no2
class AkunBank:
    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.nama_pelanggan = nama_pelanggan
        self.no_pelanggan = no_pelanggan
        self.__jumlah_saldo = jumlah_saldo 

    def lihat_saldo(self):
        print(f"saldo anda saat ini adalah : {self.__jumlah_saldo}")

    def tarik_tunai(self, jumlah_uang):
        if jumlah_uang <= self.__jumlah_saldo:
            self.__jumlah_saldo -= jumlah_uang
            print(f"tarik tunai senilai {jumlah_uang} berhasil")
        else:
            print(f"saldo tidak mencukupi!")

    def transfer(self, penerima, jumlah_uang):
        if jumlah_uang <= self.__jumlah_saldo:
            self.__jumlah_saldo -= jumlah_uang
            penerima.__jumlah_saldo += jumlah_uang #penambahan saldo ke rekening tujuan
            print(f"transfer senilai {jumlah_uang} ke {penerima.nama_pelanggan} berhasil")
        else:
            print(f"saldo tidak mencukupi!")

os.system("cls")
Akun1 = AkunBank(1234, "nama_kamu", 5000000000)
Akun2 = AkunBank(2345, "Ukraina", 6666666666)
Akun3 = AkunBank(3456, "Elon Musk", 9999999999)
base_akun = [Akun1, Akun2, Akun3]
while True:
    print("Selamat data di bank jago!")
    print(f"""Halo {Akun1.nama_pelanggan}, ingin melakukan apa?
    1. Lihat saldo
    2. Tarik tunai
    3. Transfer saldo
    4. Keluar""")
    masukan = int(input("Masukkan nomor input: "))
    if (masukan == 1):
        Akun1.lihat_saldo()
    elif(masukan == 2):
        jumlah_tarik = int(input("masukan jumlah tarik tunai : "))
        Akun1.tarik_tunai(jumlah_tarik)
    elif(masukan == 3):
        jumlah_transfer = int(input("masukan jumlah uang yang ingin ditranfer : "))
        no_tujuan = int(input("masukan no pelanggan tujuan : "))
        for akun_tujuan in base_akun:
            if akun_tujuan.no_pelanggan == no_tujuan:
                Akun1.transfer(akun_tujuan, jumlah_transfer)
    elif(masukan == 4):
        break
    print("\n")

#no3
class Mahasiswa:
    
    # atribut kelas
    jumlah_mahasiswa = 0
    nilai_ipk_minimal = 2.5
    
    def __init__(self, nama, jurusan, ipk):
        # atribut instance
        self.nama = nama
        self.jurusan = jurusan
        self.__ipk = ipk  # atribut private
        
        Mahasiswa.jumlah_mahasiswa += 1
    
    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"Jurusan: {self.jurusan}")
        print(f"IPK: {self.__ipk}")
        
    # fungsi public
    def perbarui_ipk(self, ipk_baru):
        if ipk_baru >= Mahasiswa.nilai_ipk_minimal:
            self.__ipk = ipk_baru
            print("IPK berhasil diperbarui.")
        else:
            print("IPK tidak valid.")
    
    # fungsi protected
    def _fungsi_protected(self):
        print("Ini adalah fungsi protected.")
    
    # fungsi private
    def __fungsi_private(self):
        print("Ini adalah fungsi private.")

# membuat objek m1 dari kelas Mahasiswa
m1 = Mahasiswa("John Doe", "Informatika", 3.0)

# memanggil fungsi tampilkan_info pada objek m1
m1.tampilkan_info()

# mengubah nilai IPK pada objek m1
m1.perbarui_ipk(3.5)