import os
from Directory import Directory
from File import File


class FileSystem(Directory):
    def __init__(self, root_path):
        super().__init__(root_path)  # Initialize the root directory
            
    def CLI(self):
        selected_item = None
        
        while (True):
            response = input("Enter a command: ").lower()
            
            if response == "select item":
                response = input("What is the path to the file: ")
                for file in self.items:
                    if file.path == response:
                        selected_item = file
                        print("Item selected")
                        break
            elif response == "delete file":
                self.delete_file()
            elif response == "delete directory":
                self.delete_dir()
            elif response == "create file":
                self.create_file()
            elif response == "create directory":
                self.create_dir()
            elif response == "quit":
                return
            elif response == "write":
                if not selected_item:
                    print("No file selected")
                
                for file in self.items:
                    if file == selected_item:
                        file.write()
                        break
                    
            elif response == "read":
                if not selected_item:
                    print("No file selected")
                    
                for file in self.items:
                    if file == selected_item:
                        file.read()
                        break
            elif response == "help":
                print("select item")
                print("create file")
                print("create directory")
                print("delete directory")
                print("delete file")
                print("read")
                print("write")
                print("quit")
                print("help")
            else:
                print(f"{response} is not a valid command('help' for command list)")
                
            

if __name__ == "__main__":
    # Driver Code
    fs = FileSystem("root")  # root directory path is just "root"    
    fs.CLI()        
    
        
    
    
    