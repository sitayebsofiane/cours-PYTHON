import socket

host,port = ('localhost',5566)
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind((host,port))
print('le serveur est demarré')

while True:
    socket.listen(5)
    con,address = socket.accept()
    print('un client vient de se connecter...')
    data = con.recv(1024*2)
    data = data.decode('utf8')
    print(data)
con.close()
socket.close()