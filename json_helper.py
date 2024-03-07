"""This module is used to save the messages from the vtuber twitch channel to a JSON file."""
from pathlib import Path
from json import dumps, loads
from typing import List, Dict


def save_to_json(data, filename) -> Path:
    """Save the data to a JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(dumps(data, indent=4))
    print(f"Saved the data to {filename}")
    return Path(filename).resolve()

def load_from_json(filename) -> List[Dict]:
    """Load the data from a JSON file."""
    with open(filename, "r", encoding="utf-8") as file:
        json_data = loads(file.read())
    return json_data

def add_to_json(data, filename) -> Path:
    """Add the data to a JSON file."""
    if not Path(filename).exists():
        save_to_json([data], filename)
        return

    with open(filename, "r", encoding="utf-8") as file:
        json_data = loads(file.read())
    json_data.append(data)
    save_to_json(json_data, filename)

def load_last_messages(filename, n=5) -> List[Dict]:
    """Load the last n messages from a JSON file."""
    with open(filename, "r", encoding="utf-8") as file:
        json_data = loads(file.read())
    return json_data[-n:]


if __name__ == "__main__":
    test_data = [{
        "name": "Ricardo Escobar",
        "twitch": "https://www.twitch.tv/ricardoescobar",
        "twitter": "https://twitter.com/ricardoescobar",
        "youtube": "https://www.youtube.com/channel/UC3hG3tFZt9G5c0JwY0KX6jg",
    }]
    save_to_json(test_data, "ricardo_escobar.json")
    loaded_data = load_from_json("ricardo_escobar.json")
    loaded_data.append({
        "name": "Ricardo Escobar 2",
        "twitch": "https://www.twitch.tv/ricardoescobar",
        "twitter": "https://twitter.com/ricardoescobar",
        "youtube": "https://www.youtube.com/channel/UC3hG3tFZt9G5c0JwY0KX6jg",
    })
    save_to_json(loaded_data, "ricardo_escobar.json")
    print(load_from_json("ricardo_escobar.json"))