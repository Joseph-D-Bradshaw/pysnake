from collections import namedtuple
from enum import Enum
from utils import highlight_cell_at_x_y

Vector = namedtuple('Vector', 'x y')

class Heading(Enum):
    NORTH = Vector(0, -1)
    EAST = Vector(1, 0)
    SOUTH = Vector(0, 1)
    WEST = Vector(-1, 0)

    
class BodyPart:
    def __init__(self, x: int, y: int, ref=None, head=False):
        self.x = x
        self.y = y
        self.ref = ref
        print(f'LOG CREATION OF PART: {self.__repr__()}')
        
    @property
    def next(self):
        if type(self.ref) is type(self):
            return self.ref
        return None
    
    def __repr__(self):
        return f'p{id(self)}: ({self.x},{self.y}) -> p{self.next}'


class Snake:
    def __init__(self, surface, x: int, y: int):
        self._surface = surface
        self.head = BodyPart(x, y, head=True)
        self.heading = Heading.EAST
        
    def draw(self):
        part = self.head
        highlight_cell_at_x_y(self._surface, part.x, part.y)  # draw head
        while part.next:  # draw rest of the body
            part = part.next
            highlight_cell_at_x_y(self._surface, part.x, part.y)
            
    def add_part(self):
        tail = self.head
        while tail.next:
            tail = tail.next
        # calculate where to add part by heading
        x = tail.x + self.heading.value.x
        y = tail.y + self.heading.value.y
        tail.ref = BodyPart(x, y)
        
    def move(self):
        part = self.head
        while part.next:
            part.x * self.heading.value.x
            part.y * self.heading.value.y
            part = part.next
