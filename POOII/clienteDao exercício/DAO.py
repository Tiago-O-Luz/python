from abc import ABC
import pickle

class DAO(ABC):
    def __init__(self, datasource=''):
        self.datasource = datasource
        self.objectCache = {}

        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()
    
    def __dump(self):
        pickle.dump(self.objectCache, open(self.datasource, 'wb'))

    def __load(self):
        self.objectCache = pickle.load(open(self.datasource, 'rb'))

    def add(self, key, obj):
        self.objectCache[key] = obj
        self.__dump()
    
    def get(self, key: int):
        if key in self.objectCache:
            return self.objectCache[key]
        else:
            return "Key not found"
        
    def remove(self, key):
        if key in self.objectCache:
            self.objectCache.pop(key)
            self.__dump()
        else:
            return "Key not found"
    
    def get_all(self):
        return self.objectCache.values()