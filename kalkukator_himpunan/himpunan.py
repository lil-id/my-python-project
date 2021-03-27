def mainMenu():
    print("Selamat Datang !")
    print("Pilih operasi himpunan")
    print("1. Irisan")
    print("2. Gabungan")
    print("3. Selisih")
    print("4. Komplement")
    print("5. Keluar")
    
    pilihan = input("Masukkan angka: ")
    
    if pilihan == "1":
        print("Operasi: Irisan")
        angkaHimpunan(pilihan)
    elif pilihan == "2":
        print("Operasi: Gabungan")
        angkaHimpunan(pilihan)
    elif pilihan == "3":
        print("Operasi: Selisih")
        angkaHimpunan(pilihan)
    elif pilihan == "4":
        print("Operasi: Komplemen")
        angkaHimpunan(pilihan)
    elif pilihan == "5":
        print("Selamat Tinggal.")
        exit()
    else:
        print("Maaf menu yang kamu cari tidak ada.")
        
def angkaHimpunan(operasi_dipilih):
    print("=========================================")
    print("Contoh format penulisan himpunan : 2 3 4")
    print("=========================================")
    
    himpunan_1 = list(map(int, input("Masukkan angka himpunan 1: ").rstrip().split()))
    himpunan_2 = list(map(int, input("Masukkan angka himpunan 2: ").rstrip().split()))
    
    if operasi_dipilih == "1":
        irisan(himpunan_1,himpunan_2)
    elif operasi_dipilih == "2":
        gabungan(himpunan_1,himpunan_2)
    elif operasi_dipilih == "3":
        selisih(himpunan_1,himpunan_2)
    else:
        komplemen(himpunan_1,himpunan_2)

def ubahList(nilai_satu, nilai_dua, tipe_operasi):
    if nilai_satu and nilai_dua != []:
        convert_1 = " ".join(map(str, nilai_satu))
        convert_2 = " ".join(map(str, nilai_dua))
        print(tipe_operasi + " himp. 1" + " = " + convert_1)
        print(tipe_operasi + " himp. 2" + " = " + convert_2)
        keluar()
    else:
        print(tipe_operasi + " tidak di temukan.")
        print("=========================================")
        
    mainMenu()
    
def keluar():

    print("")
    tanya = input("Ingin coba operasi yang lain? (Y/N): ")
    print("")
    
    if tanya.upper() == "Y":
        mainMenu()
    elif tanya.upper() == "N":
        print("Selamat Tinggal.")
        exit()

def irisan(himp_1,himp_2):

    nama = "Irisan"
    
    irisan_1 = []
    irisan_2 = []
    
    if len(himp_1) == len(himp_2):
        if himp_1 and himp_2 != []:
            for i in himp_1:
                for j in himp_2:
                    if i == j:
                        irisan_1.append(i)
                        irisan_2.append(j)
                    else:
                        pass
    
        else:
            print("Masukkan anggota himpunan min. 1")
    else:
        print("Pastikan panjang himpunan sama.")

    ubahList(irisan_1, irisan_2, nama)
    
def gabungan(himp_1,himp_2):

    nama = "Gabungan"
    
    gabungan_1 = []
    gabungan_2 = gabungan_1
    
    if len(himp_1) == len(himp_2):
        if himp_1 and himp_2 != []:
            gabung = himp_1 + himp_2
            for i in gabung:
                if i in gabungan_1:
                    continue
                else:
                    gabungan_1.append(i)
        else:
            print("Masukkan anggota himpunan min. 1")
    else:
        print("Pastikan panjang himpunan sama.")
    
    ubahList(sorted(gabungan_1), sorted(gabungan_2),nama)

def selisih(himp_1,himp_2):

    nama = "Selisih"
    
    selisih_1 = []
    selisih_2 = []
    
    if len(himp_1) == len(himp_2):
        if himp_1 and himp_2 != []:
            for i in himp_1:
                if i not in himp_2:
                    selisih_1.append(i)
                else:
                    pass
            for j in himp_2:
                if j not in himp_1:
                    selisih_2.append(j)
                else:
                    pass
        else:
            print("Masukkan anggota himpunan min. 1")
    else:
        print("Pastikan panjang himpunan sama.")

    ubahList(selisih_1, selisih_2, nama)
    
def komplemen(himp_1,himp_2):

    nama = "Komplemen"
    
    komplemen_1 = []
    komplemen_2 = []
    
    if len(himp_1) == len(himp_2):
        if himp_1 and himp_2 != []:
            for i in himp_1:
                if i not in himp_2:
                    komplemen_1.append(i)
                else:
                    pass
            for j in himp_2:
                if j not in himp_1:
                    komplemen_2.append(j)
                else:
                    pass
        else:
            print("Masukkan anggota himpunan min. 1")
    else:
        print("Pastikan panjang himpunan sama.")

    ubahList(komplemen_1, komplemen_2, nama)

mainMenu()
