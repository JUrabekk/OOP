class BaseObject:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_coordinates(self):
        return [self.x, self.y, self.z]


class Block(BaseObject):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def shatter(self):
        self.x = None
        self.y = None
        self.z = None


class Entity(BaseObject):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def move(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Thing(BaseObject):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)


block = Block(1, 2, 3)
print(block.get_coordinates())  # Output: [1, 2, 3]
entity = Entity(4, 5, 6)
print(entity.get_coordinates())  # Output: [4, 5, 6]
thing = Thing(10, 11, 12)
print(thing.get_coordinates())  # Output: [10, 11, 12]