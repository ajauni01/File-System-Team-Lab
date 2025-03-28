import os
from Directory import Directory
from File import File


class FileSystem(Directory):
    def __init__(self, root_path):
        super().__init__(root_path)  # Initialize the root directory

    # Allows you to do FileSystem += file/directory and it will add it to the inventory of a directory
    def __iadd__(self, other):
        super().__add__(other)


    def delete_file(self):
        if os.path.exists(self):
            os.remove(self)
            print(f"File '{self}' deleted.")
        else:
            print("File not found.")


if __name__ == "__main__":
    # Driver Code
    fs = FileSystem("root")  # root directory path is just "root"
    fs.create_file()
    
    
    
    