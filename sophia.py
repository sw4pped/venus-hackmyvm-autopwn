import paramiko

from constants import VENUS_HOST, VENUS_PORT


def get_sophia_password():
    username = "hacker"
    password = "havefun!"

    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(hostname=VENUS_HOST, username=username, password=password, port=VENUS_PORT)

    _, stdout, _ = ssh.exec_command("cat .myhiddenpazz")
    stdout = stdout.readlines()
    ssh.close() 

    password = "".join(stdout).split()[0]

    return password
