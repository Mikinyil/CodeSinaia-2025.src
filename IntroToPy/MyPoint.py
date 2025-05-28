class MyPoint:
    
    ###
    # class attributes (apply to all instances)
    origX = 0
    origY = 0

    ###
    # private class fields
    # __x
    # __y

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y
    
    def __str__(self):
        return f'Orig=({self.origX},{self.origY}); Point=({self.__x},{self.__y})'
    
    @classmethod
    def rebase(cls, offsetX, offsetY):
        cls.origX += offsetX
        cls.origY += offsetY

if __name__ == "__main__":
    print('This file is not meant to be executed by itself')
