import re
from .headers import *
from .troops import Troop,King,Barbarian,Archer,Balloon

# while creating object pass the coordinates of the spawning points
class Village():
    # initial map
    def __init__(self,spawn):
        self.height = SCREEN_HEIGHT
        self.width = SCREEN_WIDTH
        self.buildings = []
        self.troops = []
        self.spawning_points = spawn
        self.grid = []
        self.barbs_spawned = 0
        self.archers_spawned = 0
        self.balloons_spawned = 0
        self.heal_spell = 0
        self.rage_spell = 0
        self.rage_FLAG = 0
        # 1 for king, 4 for queen
        self.character = 0
        self.level = 0
        for x in range(0,self.height):
            self.grid.append([])
            for y in range(0,self.width):
                self.grid[x].append([' ',0])

        # self.grid = np.zeros((self.height,self.width))

        for x in range (0,self.height):
            self.grid[x][0] = ['X',1] # left border
            self.grid[x][self.width-1] = ['X',1] # right border
        for y in range (0,self.width):    
            self.grid[0][y] = ['X',1] # top border
            self.grid[self.height-1][y] = ['X',1] # bottom border
        self.grid[self.spawning_points[0][0]][self.spawning_points[0][1]] = ['7',1]
        self.grid[self.spawning_points[1][0]][self.spawning_points[1][1]] = ['8',1]
        self.grid[self.spawning_points[2][0]][self.spawning_points[2][1]] = ['9',1]
    
    def character_alive(self):
        if len(self.troops)>0 and self.troops[0].type == self.character:
            return True
        else:
            return False
    # 0 for green
    # 1 for white
    # 2 for yellow
    # 3 for red
    # 4 for magenta
    def render(self):
        os.system('clear')
        print("Level: ",self.level)
        for x in range(1,self.height-1):
            for y in range(1,self.width-1):
                self.grid[x][y] = [' ',0]
    
        for b in self.buildings:
            b.render(self)
        for t in self.troops:
            t.render(self)
        for x in range(0,self.height):
            for y in range(0,self.width):
                if(self.grid[x][y][1]==0):
                    print(Fore.GREEN+self.grid[x][y][0]+Style.RESET_ALL,end='')
                if(self.grid[x][y][1]==1):
                    print(Fore.WHITE+self.grid[x][y][0]+Style.RESET_ALL,end='')
                if(self.grid[x][y][1]==2):
                    print(Fore.YELLOW+self.grid[x][y][0]+Style.RESET_ALL,end='')
                if(self.grid[x][y][1]==3):
                    print(Fore.RED+self.grid[x][y][0]+Style.RESET_ALL,end='')
                if(self.grid[x][y][1]==4):
                    print(Fore.MAGENTA+self.grid[x][y][0]+Style.RESET_ALL,end='')
                if(self.grid[x][y][1]==5):
                    print(Fore.CYAN+self.grid[x][y][0]+Style.RESET_ALL,end='')
                if(self.grid[x][y][1]==6):
                    print(Fore.RED+self.grid[x][y][0]+Style.RESET_ALL,end='')   
            print()
        
        print()
        if(self.character == 1):
            print("King Health: ", end='')
        else:
            print("Queen Health: ", end='')
        if self.character_alive():
            h = self.troops[0].health//2
        else:
            h=0
        h = int(h)
        for x in range(h):
            print(Fore.GREEN+"█"+Style.RESET_ALL,end='')
        for x in range(50-h):
            print(Fore.RED+"█"+Style.RESET_ALL,end='')
        print()
        print("Barbarians remaining: ",MAX_BARBS - self.barbs_spawned)
        print("Archers remaining: ",MAX_ARCHERS - self.archers_spawned)
        print("Balloons remaining: ",MAX_BALLOONS - self.balloons_spawned)

    def move_character(self,direction):
        if(self.character_alive()==False):
            return
        self.troops[0].direction = direction
        if direction == 0:
            if(self.troops[0].location[0]>1 and (self.grid[self.troops[0].location[0]-1][self.troops[0].location[1]][0]==' ' or self.grid[self.troops[0].location[0]-1][self.troops[0].location[1]][0]=='B' or self.grid[self.troops[0].location[0]-1][self.troops[0].location[1]][0]=='A')):
                self.troops[0].location[0] -= 1
        if direction == 1:
            if(self.troops[0].location[1]>1 and (self.grid[self.troops[0].location[0]][self.troops[0].location[1]-1][0]==' ' or self.grid[self.troops[0].location[0]][self.troops[0].location[1]-1][0]=='B' or self.grid[self.troops[0].location[0]][self.troops[0].location[1]-1][0]=='A')):
                self.troops[0].location[1] -= 1
        if direction == 2:
            if(self.troops[0].location[0]<self.height-2 and (self.grid[self.troops[0].location[0]+1][self.troops[0].location[1]][0]==' ' or self.grid[self.troops[0].location[0]+1][self.troops[0].location[1]][0]=='B' or self.grid[self.troops[0].location[0]+1][self.troops[0].location[1]][0]=='A' )):
                self.troops[0].location[0] += 1
        if direction == 3:
            if(self.troops[0].location[1]<self.width-2 and (self.grid[self.troops[0].location[0]][self.troops[0].location[1]+1][0]==' ' or self.grid[self.troops[0].location[0]][self.troops[0].location[1]+1][0]=='B' or self.grid[self.troops[0].location[0]][self.troops[0].location[1]+1][0]=='A')):
                self.troops[0].location[1] += 1
    
    def spawn_barb(self,key_pressed):
        if(self.barbs_spawned < MAX_BARBS):
            self.troops.append(Barbarian(key_pressed,self))
            self.barbs_spawned += 1
    def spawn_archer(self,key_pressed):
        if(self.archers_spawned < MAX_ARCHERS):
            self.troops.append(Archer(key_pressed,self))
            self.archers_spawned += 1
    def spawn_balloon(self,key_pressed):
        if(self.balloons_spawned < MAX_BALLOONS):
            self.troops.append(Balloon(key_pressed,self))
            self.balloons_spawned += 1

    def cast_spell(self,key_pressed):
        if key_pressed==1 and self.heal_spell==0:
            self.heal_spell = 1
            for t in self.troops:
                t.health = min(1.5*t.health,100)
        if key_pressed==0 and self.rage_FLAG==0:
            self.rage_spell = 1
            self.rage_FLAG = 1

    def attack_king(self):
        if(self.character_alive()==False):
            return
        if(self.troops[0].direction == 0):
            if self.troops[0].location[0]>1 and self.grid[self.troops[0].location[0]-1][self.troops[0].location[1]][0]!=' ' and self.grid[self.troops[0].location[0]-1][self.troops[0].location[1]][0]!='B':
                self.damage(self.troops[0].location[0]-1,self.troops[0].location[1],self.troops[0].damage)
        if(self.troops[0].direction == 1):
            if self.troops[0].location[1]>1 and self.grid[self.troops[0].location[0]][self.troops[0].location[1]-1][0]!=' ' and self.grid[self.troops[0].location[0]][self.troops[0].location[1]-1][0]!='B':
                self.damage(self.troops[0].location[0],self.troops[0].location[1]-1,self.troops[0].damage)
        if(self.troops[0].direction == 2):
            if self.troops[0].location[0]<self.height-2 and self.grid[self.troops[0].location[0]+1][self.troops[0].location[1]][0]!=' ' and self.grid[self.troops[0].location[0]+1][self.troops[0].location[1]][0]!='B':
                self.damage(self.troops[0].location[0]+1,self.troops[0].location[1],self.troops[0].damage)
        if(self.troops[0].direction == 3):
            if self.troops[0].location[1]<self.width-2 and self.grid[self.troops[0].location[0]][self.troops[0].location[1]+1][0]!=' ' and self.grid[self.troops[0].location[0]][self.troops[0].location[1]+1][0]!='B':
                self.damage(self.troops[0].location[0],self.troops[0].location[1]+1,self.troops[0].damage)

    def attack_queen(self):
        if(self.character_alive()==False):
            return
        loc = self.troops[0].location
        for b in self.buildings:
            flag=0
            for x in range(b.location[0],b.location[0]+b.size[0]):
                for y in range(b.location[1],b.location[1]+b.size[1]):

                    if(self.troops[0].direction == 0):
                        for i in range(loc[0]-10,loc[0]-5):
                            for j in range(loc[1]-2,loc[1]+3):
                                if(i==x and j==y):
                                    self.damage(i,j,self.troops[0].damage)
                                    flag=1
                                    break
                            if flag==1:
                                break
                    if(self.troops[0].direction == 1):
                        for i in range(loc[0]-2,loc[0]+3):
                            for j in range(loc[1]-10,loc[1]-5):
                                if(i==x and j==y):
                                    self.damage(i,j,self.troops[0].damage)
                                    flag=1
                                    break
                            if flag==1:
                                break
                    if(self.troops[0].direction == 2):
                        for i in range(loc[0]+6,loc[0]+11):
                            for j in range(loc[1]-2,loc[1]+3):
                                if(i==x and j==y):
                                    self.damage(i,j,self.troops[0].damage)
                                    flag=1
                                    break
                            if flag==1:
                                break
                    if(self.troops[0].direction == 3):
                        for i in range(loc[0]-2,loc[0]+3):
                            for j in range(loc[1]+6,loc[1]+11):
                                if(i==x and j==y):
                                    self.damage(i,j,self.troops[0].damage)
                                    flag=1
                                    break
                            if flag==1:
                                break
                    if(flag==1):
                        break
                if flag==1:
                    break
        

    def attack_king_aoe(self):
        if(self.character_alive()==False):
            return
        if self.troops[0].location[0]>1 and self.grid[self.troops[0].location[0]-1][self.troops[0].location[1]][0]!=' ' and self.grid[self.troops[0].location[0]-1][self.troops[0].location[1]][0]!='B':
                self.damage(self.troops[0].location[0]-1,self.troops[0].location[1],self.troops[0].damage)    
        if self.troops[0].location[1]>1 and self.grid[self.troops[0].location[0]][self.troops[0].location[1]-1][0]!=' ' and self.grid[self.troops[0].location[0]][self.troops[0].location[1]-1][0]!='B':
                self.damage(self.troops[0].location[0],self.troops[0].location[1]-1,self.troops[0].damage)
        if self.troops[0].location[0]<self.height-2 and self.grid[self.troops[0].location[0]+1][self.troops[0].location[1]][0]!=' ' and self.grid[self.troops[0].location[0]+1][self.troops[0].location[1]][0]!='B':
                self.damage(self.troops[0].location[0]+1,self.troops[0].location[1],self.troops[0].damage)
        if self.troops[0].location[1]<self.width-2 and self.grid[self.troops[0].location[0]][self.troops[0].location[1]+1][0]!=' ' and self.grid[self.troops[0].location[0]][self.troops[0].location[1]+1][0]!='B':
                self.damage(self.troops[0].location[0],self.troops[0].location[1]+1,self.troops[0].damage)

    def attack_queen_aoe(self):
        attacks = []
        if(self.character_alive()==False):
            return [attacks,0]
        loc = self.troops[0].location
        for b in self.buildings:
            flag=0
            for x in range(b.location[0],b.location[0]+b.size[0]):
                for y in range(b.location[1],b.location[1]+b.size[1]):

                    if(self.troops[0].direction == 0):
                        for i in range(loc[0]-20,loc[0]-11):
                            for j in range(loc[1]-4,loc[1]+5):
                                if(i==x and j==y):
                                    attacks.append([i,j])
                                    flag=1
                                    break
                            if flag==1:
                                break
                    if(self.troops[0].direction == 1):
                        for i in range(loc[0]-4,loc[0]+5):
                            for j in range(loc[1]-20,loc[1]-11):
                                if(i==x and j==y):
                                    attacks.append([i,j])
                                    flag=1
                                    break
                            if flag==1:
                                break
                    if(self.troops[0].direction == 2):
                        for i in range(loc[0]+12,loc[0]+21):
                            for j in range(loc[1]-4,loc[1]+5):
                                if(i==x and j==y):
                                    attacks.append([i,j])
                                    flag=1
                                    break
                            if flag==1:
                                break
                    if(self.troops[0].direction == 3):
                        for i in range(loc[0]-4,loc[0]+5):
                            for j in range(loc[1]+12,loc[1]+21):
                                if(i==x and j==y):
                                    attacks.append([i,j])
                                    flag=1
                                    break
                            if flag==1:
                                break
                    if(flag==1):
                        break
                if flag==1:
                    break
        return [attacks,self.troops[0].damage]
    
    def move_attack_barbs(self):
        for barb in self.troops:
            if(barb.type!=0):
                continue
            nearest = [INF,[0,0]]
            for building in self.buildings:
                if(building.type==2):
                    continue
                if self.minimum_dist(barb,building)[0] < nearest[0]:
                    nearest = self.minimum_dist(barb,building)
                    
            if(nearest[0] == INF):
                continue
            if(abs(barb.location[0]-nearest[1][0])>=abs(barb.location[1]-nearest[1][1])):
                if(barb.location[0]-nearest[1][0]>0):
                    barb.direction = 0
                    if self.grid[barb.location[0]-1][barb.location[1]][0]==' ' or self.grid[barb.location[0]-1][barb.location[1]][0]=='B' or self.grid[barb.location[0]-1][barb.location[1]][0]=='K' or self.grid[barb.location[0]-1][barb.location[1]][0]=='Q' or self.grid[barb.location[0]-1][barb.location[1]][0]=='A' or self.grid[barb.location[0]-1][barb.location[1]][0]=='L':
                        barb.location[0]-=1
                    else:
                        self.damage(barb.location[0]-1,barb.location[1],barb.damage)
                else:
                    barb.direction = 2
                    if self.grid[barb.location[0]+1][barb.location[1]][0]==' ' or self.grid[barb.location[0]+1][barb.location[1]][0]=='B' or self.grid[barb.location[0]+1][barb.location[1]][0]=='K' or self.grid[barb.location[0]+1][barb.location[1]][0]=='Q' or self.grid[barb.location[0]+1][barb.location[1]][0]=='A' or self.grid[barb.location[0]+1][barb.location[1]][0]=='L':
                        barb.location[0]+=1
                    else:
                        self.damage(barb.location[0]+1,barb.location[1],barb.damage)
            else:
                if(barb.location[1]-nearest[1][1]>0):
                    barb.direction = 1
                    if self.grid[barb.location[0]][barb.location[1]-1][0]==' ' or self.grid[barb.location[0]][barb.location[1]-1][0]=='B' or self.grid[barb.location[0]][barb.location[1]-1][0]=='K' or self.grid[barb.location[0]][barb.location[1]-1][0]=='Q' or self.grid[barb.location[0]][barb.location[1]-1][0]=='A' or self.grid[barb.location[0]][barb.location[1]-1][0]=='L':
                        barb.location[1]-=1
                    else:
                        self.damage(barb.location[0],barb.location[1]-1,barb.damage)
                else:
                    barb.direction = 3
                    if self.grid[barb.location[0]][barb.location[1]+1][0]==' ' or self.grid[barb.location[0]][barb.location[1]+1][0]=='B' or self.grid[barb.location[0]][barb.location[1]+1][0]=='K' or self.grid[barb.location[0]][barb.location[1]+1][0]=='Q' or self.grid[barb.location[0]][barb.location[1]+1][0]=='A' or self.grid[barb.location[0]][barb.location[1]+1][0]=='L':
                        barb.location[1]+=1
                    else:
                        self.damage(barb.location[0],barb.location[1]+1,barb.damage)
        return
    
    def move_attack_archers(self):
        for archer in self.troops:
            if archer.type!=2:
                continue
            nearest = [INF,[0,0]]
            for building in self.buildings:
                if(building.type==2):
                    continue
                if self.minimum_dist(archer,building)[0] < nearest[0]:
                    nearest = self.minimum_dist(archer,building)
                    
            if(nearest[0] == INF):
                continue
            if nearest[0]<=ARCHER_RANGE:
                self.damage(nearest[1][0],nearest[1][1],archer.damage)
                continue
            if(abs(archer.location[0]-nearest[1][0])>=abs(archer.location[1]-nearest[1][1])):
                if(archer.location[0]-nearest[1][0]>0):
                    archer.direction = 0
                    if self.grid[archer.location[0]-1][archer.location[1]][0]==' ' or self.grid[archer.location[0]-1][archer.location[1]][0]=='B' or self.grid[archer.location[0]-1][archer.location[1]][0]=='K' or self.grid[archer.location[0]-1][archer.location[1]][0]=='Q' or self.grid[archer.location[0]-1][archer.location[1]][0]=='A' or self.grid[archer.location[0]-1][archer.location[1]][0]=='L':
                        archer.location[0]-=1
                    else:
                        self.damage(archer.location[0]-1,archer.location[1],archer.damage)
                else:
                    archer.direction = 2
                    if self.grid[archer.location[0]+1][archer.location[1]][0]==' ' or self.grid[archer.location[0]+1][archer.location[1]][0]=='B' or self.grid[archer.location[0]+1][archer.location[1]][0]=='K' or self.grid[archer.location[0]+1][archer.location[1]][0]=='Q' or self.grid[archer.location[0]+1][archer.location[1]][0]=='A' or self.grid[archer.location[0]+1][archer.location[1]][0]=='L':
                        archer.location[0]+=1
                    else:
                        self.damage(archer.location[0]+1,archer.location[1],archer.damage)
            else:
                if(archer.location[1]-nearest[1][1]>0):
                    archer.direction = 1
                    if self.grid[archer.location[0]][archer.location[1]-1][0]==' ' or self.grid[archer.location[0]][archer.location[1]-1][0]=='B' or self.grid[archer.location[0]][archer.location[1]-1][0]=='K' or self.grid[archer.location[0]][archer.location[1]-1][0]=='Q' or self.grid[archer.location[0]][archer.location[1]-1][0]=='A' or self.grid[archer.location[0]][archer.location[1]-1][0]=='L':
                        archer.location[1]-=1
                    else:
                        self.damage(archer.location[0],archer.location[1]-1,archer.damage)
                else:
                    archer.direction = 3
                    if self.grid[archer.location[0]][archer.location[1]+1][0]==' ' or self.grid[archer.location[0]][archer.location[1]+1][0]=='B' or self.grid[archer.location[0]][archer.location[1]+1][0]=='K' or self.grid[archer.location[0]][archer.location[1]+1][0]=='Q' or self.grid[archer.location[0]][archer.location[1]+1][0]=='A' or self.grid[archer.location[0]][archer.location[1]+1][0]=='L':
                        archer.location[1]+=1
                    else:
                        self.damage(archer.location[0],archer.location[1]+1,archer.damage)
        return

    def move_attack_balloons(self):
        for balloon in self.troops:
            if balloon.type!=3:
                continue
            nearest = [INF,[0,0]]
            for building in self.buildings:
                if(building.type==2):
                    continue
                if self.minimum_dist(balloon,building)[0] < nearest[0] and (building.type==3 or building.type==4):
                    nearest = self.minimum_dist(balloon,building)
            if(nearest[0] == INF):
                for building in self.buildings:
                    if(building.type==2):
                        continue
                    if self.minimum_dist(balloon,building)[0] < nearest[0]:
                        nearest = self.minimum_dist(balloon,building)
            if(nearest[0] == INF):
                continue
            if(nearest[0] <= 1):
                self.damage(nearest[1][0],nearest[1][1],balloon.damage)
                continue
            if (abs(balloon.location[0]-nearest[1][0])>=abs(balloon.location[1]-nearest[1][1])):
                if(balloon.location[0]-nearest[1][0]>0):
                    balloon.direction = 0
                    balloon.location[0]-=1
                else:
                    balloon.direction = 2
                    balloon.location[0]+=1
            else:
                if(balloon.location[1]-nearest[1][1]>0):
                    balloon.direction = 1
                    balloon.location[1]-=1
                else:
                    balloon.direction = 3
                    balloon.location[1]+=1
        return

    def fire_cannons(self):
        for c in self.buildings:
            if c.type != 3:
                continue
            d = INF
            for i in range(0,self.troops.__len__()):
                if self.troops[i].aerial:
                    continue
                if self.minimum_dist(self.troops[i],c)[0] < d:
                    d = self.minimum_dist(self.troops[i],c)[0]
                    t = i
            if d > CANNON_RANGE:
                continue
            os.system('aplay -q ./src/sounds/cannon.wav&')
            self.troops[t].health -= c.damage

    def fire_towers(self):
        for c in self.buildings:
            if c.type != 4:
                continue
            d = INF
            for i in range(0,self.troops.__len__()):
                if self.minimum_dist(self.troops[i],c)[0] < d:
                    d = self.minimum_dist(self.troops[i],c)[0]
                    t = i
            if d > TOWER_RANGE:
                continue
            centre = self.troops[t].location
            for i in range(0,self.troops.__len__()):
                if abs(centre[0]-self.troops[i].location[0])<=1 and abs(centre[1]-self.troops[i].location[1])<=1:
                    self.troops[i].health -= c.damage
        return

    def damage(self,x,y,damage):
        for b in self.buildings:
            if x>=b.location[0] and x<b.location[0]+b.size[0] and y>=b.location[1] and y<b.location[1]+b.size[1]:
                os.system('aplay -q ./src/sounds/attack.wav&')
                b.health -= damage
    
    def minimum_dist(self,t,b):
        d1 = INF
        d2 = INF
        x = INF
        y = INF
        for i in range(b.location[0],b.location[0]+b.size[0]):
            if abs(t.location[0]-i)<d1:
                d1 = abs(t.location[0]-i)
                x = i
        for i in range(b.location[1],b.location[1]+b.size[1]):
            if abs(t.location[1]-i)<d2:
                d2 = abs(t.location[1]-i)
                y = i
        return [d1+d2,[x,y]]