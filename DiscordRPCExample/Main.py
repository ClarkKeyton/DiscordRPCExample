from pypresence import Presence
import time
myclientID = "1141397716484751473" # This is my client ID :D

presence_discord = Presence(myclientID)

class MainPr:
    def Main():
        presence_discord.connect()
        presence_discord.update(state="Hello!!!", details="Hello From Python", large_text="Hello Word", small_text="Hi!!!")
        time.sleep(5)
if __name__ == "__main__":
    while True:
        MainPr.Main()