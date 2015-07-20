#! /usr/bin/env python

""" Simple socket message to test robot grasping.
"""

import time
import socket

from math import fabs


id_ = 0

HOST = 'localhost'
PORT = 4000
s = None

toggled = False
grasped = False

def _connect_port(port):
    """ Establish the connection with the given MORSE port"""
    local_socket = None

    for res in socket.getaddrinfo(HOST, port, socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
            local_socket = socket.socket(af, socktype, proto)
        except socket.error as msg:
            local_socket = None
            continue
        try:
            local_socket.connect(sa)
        except socket.error as msg:
            local_socket.close()
            local_socket = None
            continue
        break

    return local_socket

def main():
    global s

    s = _connect_port(PORT)
    if not s:
        sys.exit(1)

    print ("Socket connected")
    global grasped
    grasp("t")
    grasped = True
    s.close()

def grasp(seq):
    """ Sending socket messages """

    msg = b"id0 pr2 grasp_ [\"t\"]\n"
    s.send(msg)
    print("Socket grasp sent")
main()
