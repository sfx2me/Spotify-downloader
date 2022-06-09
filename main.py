import os
song = input("URL: ")
os.system(f"spotdl {song}")
os.remove(".spotdl-cache")