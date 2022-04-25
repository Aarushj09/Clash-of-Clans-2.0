from .headers import *

class Building():
    
    # type 0 for town hall, 1 for huts, 2 for walls, 3 for cannons, 4 for wizard tower
    def __init__(self,type,loc):
        self.health = 100
        self.type = type
        self.location = loc   # top left corner
        self.size = [0,0]       # height, width

    def render(self,village):
        for x in range(self.location[0],self.location[0]+self.size[0]):
            for y in range(self.location[1],self.location[1]+self.size[1]):
                village.grid[x][y] = self.shape[x-self.location[0]][y-self.location[1]]
                if self.health >= 50:
                    village.grid[x][y][1] = 0
                elif self.health >= 25:
                    village.grid[x][y][1] = 2
                else:
                    village.grid[x][y][1] = 3
    
class Town_hall(Building):
    
    def __init__(self,loc):
        super().__init__(0,loc)
        self.size = [4,3]
        self.shape =  [[['#',0],['#',0],['#',0]],[['#',0],['T',0],['#',0]],[['#',0],['H',0],['#',0]],[['#',0],['#',0],['#',0]]]
    
class Hut(Building):
    
    def __init__(self,loc):
        super().__init__(1,loc)
        self.size = [2,2]
        self.shape =  [[['H',0],['H',0]],[['H',0],['H',0]]]

class Wall(Building):
    
    def __init__(self,loc):
        super().__init__(2,loc)
        self.size = [1,1]
        self.shape =  [[['W',0]]]

class Cannon(Building):
    
    def __init__(self,loc):
        super().__init__(3,loc)
        self.size = [2,2]
        self.shape =  [[['C',0],['C',0]],[['C',0],['C',0]]]
        self.damage = CANNON_DAMAGE

class Wizard_Tower(Building):

    def __init__(self,loc):
        super().__init__(4,loc)
        self.size = [2,2]
        self.shape =  [[['W',0],['W',0]],[['W',0],['W',0]]]
        self.damage = CANNON_DAMAGE