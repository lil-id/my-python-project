def infoIP():
    print('****************************************')
    print('Rentang alamat IP: ')
    print('Kelas A: 1-126')
    print('Kelas B: 128-191')
    print('Kelas C: 192-223')
    print('Kelas D: 224-239')
    print('Kelas E: 240-255')
    print('****************************************')

def cekIP(ip_user, split):
    
    ip_normal = []
    
    for ip in split:
        if int(ip) > 255:
            print('Batas setiap oktet alamat IP adalah 255.')
            exit()
        else:
            ip_normal.append(ip)
    
    classIP(ip_user, ip_normal)

def classIP (ip_user, ip_normal): 

    if int(split[0]) >= 0 and int(split[0]) <= 127:
        class_ip = 'IP Kelas: A (8 bit NetID, 24 bit HostID)'
    elif int(split[0]) > 127 and int(split[0]) < 192:
        class_ip = 'IP Kelas: B (16 bit NetID, 16 bit HostID)'
    elif int(split[0]) > 191 and int(split[0]) < 224:
        class_ip = 'IP Kelas: C (24 bit NetID, 8 bit HostID)'
    elif int(split[0]) > 223 and int(split[0]) < 240:
        class_ip = 'IP Kelas: D (28 bit HostID)'
    elif int(split[0]) > 239 and int(split[0]) < 256:
        class_ip = 'IP Kelas: D (28 bit HostID)'
    else:
        print('Masukkan alamat IP sesuai rentangnya.')
        exit()
        
    detailIP(ip_user, class_ip, split)
    
def detailIP(ip_user, class_ip, split):
    print('****************************************')
    print('Alamat IP: ', ip_user)
    print('Nilai oktet pertama: ', split[0])
    print('Nilai oktet kedua: ', split[1])
    print('Nilai oktet ketiga: ', split[2])
    print('Nilai oktet keempat: ', split[3])
    print(class_ip)
    print('****************************************')

infoIP()

ip_user = input("Masukkan alamat IP: ")

split = ip_user.split('.')

cekIP(ip_user, split)

