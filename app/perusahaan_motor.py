from function import Perusahaan, Karyawan, Motor, Sales, Teknisi
from datetime import datetime

def formatrupiah(uang):
    y = str(uang)
    if len(y) <= 3:
        return 'Rp ' + y
    else:
        p = y[-3:]
        q = y[:-3]
        return formatrupiah(q) + '.' + p

tanggal = datetime.now()
tgl_sekarang = tanggal.strftime('%d '+'%B '+'%Y')
waktu_lokal = datetime.now()
jam = waktu_lokal.strftime('%H:' + '%M')

# objek sales
tina = Sales('tina', 5000000)
tina.insentif_sales(15000000)
#print('Gaji Sales :', formatrupiah(int(tina.total_pendapatan())))

gani = Teknisi('Gani', 7000000)
#print('Gaji Teknisi :', formatrupiah(int(gani.total_pendapatan())))

# objek perusahaan
perusahaan = Perusahaan('Jaya Motor', 'Jl. Jendral Sudirman, Blok 11', '(021) 9581251', 'jayamotor@gmail.com')

perusahaan.karyawan_aktif(tina)
perusahaan.karyawan_aktif(gani)

# objek motor
yamaha = Motor('jupiter','yamaha',15000000)
honda = Motor('revo', 'honda', 13000000, 5)

perusahaan.daftar_motor(yamaha)
perusahaan.daftar_motor(honda)

jumlah_motor = len(perusahaan.list_motor)
# total pengeluaran perusahaan
#print('Total pengeluaran perusahaan :',formatrupiah(int(perusahaan.total_pengeluaran())))
#print('Total pendapatan perusahaan :',formatrupiah(int(perusahaan.total_pendapatan())))
#print('=======================================')
# diskon motor
#print('Harga motor | ' + yamaha.nama_motor + ' | : ' + formatrupiah(int(Motor.diskon(yamaha))))
#print('Harga motor | ' + honda.nama_motor + ' | : ' + formatrupiah(int(Motor.diskon(honda))))
#print('Diskon ' + honda.nama_motor + ' ' + str(honda.diskon_motor) + '%')
#print('Total harga ' + str(jumlah_motor) + ' motor : ' + formatrupiah(int(perusahaan.total_harga_motor())))

while True:
    print("===============================================================")
    print("                  Selamat datang di " + perusahaan.nama)
    print(perusahaan.alamat + ' ' + perusahaan.telepon + ' ' + perusahaan.email)
    print("===============================================================")
    print("")
    print("Daftar Layanan")
    print("1. Servis Motor")
    print("2. Beli Motor")

    pilihan = int(input("Masukkan pilihan layanan: "))

    if pilihan == 1:
        print("Motor anda akan segera di layani, silahkan menunggu.")
        break
    elif pilihan == 2:
        print("Berikut daftar motor yang tersedia:")
        print('1. ' + yamaha.nama_motor + ' ' + formatrupiah(int(yamaha.harga)))
        print('2. ' + honda.nama_motor + ' ' + formatrupiah(int(honda.harga)))

        print("Jadi beli? ")
        print("1. Ya")
        print("2. Tidak")

        tanya = int(input())

        if tanya == 1:

            no_pilihan = int(input("Masukkan no motor yang dipilih: "))

            if no_pilihan == 1:
                print("Total yang harus dibayar " + formatrupiah(int(Motor.diskon(yamaha))))
            elif no_pilihan == 2:
                print("Selamat anda mendapat diskon " + str(honda.diskon_motor) + '%')
                print("Total yang harus dibayar " + formatrupiah(int(Motor.diskon(honda))))
            else:
                print("Maaf, masukkan no pilihan dengan benar")

        elif tanya == 2:
            print('Baik, terima kasih.')
            break

    else:
        print("Masukkan pilihan dengan benar.")

print('hello world')
