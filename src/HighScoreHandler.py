from src.DataHandler import DataHandler

class HighScoreHandler(DataHandler):
    def read_data(self):
        data = super().read_data() 
        if data is None or data.strip() == "" or data.isnumeric() == False:
            return 0
        return int(data)