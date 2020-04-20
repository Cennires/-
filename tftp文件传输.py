import struct
from socket import *


filename = 'data.txt'
cmp_data = struct.pack('!H%dsb5sb'%len(filename),1,filename.encode(),0,'octet'.encode(),0)
s = socket(AF_INET,SOCK_DGRAM)
addr_ip = '127.0.0.1'
port = 69
s.sendto(cmp_data,(addr_ip, port))
f = open(filename,'ab')

while True:
    recv_data = s.recvfrom(1024)
    operator_number, ack_num = struct.unpack('!HH', recv_data[0][:4])
    if operator_number == 5:
        break
    rand_port = recv_data[1][1]
    ip = recv_data[1][0]
    print(operator_number)
    print(ack_num)
    print(rand_port)
    print(ip)
    f.write(recv_data[0][4:])
    if len(recv_data[0]) < 516:
        break
    ack_data = struct.pack('!HH', 4, ack_num)
    s.sendto(ack_num, (addr_ip, recv_data[1][1]))
