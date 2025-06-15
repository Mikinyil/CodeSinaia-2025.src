import json


class RandomNumber:

    ###
    # Private class fields
    # __value: the random value stored in this object
    # __indexes: the indexes in the dataset where this value was generated

    def __init__(self, value, index):
        self.__value = value
        self.__indexes = [index]

    def add_index(self, index):
        self.__indexes.append(index)

    def get_value(self):
        return self.__value
    
    def get_count(self):
        return len(self.__indexes)
    
    def get_indexes(self):
        return self.__indexes

    def __lt__(self, other):
        return len(self.__indexes) < len(other.__indexes)
    
    def __str__(self):
        return f"{self.__value} : {len(self.__indexes)} occurrences @ {self.__indexes}"

    def to_dict(self):
        return {
            "value": self.__value,
            "indexes": self.__indexes
        }

    def to_json(self):
        return json.dumps(self.to_dict())
    
    @classmethod
    def from_dict(cls, data):
        obj = cls(data["value"], data["indexes"][0])
        obj.__indexes = data["indexes"]
        return obj
    
    @classmethod
    def from_json(cls, json_str):
        return cls.from_dict(json.loads(json_str))
