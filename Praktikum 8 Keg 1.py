d = {'NIM' : 'L200180167' , 'Nama' : 'Dzulfiqar Adi' , 'Alamat' : 'Jalan Puntodewo NO.50 Cemani,Grogol,Sukoharjo' , 'Panggilan' : 'Sayang' , 'Kendaraan' : 'Motor Alamat' , 'Prodi' : 'Informatika' , 'Fakultas' : 'Ilmu Komunikasi dan Informatika'}

print ("Pilihan yang tersedia :")
print ("N menampilkan Nama")
print ("I menampilkan NIM")
print ("A menampilkan Alamat")
print ("P menampilkan Panggilan")
print ("K manampilkan Kendaraan")
print ("R menampilkan Prodi")
print ("F menampilkan Fakultas")


def Nama ():
    "menampilkan data diri masing masing 1 setiap data"
    print ('Nama:' + d['Nama'])
def NIM ():
    "menampilkan data diri masing masing 1 setiap data"
    print ('NIM:' + d['NIM'])
def Alamat ():
    "menampilkan data diri masing masing 1 setiap data"
    print ('Alamat:' + d['Alamat'])
def Panggilan ():
    "menampilkan data diri masing masing 1 setiap data"
    print ('Panggilan:' + d['Panggilan'])
def Kendaraan ():
    "menampilkan data diri masing masing 1 setiap data"
    print ('Kendaraan:' + d['Kendaraan'])
def Prodi ():
    "menampilkan data diri masing masing 1 setiap data"
    print ('Prodi:' + d['Prodi'])
def Fakultas ():
    "menampilkan data diri masing masing 1 setiap data"
    print ('Fakultas:' + d['Fakultas'])

repeat = True

while repeat :
    x = input("Pilihan Saudara:")
    if x == ("N") :
        Nama ()
    elif x == ("I"):
        NIM ()
    elif x == ("A"):
        Alamat ()
    elif x == ("P"):
        Panggilan ()
    elif x == ("K"):
        Kendaraan ()
    elif x == ("R"):
        Prodi ()
    elif x == ("F"):
        Fakultas()
    elif x == ("k"):
        print ("Terimakasih!")
        repeat = False
