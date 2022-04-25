from .headers import *


class Troop():
    
    # type 0 for barbarian, 1 for king, 2 for archer, 3 for balloon, 4 for queen
    def __init__(self,type):
        self.health = 100
        self.type = type
        self.aerial = False
        self.location = [1,1]
        self.damage = 10
        self.direction = 0
        if(type == 2):
            self.damage = self.damage/2
            self.health = self.health/2
        if(type == 3):
            self.damage = self.damage*2

    def render(self,village):
        if(self.type == 1):
            village.grid[self.location[0]][self.location[1]] = ['K',4]
        if(self.type == 4):
            village.grid[self.location[0]][self.location[1]] = ['Q',4]
        
        if(self.type == 0):
            if self.health>=50:
                village.grid[self.location[0]][self.location[1]] = ['B',5]
            else:
                village.grid[self.location[0]][self.location[1]] = ['B',6]
        if(self.type == 2):
            if self.health>=50:
                village.grid[self.location[0]][self.location[1]] = ['A',5]
            else:
                village.grid[self.location[0]][self.location[1]] = ['A',6]
        if(self.type == 3):
            if self.health>=50:
                village.grid[self.location[0]][self.location[1]] = ['L',5]
            else:
                village.grid[self.location[0]][self.location[1]] = ['L',6]
        


class King(Troop):

    def __init__(self):
        super().__init__(1)
        self.damage = 30

class Queen(Troop):
    
    def __init__(self):
        super().__init__(4)
        self.damage = 15

class Barbarian(Troop):

    def __init__(self, key_pressed, village):
        super().__init__(0)
        if(key_pressed == '7'):
            self.location = [village.spawning_points[0][0],village.spawning_points[0][1]+1]
        if(key_pressed == '8'):
            self.location = [village.spawning_points[1][0]+1,village.spawning_points[1][1]]
        if(key_pressed == '9'):
            self.location = [village.spawning_points[2][0],village.spawning_points[2][1]-1]
        
class Archer(Troop):

    def __init__(self, key_pressed, village):
        super().__init__(2)
        if(key_pressed == '1'):
            self.location = [village.spawning_points[0][0],village.spawning_points[0][1]+1]
        if(key_pressed == '2'):
            self.location = [village.spawning_points[1][0]+1,village.spawning_points[1][1]]
        if(key_pressed == '3'):
            self.location = [village.spawning_points[2][0],village.spawning_points[2][1]-1]
        
class Balloon(Troop):
    def __init__(self, key_pressed, village):
        super().__init__(3)
        self.aerial = True
        if(key_pressed == '4'):
            self.location = [village.spawning_points[0][0],village.spawning_points[0][1]+1]
        if(key_pressed == '5'):
            self.location = [village.spawning_points[1][0]+1,village.spawning_points[1][1]]
        if(key_pressed == '6'):
            self.location = [village.spawning_points[2][0],village.spawning_points[2][1]-1]
        
