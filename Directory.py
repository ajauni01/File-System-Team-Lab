from File import File
import os

class Directory:
    path = ""
    items = []

    def __init__(self, path):
        self.path = path
        try:
            os.mkdir(path)
        except FileExistsError:
            ""
            
    def __iadd__(self, other):
        self.items.append(other)

    def create_file(self):
        path = input("File Path: ")
        self.items.append(File("root/" + path))

    def create_dir(self):
        path = input("Directory Path: ")
        self.items.append(Directory("root/" + path))