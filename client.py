# -*- coding:utf8 -*-

import threading
import socket
import sys
import json

buffer = []


def init_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 8000))
    s.send(make_register_info())
    return s


def start_listen(sock):
    while True:
        d = sock.recv(1024)
        if d:
            print d


def make_register_info():
    return json.dumps({'name': sys.argv[1]})


def listen_input(sock):
    while True:
        content = raw_input('input:')
        if content:
            # Just send for test
            sock.send(json.dumps({"to": "frank", "message": "hello"}))


if __name__ == '__main__':
    sock = init_socket()
    t = threading.Thread(target=start_listen, args=(sock,))
    t.setDaemon(True)
    t.start()
    listen_input(sock)