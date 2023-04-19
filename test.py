import socket
import threading
from time import sleep

ya_sock = socket.socket()
addr = ("77.88.55.242", 443)
ya_sock.connect(addr)

data_out = b"Hi server!"
# ya_sock.send(data_out)

data_in = b""



def Recieving():
    global data_in
    while (True):
        data_chunk = ya_sock.recv(1024)
        data_in = data_in + data_chunk


rec_thread = threading.Thread(target=Recieving)
rec_thread.start()
sleep(4)
print(data_in)
ya_sock.close()


