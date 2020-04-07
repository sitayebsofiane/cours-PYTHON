import socket

host,port = ('127.0.0.1',5566)
try:
    socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.connect((host,port))
    print('Client connecté !')
 
    data = f'message du bruno'
    data = data.encode("utf8")
    socket.sendall(data)
except ConnectionRefusedError:
    print('erreur conexion')
finally:
    socket.close()
