from pymongo import MongoClient
import certifi
import os


class MongoConnectionManager():
    def __init__(self, database, collection):
        self.client = MongoClient(os.environ.get('MONGO_URI'), tlsCAFile=certifi.where())
        self.database = database
        self.collection = collection
    
    def __enter__(self):
        self.database = self.client[self.database]
        self.collection = self.database[self.collection]
        return self.collection
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.client.close()
