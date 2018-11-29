##Kegiatan 1
berkas = open("L200180167.txt","w")
berkas.write("NIM = L200180167\n")
berkas.write("TL = 10-04-1999\n")
berkas.write("Nama = Dzulfiqar Adi\n")
berkas.close()
##Kegiatan 2
berkas = open("L200180167.txt","w")
berkas.write("NIM = L200180167\n")
berkas.write("TL = 10-04-1999\n")
berkas.write("Nama = Dzulfiqar Adi\n")
berkas.write("Kota = Surakarta")
berkas.close()
z = open ("L200180167.txt")
NIM = z.readline()
TL = z.readline()
Nama = z.readline()
Kota = z.readline()
print (Nama)
print (Kota, TL)
print (NIM)
##Kegiatan 3
import shelve
a = open("L200180167.txt","r")
NIM = a.readline()
TL = a.readline()
Nama = a.readline()
a.close()

a = shelve.open("Ijul Gans")
a['b'] = [NIM,TL,Nama]
a.close()
##Kegiatan 4
a = shelve.open("Ijul Gans")
print (a ['b'])
print (a ['b'][0])
print (a ['b'][1])
print (a ['b'][2])
