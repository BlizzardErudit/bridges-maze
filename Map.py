import State
import random

class Pixel:
    def __init__(self, property: State.State=State.State.Water, nord: State.State=State.State.Water, south: State.State=State.State.Water, east: State.State=State.State.Water, west: State.State=State.State.Water):
        self.property = property
        self.nord = nord
        self.south= south
        self.east = east
        self.west = west
    def available_water_direction(self):
        available = []
        if self.nord == State.State.Water:
            available.append("nord")
        elif self.south == State.State.Water:
            available.append("south")
        elif self.east == State.State.Water:
            available.append("east")
        elif self.west == State.State.Water:
            available.append("west")
        return available
    def available_bridge_direction(self):
        available = []
        if self.nord == State.State.Bridge:
            available.append("nord")
        elif self.south == State.State.Bridge:
            available.append("south")
        elif self.east == State.State.Bridge:
            available.append("east")
        elif self.west == State.State.Bridge:
            available.append("west")
        return available
    def turn_direction_brigde(self, name: str):
        match name:
            case "nord":
                self.nord = State.State.Bridge
            case "south":
                self.south = State.State.Bridge
            case "east":
                self.east = State.State.Bridge
            case "weast":
                self.weast = State.State.Bridge
    

def empty_map(height: int, width: int) -> list[list[Pixel]]:
    the_map = []
    for _ in range(height):
        j = []
        for _ in range(width):
            j.append(Pixel())
        the_map.append(j)

    south_line = []
    for i in range(width):
        if i == 0:
            south_line.append(Pixel(State.State.Bridge, State.State.Water, State.State.SouthBorder, State.State.Bridge,State.State.Water))
        elif i == 49:
            south_line.append(Pixel(State.State.Bridge, State.State.Water, State.State.SouthBorder, State.State.Water,State.State.Bridge))
        else :
            south_line.append(Pixel(State.State.Bridge, State.State.Water, State.State.SouthBorder, State.State.Bridge,State.State.Bridge))
    the_map.reverse()
    the_map.append(south_line)
    the_map.reverse()


    nord_line = []
    for i in range(width):
        if i == 0:
            nord_line.append(Pixel(State.State.Bridge, State.State.Water, State.State.NordBorder, State.State.Bridge,State.State.Water))
        elif i == 49:
            nord_line.append(Pixel(State.State.Bridge, State.State.Water, State.State.NordBorder, State.State.Water,State.State.Bridge))
        else :
            nord_line.append(Pixel(State.State.Bridge, State.State.Water, State.State.SouthBorder, State.State.Bridge,State.State.Bridge))
    the_map.append(nord_line)
    return the_map

def init_map(height: int, width: int):
    direction = []
    the_map = empty_map
    for _ in range(random.randint(10, 15)):
        first_pixel_y = random.randint(50)
        first_pixel_x = the_map.len()-1
        first_pixel = the_map[-1][first_pixel]
        ran = random.choice(first_pixel.available_water_direction())


if __name__ == "__main__":
    test_map = empty_map(50, 100)
    for i in test_map:
        for a in i:
            if a.property == State.State.Bridge:
                print('*', end='')
        print()
