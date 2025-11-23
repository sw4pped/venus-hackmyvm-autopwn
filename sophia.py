import paramiko


def get_sophia_password(HOST, PORT):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(hostname=HOST, username="hacker", password="havefun!", port=PORT)

    # Read hidden password
    stdin, stdout, stderr = ssh.exec_command("cat .myhiddenpazz")
    stdout = stdout.readlines()
    password = "".join(stdout).split()[0]
    print(password)
    ssh.close() 

    return password
