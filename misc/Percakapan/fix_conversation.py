import socket

def main():
    host = '0.0.0.0'
    port = 1412

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    c, addr = s.accept()
    print("Connection from: " + str(addr))
    print('Hello ctfer')
    sleep(1)
    c.send('You know my favorite number?')
    sleep(1)
    number = input('> ')
    print('%s not my favorite number' %number)
    sleep(1)
    c.send('If you can guess mu favorite number, i will give you a gift')
    c.close()

if __name__ == '__main__':
    main()
