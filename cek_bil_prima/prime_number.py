# mengecek apakah angka yang dimasukkan pengguna 
# bil.prima atau bukan.

input_user = int(input("Masukkan angka: "))
    
if input_user == 1:
    print(input_user, "bukan bilangan prima.")
else:
    count = 0
    if input_user % 1 == 0:
        for i in range(1, input_user+1):
            if input_user % i != 0:
                continue
            else:
                count += 1
    else:
        print(input_user)
        
    if count > 2:
        print(input_user, "bukan bilangan prima.")
    else:
        print(input_user, "adalah bilangan prima.")

