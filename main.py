from ai_agents import initialize_agent_zero_shot
from ai_tools import tool_start_palying_song_by_name, tool_start_palying_song_by_lyrics

tools = [
    tool_start_palying_song_by_name(),
    tool_start_palying_song_by_lyrics(),
]

agent =initialize_agent_zero_shot(tools=tools)

print("\n Hi, This is you Spotify AI Agent. I will take your requests?")

while True:
    request = input("\nSong request: ")
    result = agent({"input": request})
    answer = result["output"]

    print(answer)