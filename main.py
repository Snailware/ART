import os

class ArtMaker:
    def __init__(self):

        with os.scandir('ascii_art/') as entries:
            for entry in entries:
                print(entry.name)
