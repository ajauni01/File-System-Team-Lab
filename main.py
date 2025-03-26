import os
import Directory
import File


class FileSystem(Directory):
    def __init__(self, root_path):
        super().__init__(root_path)  # Initialize the root directory
        pass

    # Allows you to do FileSystem += file/directory and it will add it to the inventory of a directory
    def __iadd__(self, other):
        super().__add__(other)



    def delete_file(self):
        pass


if __name__ == "__main__":
    # Driver Code
    fs = FileSystem("root")  # root directory path is just "root"