import subprocess

while True:
    command = input("Enter a command: ")
    try:
        result = subprocess.run(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
    except FileNotFoundError:
        print("127")
    else:
        print(result.returncode)
