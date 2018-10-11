from osascript import osascript
import time
from pypresence import Presence




# INSERT CLIENT ID IN HERE (NOT YOUR DISCORD USER ID, GET CLIENT ID FROM DISCORD BOT AREA)
client_id = ""
RPC = Presence(client_id)
RPC.connect()

def get_current_artist():
    artist_name = osascript('tell application "iTunes" to artist of current track as string')[1]
    if artist_name == "":
        artist_name = "None"
        return artist_name
    else:
        return artist_name

def get_current_song():
    song_name = osascript('tell application "iTunes" to get the name of the current track')[1]
    if song_name == "":
        song_name == "None"
    else:
        return song_name

def update_status():
    if is_playing() == True:
        RPC.update(details=get_current_song(), state=get_current_artist(), large_image="itunes", large_text="iTunes", small_image="play", small_text="Playing!")
    elif is_playing() == False:
        RPC.update(details=get_current_song(), state=get_current_artist(), large_image="itunes", large_text="iTunes", small_image="pause", small_text="Paused!")



def is_playing():
    if osascript('tell application "iTunes" to get player state as string')[1] == "paused":
        return False
    else:
        return True


while True:
    update_status()
    print('updated')
    time.sleep(15)