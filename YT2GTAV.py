#NOTE: this requires yt-dlp installed along with FFmpeg, and both added to system path in order to function.

# # # # # # # # # # # # #
# # # #   SETUP   # # # #
# # # # # # # # # # # # #

import os
import subprocess

ytUrl = input("Enter The YouTube URL of the Song: ")
GTAVFiles = os.path.expanduser("~/Documents/Rockstar Games/GTA V/User Music")

#if files dont exist create proper folders
if not os.path.exists(GTAVFiles):
    print(f"Creating directory: {GTAVFiles}")
    os.makedirs(GTAVFiles, exist_ok=True)

#setup command to download mp3 file
command = [
    "yt-dlp",
    "--extract-audio",
    "--audio-format", "mp3",
    "--output", os.path.join(GTAVFiles, "%(title)s.%(ext)s"),
    ytUrl,
]

# # # # # # # # # # # # #
# # # #  EXECUTE  # # # #
# # # # # # # # # # # # #

try:
    #execute command
    print("Downloading...")
    subprocess.run(command, check=True)
    print(f"The song has been successfully added to your radio in GTA V.")
#if yt-dlp isnt installed...
except FileNotFoundError:
    print("YT2GTA ERROR: install yt-dlp to use. [pip install yt-dlp]")
    print("If you keep running into issues, ensure that yt-dlp and FFmpeg are both installed and added to your system path.")
#misc error handling
except subprocess.CalledProcessError as e:
    print(f"YT2GTA ERROR: {e}")
    print("If you keep running into issues, ensure that yt-dlp and FFmpeg are both installed and added to your system path.")

input("Press enter to exit.")
