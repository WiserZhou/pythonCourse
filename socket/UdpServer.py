import socket

class UdpServer:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.server_ip, self.server_port))

    def receive_message(self):
        try:
            data, addr = self.socket.recvfrom(1024)
            return data.decode("utf-8"), addr
        except Exception as e:
            print(f"Error receiving message: {e}")
            return "", None

    def send_message(self, addr, message):
        try:
            self.socket.sendto(message.encode("utf-8"), addr)
        except Exception as e:
            print(f"Error sending message: {e}")

    def close(self):
        try:
            self.socket.close()
        except Exception as e:
            print(f"Error closing socket: {e}")
