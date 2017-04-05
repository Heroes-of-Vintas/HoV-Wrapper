from screenutils import Screen
from Config import *
import datetime
import time
import os


def start_server(screen):
    if not screen.exists:
        os.system("screen -d -S " + screenName + " -m " + startScript)
    screen.send_commands(startScript)


def restart_server(screen):
    if screen.exists:
        screen.send_commands("say Server restarting in 60 seconds.")
        time.sleep(30)
        screen.send_commands("say Server restart in 30 seconds.")
        time.sleep(15)
        screen.send_commands("say Server restart in 15 seconds.")
        time.sleep(10)
        screen.send_commands("say Server restart in 5 seconds.")
        time.sleep(5)
        screen.send_commands("save-all")
        screen.send_commands("kick @a Server restarting, please come back in a minute.")
        screen.send_commands("stop")
        time.sleep(15)
        start_server(screen)


def save_server(screen):
    if screen.exists:
        print("Saving Server")
        screen.send_commands("save-all")


def check_restart_event(screen):
    if os.path.isfile(restartEventFile):
        restart_server(screen)
        os.remove(restartEventFile)


def main():
    has_started_before = False
    save_counter = 0
    screen = Screen(screenName)

    while True:
        if screen.exists:
            print("Server is running")
            if autoSave:
                if save_counter == autoSaveFrequency:
                    save_server(screen)
                    save_counter = 0
                else:
                    save_counter += serverCheckInterval
            if autoRestart:
                current_time = datetime.datetime.now()
                current_time_formatted = current_time.strftime('%H:%M')
                if current_time_formatted in autoRestartTime:
                    restart_server(screen)
                    save_counter = 0
            if checkRestartEvent:
                check_restart_event(screen)
        else:
            if not has_started_before:
                print("Starting the server")
                start_server(screen)
                has_started_before = True
            else:
                print("The server crashed, restarting")
                start_server(screen)

        time.sleep(serverCheckInterval)

main()
