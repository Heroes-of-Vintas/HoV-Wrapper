from subprocess import Popen, PIPE, STDOUT
from wrapper.Config import pathToMinecraft, minecraftExecutable, minecraftArguments
import socket
import os
import time


class Server:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.process = None
        self.start()

    def is_running(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((self.host, self.port))
        if result == 0:
            return True
        else:
            return False

    def start(self):
        os.chdir(pathToMinecraft)
        self.process = Popen(['java', '-jar', minecraftExecutable, minecraftArguments],
                             stdin=PIPE, stdout=PIPE, stderr=STDOUT, universal_newlines=True)

    def send_command(self, command):
        self.process.communicate(command)

    def read(self):
        stdout, stderr = self.process.communicate()
        return stdout

    def stop(self):
        self.send_command("save-all")
        time.sleep(2)
        self.send_command("stop")

if __name__ == "__main__":
    s = Server("127.0.0.1", 25565)
    time.sleep(45)
    if s.is_running():
        s.send_command("plugins")
    time.sleep(3)
    s.stop()
