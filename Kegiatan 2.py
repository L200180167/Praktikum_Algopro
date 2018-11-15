password =str(input('Masukan Password: '))
for x in range(2):
    if password =='Adi':
        print ("Anda Telah Login!")
        break
    elif password !='Adi':
        print ("Maaf Password Anda Salah")
        password = str(input('Masukan Password: '))
else :
    print ("Anda telah salah 3 kali, Akses Anda Ditolak") 
    
