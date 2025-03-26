from File import File
import os

class Directory:
    path = ""
    items = []

    def __init__(self, path):
        self.path = path
        os.mkdir(path)

    def __iadd__(self, other):
        self.items.append(other)

    def create_file(self):
        path = input("File Path: ")
        self.items.append(File(path))

    def create_dir(self):
        path = input("Directory Path: ")
        self.items.append(Directory(path))