class RandomNumber:

    ###
    # Private class fields
    # __value: the random value stored in this object
    # __indexes: the indexes in the dataset where this value was generated

    def __init__(self, value, index):
        self.__value = value
        self.__indexes = []
        self.__indexes.append(index)

    def addIndex(self, index):
        self.__indexes.append(index)

    def __lt__(self, other):
        return len(self.__indexes) < len(other.__indexes)
    
    def __str__(self):
        return f"{self.__value} : {len(self.__indexes)} occurrences @ {self.__indexes}"
