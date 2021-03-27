# mengecek apakah angka yang dimasukkan pengguna 
# bil.prima atau bukan.

input_user = int(input("Masukkan angka: "))
    
if input_user == 1:
    print(input_user, "bukan bilangan prima.")
else:
    arr = []
    if input_user % 1 == 0:
        for i in range(1, input_user+1):
            if input_user % i != 0:
                continue
            else:
                arr.append(i)
    else:
        print(input_user)
        
    if len(arr) > 2:
        print(input_user, "bukan bilangan prima.")
    else:
        print(input_user, "adalah bilangan prima.")
    
    print(arr)

