import core


try:
    print("Masukkan angka :)")

    input_minutes = int(input("Hitung mundur berapa menit? "))
    real_minute = (core.minutes(input_minutes) // 60) - 1
    core.show_minute(real_minute)
except ValueError:
    print("Masukkan angka.")
