from .headers import * 
from .village import Village
from .buildings import Building,Town_hall,Hut,Wall, Cannon, Wizard_Tower
from .troops import Troop,King,Barbarian,Queen
from .spell import Spell,Rage,Heal
import time

def initialise_village_1(village):
    village.buildings.append(Town_hall([SCREEN_HEIGHT//2,SCREEN_WIDTH//2]))
    village.buildings.append(Hut([25,15]))
    village.buildings.append(Hut([10,30]))
    village.buildings.append(Hut([8,70]))
    village.buildings.append(Hut([20,80]))
    village.buildings.append(Hut([30,60]))
    village.buildings.append(Cannon([15,32]))
    village.buildings.append(Cannon([10,75]))
    village.buildings.append(Wizard_Tower([8,50]))
    village.buildings.append(Wizard_Tower([30,40]))

    for x in range(15,25):
        village.buildings.append(Wall([x,43]))
        village.buildings.append(Wall([x,60]))
    for x in range(43,61):
        village.buildings.append(Wall([15,x]))
        village.buildings.append(Wall([24,x]))
    
def initialise_village_2(village):
    village.buildings.append(Town_hall([SCREEN_HEIGHT//2,SCREEN_WIDTH//2]))
    village.buildings.append(Hut([25,15]))
    village.buildings.append(Hut([10,30]))
    village.buildings.append(Hut([8,70]))
    village.buildings.append(Hut([20,80]))
    village.buildings.append(Hut([30,60]))
    village.buildings.append(Cannon([20,32]))
    village.buildings.append(Cannon([10,75]))
    village.buildings.append(Cannon([12,60]))
    village.buildings.append(Wizard_Tower([8,50]))
    village.buildings.append(Wizard_Tower([30,40]))
    village.buildings.append(Wizard_Tower([25,75]))

    for x in range(15,25):
        village.buildings.append(Wall([x,43]))
        village.buildings.append(Wall([x,60]))
    for x in range(43,61):
        village.buildings.append(Wall([15,x]))
        village.buildings.append(Wall([24,x]))
    
def initialise_village_3(village):
    village.buildings.append(Town_hall([SCREEN_HEIGHT//2,SCREEN_WIDTH//2]))
    village.buildings.append(Hut([25,15]))
    village.buildings.append(Hut([10,30]))
    village.buildings.append(Hut([8,70]))
    village.buildings.append(Hut([20,80]))
    village.buildings.append(Hut([30,60]))
    village.buildings.append(Cannon([20,32]))
    village.buildings.append(Cannon([10,75]))
    village.buildings.append(Cannon([27,64]))
    village.buildings.append(Wizard_Tower([8,50]))
    village.buildings.append(Wizard_Tower([30,40]))
    village.buildings.append(Wizard_Tower([25,75]))
    village.buildings.append(Wizard_Tower([20,18]))

    for x in range(15,25):
        village.buildings.append(Wall([x,43]))
        village.buildings.append(Wall([x,60]))
    for x in range(43,61):
        village.buildings.append(Wall([15,x]))
        village.buildings.append(Wall([24,x]))
    

def handle_input(key,village):
    if(key=='w' or key=='W'):
        village.move_character(0)
    if(key=='a' or key=='A'):
        village.move_character(1)
    if(key=='s' or key=='S'):
        village.move_character(2)
    if(key=='d' or key=='D'):
        village.move_character(3)

    if(key=='1' or key=='2' or key=='3'):
        village.spawn_archer(key)
    if(key=='4' or key=='5' or key=='6'):
        village.spawn_balloon(key)
    if(key=='7' or key=='8' or key=='9'):
        village.spawn_barb(key)
    
    if(key=='r' or key=='R'):
        rage = Rage()
        rage.action(village)
    if(key=='h' or key=='H'):
        heal = Heal()
        heal.action(village)

    if(key==' '):
        if(village.character == 1):
            village.attack_king()
        else:
            village.attack_queen()
    if(key=='l' or key=='L'):
        if(village.character == 1):
            village.attack_king_aoe()
        else:
            attacks = village.attack_queen_aoe()
            time.sleep(1)
            for attack in attacks[0]:
                village.damage(attack[0],attack[1],attacks[1])


    if(key == 'e' or key == 'E'):
        exit()

def game_over(village):
    t_flag = 0
    b_flag = 0
    for troop in village.troops:
        if troop.health > 0:
            t_flag = 1
            break
    for building in village.buildings:
        if building.health > 0 and building.type != 2:
            b_flag = 1
            break
    if t_flag == 1 and b_flag == 1:
        return -1
    if b_flag == 0:
        return 1
    if t_flag == 0:
        return 0

def victory():
    # os.system('clear')
    os.system('aplay -q ./src/sounds/win.wav&')
    print("Game Over")
    print("You win!")

def defeat():
    # os.system('clear')
    os.system('aplay -q ./src/sounds/defeat.wav&')
    print("Game Over")
    print("You lose!")