import os
import socket

def main_menu():
    conn.sendall("================\n  MENU ADMIN\n================\n1) Service Access\n2) Read EULA/patch note\n3) Quit\ngt72@pwn0: ".encode())
    data = conn.recv(1024)
    choice = data.decode().strip()
    return choice

def boongan():
    conn.sendall("Enter password: ".encode())
    data = conn.recv(1024)
    password = data.decode()
    output = "[!]Access Denied!!!\n\n"
    conn.sendall(output.encode())

def vuln():
    conn.sendall("Choose version (0.1/0.2): ".encode())
    data = conn.recv(1024)
    version = data.decode().strip()
    if version == "0.1":
        output = "- version 0.1\n- bla bla\n\n"
        conn.sendall(output.encode())
    elif version == "0.2":
        output = "- version 0.2\n- upgrade from 0.1\n\n"
        conn.sendall(output.encode())
    else:
        file_path = version
        try:
            with open(file_path, "r") as file:
                output = file.read()
                conn.sendall(output.encode())
        except FileNotFoundError:
            output = "[+]No such file or directory\n\n"
            conn.sendall(output.encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("IP", PORT))
s.listen(1)

while True:
    conn, addr = s.accept()
    while True:
        choice = main_menu()
        if choice == "1":
            boongan()
        elif choice == "2":
            vuln()
        elif choice == "3":
            break
        else:
            output = "Invalid choice\n\n"
            conn.sendall(output.encode())
    conn.close()
