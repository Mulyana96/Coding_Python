#Biasakan membaca Bismillah
#Membuat data mahasiswa
#code Program
list_siswa = []

def pilihannya():
    print('\nSilahkan pilih menu yang tersedia : ')
    print ("1. masukan data.")
    print ("0. logout.")
    pilihan = int(input('Masukkan Pilihanmu : '))
    
    return pilihan
    


def masukkan_data():
    siswa = {}
    masnim = input("masukan nim : ")
    siswa['nim'] = masnim
    masnama = input("masukan nama : ")
    siswa['nama'] = masnama
    masasal = input("masukan asal : ")
    siswa['asal'] = masasal
    list_siswa.append(siswa)


while True:
    pilihan = pilihannya()
    
    if(pilihan == 0):
        break
    elif(pilihan == 1):
        jalankan = masukkan_data()
    else:
        continue

print(list_siswa)
