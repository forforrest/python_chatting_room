import socket
import threading

def session(sock,addr):
    print 'Accept new connection from %s:%s...' % addr
    sock.send('Welcome!')
    while True:
        data = sock.recv(1024)
        if data == 'exit' or not data:
            break
        sock.send('Hello,%s!' % data)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',8000))

s.listen(5)

print 'Waiting for connection...'

while True:
    socket,addr = s.accept()
    t = threading.Thread(target=session,args=(sock,addr))
    t.start()