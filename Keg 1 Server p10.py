import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50002))
s.listen(5)
print "Server sudah siap"
data = ''
kamus = {'Nama':'Dzulfiqar Adi',
         'NIM':'L200180167',
         'Keluar':'Terimakasih'}
while data.lower() != 'keluar':
    komm, addr = s.accept()
    while data.lower() != 'keluar':
        data = komm.recv(1024)
        print 'Perintah: ',data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send('Maaf, perintah tidak dikenal!')
