Nama = str(input('Masukan Nama Anda : '))
Jam = float(input('Pukul Berapa Sekarang?: '))
waktu = ('Pagi', 'Siang', 'Sore', 'Petang', 'Malam')
if 00.00 < Jam <= 10.00 :
    print('Selamat' + '' + waktu[0] + '' + Nama + '.')
elif 10.00 < Jam <= 14.00 :
    print('Selamat' + '' + waktu[1] + '' + Nama + '.')
elif 14.00 < Jam <= 17.30 :
    print('Selamat' + '' + waktu[2] + '' + Nama + '.')
elif 17.30 < Jam <= 19.00 :
    print('Selamat' + '' + waktu[3] + '' + Nama + '.')
elif 19.00 < Jam <= 24.00 :
    print('Selamat' + '' + waktu[4] + '' + Nama + '.')
