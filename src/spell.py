import imp

from src.village import Village
from .headers import *

class Spell():

    def action(self,village):
        pass
    
class Rage(Spell):
    
    def action(self,village):
        if village.rage_FLAG==0:
            village.rage_spell = 1
            village.rage_FLAG = 1

class Heal(Spell):
    
    def action(self,village):
        if village.heal_spell==0:
            village.heal_spell = 1
            for troop in village.troops:
                troop.health = min(1.5*troop.health,100)