import State
import random

class Pixel:
    def __init__(self, property: State.State=State.State.Water, north: State.State=State.State.Water, south: State.State=State.State.Water, east: State.State=State.State.Water, west: State.State=State.State.Water, x: int=0, y: int=0):
        self.property = property
        self.north = north
        self.south= south
        self.east = east
        self.west = west
        self.x = x
        self.y = y

    def available_water_direction(self):
        available = []
        if self.north == State.State.Water:
            available.append((self.y-1,self.x,"north"))
        if self.south == State.State.Water:
            available.append((self.y+1,self.x, "south"))
        if self.east == State.State.Water:
            available.append((self.y,self.x+1, "east"))
        if self.west == State.State.Water:
            available.append((self.y,self.x-1,"west"))
        return available
    def available_bridge_direction(self):
        available = []
        if self.north == State.State.Bridge:
            available.append((self.y-1,self.x))
        if self.south == State.State.Bridge:
            available.append((self.y+1,self.x))
        if self.east == State.State.Bridge:
            available.append((self.y,self.x+1))
        if self.west == State.State.Bridge:
            available.append((self.y,self.x-1))
        return available
    def turn_direction_brigde(self, name: str):
        match name:
            case "north":
                self.north = State.State.Bridge
            case "south":
                self.south = State.State.Bridge
            case "east":
                self.east = State.State.Bridge
            case "weast":
                self.weast = State.State.Bridge
    

def empty_map(height: int, width: int) -> list[list[Pixel]]:
    the_map = []
    for a in range(height+2):
        j = []
        if a == 1:
            for i in range(width):
                j.append(Pixel(north=State.State.Bridge,x=i,y=a))
        elif a==height:
            for i in range(width):
                j.append(Pixel(south=State.State.Bridge,x=i,y=a))
        elif a == 0:
            for i in range(width):
                if i == 0:
                    j.append(Pixel(State.State.Bridge, State.State.Water, State.State.NorthBorder, State.State.Bridge,State.State.Water,i,a))
                elif i == 49:
                    j.append(Pixel(State.State.Bridge, State.State.Water, State.State.NorthBorder, State.State.Water,State.State.Bridge,i,a))
                else :
                    j.append(Pixel(State.State.Bridge, State.State.Water, State.State.NorthBorder, State.State.Bridge,State.State.Bridge,i,a))
        elif a == height+1:
            for i in range(width):
                if i == 0:
                    j.append(Pixel(State.State.Bridge, State.State.Water, State.State.SouthBorder, State.State.Bridge,State.State.Water,i,a))
                elif i == 49:
                    j.append(Pixel(State.State.Bridge, State.State.Water, State.State.SouthBorder, State.State.Water,State.State.Bridge,i,a))
                else :
                    j.append(Pixel(State.State.Bridge, State.State.Water, State.State.SouthBorder, State.State.Bridge,State.State.Bridge,i,a))
        else:
            for i in range(width):
                j.append(Pixel(x=i,y=a))
        the_map.append(j)
    return the_map

def init_map(height: int, width: int):
    direction = []
    the_map = empty_map
    for _ in range(random.randint(10, 15)):
        first_pixel_y = random.randint(50)
        first_pixel_x = the_map.len()-1
        first_pixel = the_map[-1][first_pixel]
        ran = random.choice(first_pixel.available_water_direction())
        
        # current_pixel = 


if __name__ == "__main__":
    test_map = empty_map(50, 100)
    for i in test_map:
        for a in i:
            if a.property == State.State.Bridge:
                print('*', end='')
        print()
