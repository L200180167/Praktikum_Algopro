import socket
def tabung(r=0):
    L = 10 * 3.14 * r * r
    return L
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50003))
s.listen(5)
print "Server sudah siap"
data = ''

while 1:
    komm, addr = s.accept()
    while data.lower() !='keluar':
        data = komm.recv(1024)
        print 'Pesan:', data
        if data.find("parameter") != -1:
            param, value = data.split("=")
            if param == "parameter1":
                r = float(value)
                x = value
                komm.send("Parameter dicatat")
        elif data=='Hitung':
            komm.send('volume tabung dengan tinggi 10cm dan jari-jari {} adalah {}'.format(x, tabung(r)))
        else:
            komm.send('Tidak bisa')
