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
            
    def append(self, item):
        self.items.append(item)

    def create_file(self):
        path = input("File Path: ")
        self.items.append(File(path))

    def create_dir(self):
        path = input("Directory Path: ")
        self.items.append(Directory(path))
        
    def delete_file(self):
        path = input("File path: ")
        
        if os.path.exists(path):
            os.remove(path)
            print(f"'{path}' deleted.")
        else:
            print("Path not found")
            
    def delete_dir(self):
        path = input("Directory Path: ")
        
        if os.path.exists(path):
            os.removedirs(path)