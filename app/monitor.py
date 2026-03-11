import time
import winsound
import json
from os import system
from websocket import create_connection

URL = "https://openfront.io/"


def beep():
    winsound.Beep(1200, 200)
    winsound.Beep(1500, 200)


def monitor_games(map_filter, mode_filter, debug, interval, autoopen):

    # Connects to the websocket server to listen for new games.
    socket = create_connection("wss://openfront.io/lobbies")

    # Keep track of found games to avoid duplicates and spam notifications.
    found_games = set()

    mode_aliases = {
        "ffa": "free for all",
        "team": "team"
    }

    #  Convert the mode and map to lowercase for easier comparison, and check if they match the filters.
    mode_filter = mode_filter.lower() if mode_filter is not None else None
    map_filter = map_filter.lower() if map_filter is not None else None

    #  Resolve any mode aliases (e.g. changes "ffa" in to "free for all" so that it can be matched)
    mode_filter = mode_aliases.get(mode_filter, mode_filter) if mode_filter else mode_filter

    while True:
        result = json.loads(socket.recv())

        game_map = result["data"]["lobbies"][0]["gameConfig"]["gameMap"].lower()
        game_mode = result["data"]["lobbies"][0]["gameConfig"]["gameMode"].lower()
        game_id = result["data"]["lobbies"][0]["gameID"]

        if game_id not in found_games:
            found_games.add(game_id)

            #  Check if the mode and map of the current game match the filters.
            mode_matches = not mode_filter or game_mode == mode_filter
            map_matches = not map_filter or game_map == map_filter

            #  If both the mode and map match the filters, or if the filters are not set, notify the user about the new game.
            if mode_matches and map_matches:
                system("cls")  # Clear the screen before printing the new game info to avoid cluttering the console with too many games.
                print(f"Found a new game!\nMap: {game_map}\nMode: {game_mode}")
                beep()
    
    
        #  Sleep for the specified interval before checking for new games again.
        time.sleep(interval)
    