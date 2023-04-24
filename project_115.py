import os

source = "main.txt"
destination = "newFile.txt"

os.rename(source, destination)
print("File Renamed")