#!/usr/bin/env python

import socket as s
import time as t

def send(m, dest_ip, dest_port):
    S = s.socket(s.AF_INET, s.SOCK_STREAM)
    S.connect((dest_ip, dest_port))
    S.sendall(m)
    S.close()

def there_I_fixed_it(dest_ip, dest_port):
    for i in range(16):
        send(b'na\n', dest_ip, dest_port)
        t.sleep(0.5)
    t.sleep(1.5)
    send(b'batman\n', dest_ip, dest_port)

target = '127.0.0.1'
port = 5552

there_I_fixed_it(target, port)
