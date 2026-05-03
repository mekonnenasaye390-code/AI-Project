import webbrowser

print("🎧 Music Chatbot Started!")
print("Type 'play song name' to listen music")
print("Type 'exit' to quit\n")

def play_music(song):
    query = song.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

while True:
    user = input("You: ").lower()

    if user == "exit":
        print("Bye 👋")
        break

    elif user.startswith("play"):
        song = user.replace("play", "").strip()
        if song:
            print(f"🎶 Playing: {song}")
            play_music(song)
        else:
            print("⚠️ Please type a song name like: play adele hello")

    else:
        print("🤖 Try: play song name")