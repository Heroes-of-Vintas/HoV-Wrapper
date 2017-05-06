import datetime
import os
import time

from wrapper.Server import Server
from wrapper.Config import *


def restart_server(server):
    if server.is_running():
        server.send_command("say Server restarting in 60 seconds.")
        time.sleep(30)
        server.send_command("say Server restart in 30 seconds.")
        time.sleep(15)
        server.send_command("say Server restart in 15 seconds.")
        time.sleep(10)
        server.send_command("say Server restart in 5 seconds.")
        time.sleep(5)
        server.send_command("kick @a Server restarting, please come back in a minute.")
        server.stop()
        time.sleep(15)
        server.start()


def save_server(server):
    if server.is_running():
        server.send_command("save-all")


def check_restart_event(server):
    if os.path.isfile(restartEventFile):
        restart_server(server)
        os.remove(restartEventFile)


def get_formatted_time():
    current_time = datetime.datetime.now()
    current_time_formatted = current_time.strftime('%H:%M')
    return current_time_formatted


def main():
    has_started_before = False
    save_counter = 0
    server = Server(serverIP, serverPort)

    while True:
        if server.is_running():
            if autoSave:
                if save_counter == autoSaveFrequency:
                    server.send_command("save-all")
                    save_counter = 0
                else:
                    save_counter += serverCheckInterval
            if autoRestart:
                if get_formatted_time() in autoRestartTime:
                    restart_server(server)
                    save_counter = 0
            if checkRestartEvent:
                check_restart_event(server)
        else:
            if has_started_before:
                server.start()
            else:
                server.start()

        time.sleep(serverCheckInterval)

if __name__ == "__main__":
    main()
