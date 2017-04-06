# Config file for the hov-wrapper program.

# Full path to the server start script. The script
# must, at minimum, move to the server directory
# and start java.
startScript = "/home/user/server-files/game/start.sh"

# The name to give the screen session running the server.
# Useful if you are running multiple server sessions.
#
# Default: mcserver
screenName = "mcserver"

# How often, in second, to check if the server is still
# up and running.
#
# Default: 5
serverCheckInterval = 5

# If set to true the wrapper will restart the server at
# the given time(s) everyday.
#
# Default: True
autoRestart = True

# List of times to restart the server at. Times should be
# comma separated, and in double quotes using a 24 hour format.
#
# Default: ["05:00"]
autoRestartTime = ["05:00"]

# If set to true the wrapper will save the world every x amount
# of seconds.
#
# Default: True
autoSave = True

# How often, in seconds, you want the world to be saved.
#
# Default: 300 (5 minutes)
autoSaveFrequency = 300

# If this is set to true the wrapper will periodically check for
# an external file (specified below). If the file exists restart
# the server. Useful for triggering restarts from external events.
#
# Default: True
checkRestartEvent = True

# Full path to the file the wrapper will search for when checking
# for the restart event. The wrapper will simply check for this
# file's existence and restart the server if successfully finds the
# file.
restartEventFile = "/home/user/server-files/required-actions/restart-required"
