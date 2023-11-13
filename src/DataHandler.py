import os

class DataHandler:
    def __init__(self, directory, filename):
        self.directory = directory
        self.filename = filename
        self.file_path = os.path.join(directory, filename)
    
    def write_data(self, data):
        with open(self.file_path, 'w') as file:
            file.write(str(data))
    
    def read_data(self):
        try:
            with open(self.file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return None
