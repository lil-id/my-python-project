# TODO: Buat kode untuk bisa melihat tugas yang ditulis/edit/hapus tanpa menjalankan ulang program.

import os
import time
from os import system, name


def clear():    # fungsi untuk membersihkan layar.
    # windows
    if name == 'nt':
        _ = system('cls')

    # mac dan linux
    else:
        _ = system('clear')


def findPath():  # fungsi untuk menemukan lokasi file "todoList.py"
    # dan menjadikannya sebagai lokasi file todo_list.txt
    return os.getcwd()


def checkTask(display_task):  # fungsi untuk cek apakah sudah ada tugas atau belum.

    file_loc = findPath() + "/todo_list.txt"

    if os.stat(file_loc).st_size == 0:
        print("----------------------------------------------")
        print("¯\_(͡❛ ᴗ ͡❛)_/¯\t Oops! Belum ada tugas.")
        showTask(display_task)
    else:
        print("Tugas hari ini:")
        showTask(display_task)


def showTask(display_task):

    no = 0

    for name_task in display_task:
        no += 1
        print(str(no) + ". " + name_task.strip())  # tampilkan isi file todo_list.txt dan berikan nomor.

    print("----------------------------------------------")
    print("t: tulis    ", "h: hapus   ", "e: edit    ", "k: keluar")

    choice = input("Pilih mode: ")

    if choice.lower() == 't':
        addTask(display_task)
    elif choice.lower() == 'h':
        removeTask()
    elif choice.lower() == 'e':
        editTask()
    elif choice.lower() == 'k':
        exit()
    else:
        clear()
        print("----------------------------------------------")
        print("¯\_(͡❛ ᴗ ͡❛)_/¯\tMode yang di pilih tidak benar")
        showTask(display_task)

    display_task.close()


def addTask(display_task):

    total_add_task = 0

    write_task = input("\nTuliskan tugas: ")

    total_add_task += 1

    # buka file todo_list.txt dengan mode append untuk menambahkan tugas.
    with open(findPath() + "/todo_list.txt", 'a') as append_task:

        append_task.write(write_task + "\n")  # tambahkan tugas yang di inputkan pengguna.

        append_task.close()

    while True:

        ask_user = input("\nMau tulis lagi? (y/t) ")

        if ask_user.lower() == 'y':
            write_again = input("\nTuliskan tugas: ")
            with open(findPath() + "/todo_list.txt", 'a') as append_task:
                append_task.write(write_again + "\n")
                append_task.close()
            total_add_task += 1
        elif ask_user.lower() == "t":
            print("\n" + str(total_add_task), "tugas baru ditambahkan, Bye.")
            exit()
        else:
            print("Maaf pilihan tidak valid.")


def editTask():

    no = 0

    dict_task = {}  # variabel untuk menampung tugas dalam bentuk dictionary

    with open(findPath() + "/todo_list.txt", "r") as rename_task_file:

        for name_task in rename_task_file:  # loop setiap tugas dalam file todo_list.txt
            no += 1
            dict_task[no] = name_task  # masukkan setiap tugas dari file todo_list.txt kedalam dictionary.
            # dan jadikan nomor sebagai key setiap tugas.

    while True:

        try:

            select_task = int(input("\nEdit tugas nomor: "))

            if select_task not in dict_task.keys():
                print("Nomor tugas tidak ada/salah.")
            else:
                rename_task = input("Ubah tugas menjadi: ")
                dict_task[select_task] = rename_task + "\n"

            while True:

                ask_user = input("\nMau ubah lagi? (y/t) ")  # tanya kembali pengguna apakah masih ingin menghapus tugas?

                if ask_user.lower() == 'y':

                    try:
                        select_task_again = int(input("\nEdit tugas nomor: "))

                        # cek apakah nomor tugas yang dipilih sama atau tidak?
                        if select_task_again not in dict_task.keys():
                            print("Nomor tugas tidak ada/salah.")

                        else:
                            rename_task_again = input("Ubah tugas menjadi: ")
                            dict_task[select_task_again] = rename_task_again + "\n"

                    except ValueError:
                        print("Masukkan nomor tugas.")
                        continue

                elif ask_user.lower() == 't':
                    break
                else:
                    print("Maaf pilihan tidak valid.")

        except ValueError:
            print("Masukkan nomor tugas.")
            continue

        break

    os.remove(findPath() + "/todo_list.txt")

    with open(findPath() + "/todo_list.txt", 'a') as new_file_task:
        for update_task in dict_task.values():
            new_file_task.write(update_task)

    print("\nTugas berhasil diperbarui.")


def removeTask():

    no = 0

    dict_task = {}  # variabel untuk menampung tugas dalam bentuk dictionary

    key_want_rm = []  # variabel untuk menampung setiap nomor tugas yang akan dihapus.

    # buka file todo_list.txt dalam mode read dan write.
    with open(findPath() + "/todo_list.txt", "r+") as edit_file:

        for name_task in edit_file:  # loop setiap tugas dalam file todo_list.txt
            no += 1
            dict_task[no] = name_task  # masukkan setiap tugas dari file todo_list.txt kedalam dictionary.
            # dan jadikan nomor sebagai key setiap tugas.

    while True:

        try:

            select_task = int(input("\nHapus tugas nomor: "))

            key_want_rm.append(select_task)  # tambahkan nomor tugas yang di hapus pengguna ke variabel key_want_rm.

            print("Total dipilih:", len(key_want_rm))

            while True:
                
                ask_user = input("\nMau hapus lagi? (y/t) ")  # tanya kembali pengguna apakah masih ingin menghapus tugas?

                if ask_user.lower() == 'y':

                    try:
                        select_task_again = int(input("\nHapus tugas nomor: "))

                        # cek apakah nomor tugas yang dipilih sama atau tidak?
                        if select_task_again not in key_want_rm:
                            key_want_rm.append(select_task_again)
                            print("Total dipilih:", len(key_want_rm))

                        else:
                            print("Tidak bisa memilih nomor tugas yang sama.")

                    except ValueError:
                        print("Masukkan angka.")
                        continue

                elif ask_user.lower() == 't':
                    break
                else:
                    print("Maaf pilihan tidak valid.")

        except ValueError:
            break
        break

    # cek satu-persatu apakah nomor tugas yang dipilih sudah sesuai dengan tugas yang ditampilkan?
    for all_key_rm in key_want_rm:
        if all_key_rm not in dict_task.keys():
            print("\nGagal menghapus tugas!")
            print("Sepertinya ada nomor tugas yang tidak valid.")
            exit()

    # jika nomor tugas yang dipilih sesuai dengan yang ditampilkan maka hapus tugas berdasarkan nomor yang dipilih.
    for all_key_rm in key_want_rm:
        if all_key_rm in dict_task.keys():
            del dict_task[all_key_rm]

    if not key_want_rm:
        print("Gagal menghapus tugas!")
        print("Sepertinya ada nomor tugas yang tidak valid.")
    else:
        print("\n" + str(len(key_want_rm)), "tugas dihapus. Bye.")

    os.remove(findPath() + "/todo_list.txt")

    with open(findPath() + "/todo_list.txt", 'w') as new_file_task:
        for update_task in dict_task.values():
            new_file_task.write(update_task)


if __name__ == "__main__":

    # cek apakah file todo_list.txt sudah ada atau belum.

    if os.path.isfile(findPath() + "/todo_list.txt"):  # Jika file todo_list.txt sudah ada maka langsung buka.
        display_file = open(findPath() + "/todo_list.txt", "r+")
        checkTask(display_file)
        display_file.close()
    else:
        display_file = open(findPath() + "/todo_list.txt", "w+")  # atau kalau belum ada maka buat filenya.
        checkTask(display_file)
        display_file.close()
