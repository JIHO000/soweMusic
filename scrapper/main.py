from bugs import extract_songs
from save import save_to_file
from yt import get_data


if __name__ == "__main__":
    songs = extract_songs()
    save_to_file(songs)
    get_data(songs)