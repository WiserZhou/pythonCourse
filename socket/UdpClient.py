import socket

class UdpClient:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_message(self, message):
        try:
            self.socket.sendto(message.encode("utf-8"), (self.server_ip, self.server_port))
        except Exception as e:
            print(f"Error sending message: {e}")

    def receive_message(self):
        try:
            self.socket.settimeout(1)  # 设置超时时间为1秒
            data, addr = self.socket.recvfrom(1024)
            return data.decode("utf-8"), addr
        except socket.timeout:
            print("Timeout occurred while receiving message.")
            return "", None
        except Exception as e:
            print(f"Error receiving message: {e}")
            return "", None

    def close(self):
        try:
            self.socket.close()
        except Exception as e:
            print(f"Error closing socket: {e}")
