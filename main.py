import os
import Directory
import File


class FileSystem(Directory):
    def __init__(self, root_path):
        super().__init__(root_path)
        pass

    def __add__(self, other):
        super().__add__(other)

    def create_file(self):
        pass

    def delete_file(self):
        pass




if __name__ == "__main__":
    # Driver Code
    print("nothing")