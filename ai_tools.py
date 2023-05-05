import os
from langchain.agents import Tool

from spotify import start_playing_song_by_name, start_playing_song_by_lyrics, start_music

def tool_start_palying_song_by_name():
    return Tool(name="Play a song given the name of the song", func= lambda song_name: start_playing_song_by_name(song_name), description=f"given a song name, start playing a song. Action Input is string of song_name", return_direct=True)

def tool_start_palying_song_by_lyrics():
    return Tool(name="Play a song given the lyrics of the song", func= lambda lyrics: start_playing_song_by_lyrics(lyrics), description=f"given lyrics, start playing a song. Action Input is string of lyrics", return_direct=True)

# def tool_start_playback():
#     return Tool(name="Start the spotify playback", func= start_music, description="given start playback, start the spotify playback", return_direct=True)


