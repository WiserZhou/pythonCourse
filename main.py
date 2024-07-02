import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1', 5005))

while True:
    data, addr = s.recvfrom(1024)
    if not data:
        print('Client has exited!')
        break
    print('Received:', data, 'from', addr)


