import socket
from threading import Thread


udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(('', 7790))


def send_msg():
    while True:
        ipaddr = '192.168.0.4'
        port = 8080
        send_data = input("")
        udp_socket.sendto(send_data.encode('utf-8'), (ipaddr, port))


def recv_msg():
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(">>%s:%s" % (str(recv_data[1]), recv_data[0].decode('utf-8')))


if __name__=='__main__':
    t1 = Thread(target=send_msg)
    t2 = Thread(target=recv_msg)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
