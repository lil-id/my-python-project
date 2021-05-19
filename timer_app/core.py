import time as tm


#######################################################################################
############################## FUNGSI UNTUK FITUR MENIT ###############################
#######################################################################################

# mengubah masukan/inputan dari menit ke detik.
def minutes(minute_input):
    if minute_input > 1:
        return minute_input * 60
    else:
        return minute_input * 60


# menampilkan waktu menit dan detik
def show_minute(minute: int):
    for time in range(60 - 1, -1, -1):
        if minute == -1:  # kalau menit = 0 maka berhenti.
            print("\nWaktu habis.")
            break
        else:  # kalau menit != 0 maka lanjutkan iterasi.
            if time == 0:
                print("\r" + str(minute) + ' menit ' + str(time) + ' detik', end="")
                show_minute(minute - 1)
            else:
                print("\r" + str(minute) + ' menit ' + str(time) + ' detik', end="")
                tm.sleep(1)