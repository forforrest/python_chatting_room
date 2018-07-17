# -*- coding:utf8 -*-

import socket
import threading
import time
import json

socks = {}


def register(name, sock):
    socks[name] = sock
    print 'register %s' % name


def tcplink(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    ack = sock.recv(1024)
    if 'name' in ack:
        print 'registing'
        register(json.loads(ack)['name'], sock)
    while True:
        data = sock.recv(1024)
        if data:
            print 'New Data: %s' % data
            if 'to' in data:
                data = json.loads(data)
                socks[data['to']].send(data['message'])


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind port
    s.bind(('127.0.0.1', 8000))
    s.listen(5)
    print 'Waiting for connection...'

    while True:
        # accept a connection
        sock, addr = s.accept()
        # create a thread to hand the connection
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.setDaemon(True)
        t.start()
