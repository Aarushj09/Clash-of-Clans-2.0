import os
from posixpath import split
import sys
from time import sleep
from src.headers import *
from src.utility import *
from src.input import *

os.system('clear')

file = open(f"replays/{sys.argv[1]}", "r")
file_data = file.read().split('\n')
file.close()

file = open(f"replays/{len(os.listdir('./replays')) + 1}.txt", "w")
village = Village([[SCREEN_HEIGHT//3,0],[0,SCREEN_WIDTH//2],[2*SCREEN_HEIGHT//3,SCREEN_WIDTH-1]])
initialise_village_1(village)
village.level=1
inputt = 1
it1 = 0
it2 = 0
it3 = 0
it_archer = 0
it_balloon = 0
it_tower = 0
level = 1

while True:
    print("Press 0 for King, 1 for Queen: ",end="")
    character = str(file_data[0])
    print(character)
    if(character == '0'):
        village.troops.append(King())
        village.character = 1
        break
    elif(character == '1'):
        village.troops.append(Queen())
        village.character = 4
        break
    else:
        print("Enter valid input!!")



while True:
    sleep(0.1)
    it1+=1
    it2+=1
    it_archer+=2
    it_balloon+=2
    it_tower+=1
    if village.rage_spell==1:
        it3+=1

    for x in village.buildings:
        if x.health <= 0:
            village.buildings.remove(x)
    for x in village.troops:
        if x.health <= 0:
            village.troops.remove(x)

    village.render()
    if(it3>100):
        village.rage_spell = 0
        it3 = 0


    result = game_over(village)
    if result!=-1:
        if result == 0:
            break
        if level==1:
            level = 2
            village = Village([[SCREEN_HEIGHT//3,0],[0,SCREEN_WIDTH//2],[2*SCREEN_HEIGHT//3,SCREEN_WIDTH-1]])
            initialise_village_2(village)
            village.level=2
            if(character == '0'):
                village.troops.append(King())
                village.character = 1
                
            elif(character == '1'):
                village.troops.append(Queen())
                village.character = 4
        elif level==2:
            level = 3
            village = Village([[SCREEN_HEIGHT//3,0],[0,SCREEN_WIDTH//2],[2*SCREEN_HEIGHT//3,SCREEN_WIDTH-1]])
            initialise_village_3(village)
            village.level=3
            if(character == '0'):
                village.troops.append(King())
                village.character = 1
            elif(character == '1'):
                village.troops.append(Queen())
                village.character = 4
        elif level==3:
            break
        # break

    # print(file_data)
    # print(input)
    # print(file_data[input])
    inp = str(file_data[inputt])
    inputt+=1
    # print(inp)
    if(inp != None):
        handle_input(inp,village)

    if(it1 >= 10/(village.rage_spell+1)):
        village.move_attack_barbs()
        it1 = 0
    if(it_archer >= 10/(village.rage_spell+1)):
        village.move_attack_archers()
        it_archer = 0
    if(it_balloon >= 10/(village.rage_spell+1)):
        village.move_attack_balloons()
        it_balloon = 0
    if(it2 >= 10):
        village.fire_cannons()
        it2 = 0
    if(it_tower>=10):
        village.fire_towers()
        it_tower = 0


if(result == 0):
    defeat()
else:
    victory()
