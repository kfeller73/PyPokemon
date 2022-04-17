# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 09:03:57 2021

@author: Keyton Feller
"""

import numpy as np
import pandas as pd
from Checks import Damage


### Normal Moves
class Pound:
    def __init__(self):
        self.name = 'Pound'
        self.Etype = 'Normal'
        self.power = 40
        self.Mtype = 'Physical'
        self.Crit = 0.0625
        self.Priority = 0
        self.PP = 35
        self.Accuracy = 100
    def attack(mon1, self, mon2):
        damage = Damage(mon1, self, mon2)
        mon2.HP = mon2.HP - damage
        return
    
class Double_Slap:
    def __init__(self):
        self.name = 'Double Slap'
        self.Etype = 'Normal'
        self.power = 15
        self.Mtype = 'Physical'
        self.Crit = 0.0625
        self.Priority = 0
        self.PP = 10
        self.Accuracy = 85
    def attack(mon1, self, mon2):
        hits = np.random.choice([2,3,4,5], 1, p=[0.375, 0.375, 0.125, 0.125])
        for _ in range(hits):
            damage = Damage(mon1, self, mon2)
            if damage == 0:
                break
            else:
                mon2.HP = mon2.HP - damage
        return    

# Flinching move
class Stomp:
    def __init__(self):
        self.name = 'Stomp'
        self.Etype = 'Normal'
        self.power = 65
        self.Mtype = 'Physical'
        self.Crit = 0.0625
        self.Priority = 0
        self.PP = 35
        self.Accuracy = 100
        self.Effect = 'Flinch'
    def attack(mon1, self, mon2):
        damage = Damage(mon1, self, mon2)
        mon2.HP = mon2.HP - damage
        mon2.Status = np.random.choice([self.Effect,'none'], 1, p=[self.Effect_Chance,1-self.Effect_Chance])
        return    



class Karate_Chop:
    def __init__(self):
        self.name = 'Karate Chop'
        self.Etype = 'Fighting'
        self.power = 50
        self.Mtype = 'Physical'
        self.Crit = 0.125
        self.Priority = 0
        self.PP = 25
        self.Accuracy = 100
    def attack(mon1, self, mon2):
        damage = Damage(mon1, self, mon2)
        mon2.HP = mon2.HP - damage
        return damage
  
class Double_Kick:
    def __init__(self):
        self.name = 'Double Kick'
        self.Etype = 'Normal'
        self.power = 15
        self.Mtype = 'Physical'
        self.Crit = 0.0625
        self.Priority = 0
        self.PP = 10
        self.Accuracy = 85
    def attack(mon1, self, mon2):
        damage = Damage(mon1, self, mon2)
        mon2.HP += -damage
        self.Crit = 0
        damage = Damage(mon1, self, mon2)
        return    
  
class Comet_Punch:
    # not completely right but its pretty close
    # damage should be the same if i > 0
    def __init__(self):
        self.name = 'Comet Punch'
        self.Etype = 'Normal'
        self.power = 18
        self.Mtype = 'Physical'
        self.Crit = 0.0625
        self.Priority = 0
        self.PP = 15
        self.Accuracy = 85
    def attack(mon1, self, mon2):
        hits = np.random.choice([2,3,4,5], 1, p=[0.375, 0.375, 0.125, 0.125])
        for i in range(hits):
            if i == 0:
                damage = Damage(mon1, self, mon2)
                mon2.HP = mon2.HP - damage
                self.Crit = 0
            else:
                damage = Damage(mon1, self, mon2)
                mon2.HP = mon2.HP - damage
            if damage == 0:
                break
        return
    
class Mega_Punch:
    def __init__(self):
        self.name = 'Mega Punch'
        self.Etype = 'Normal'
        self.power = 80
        self.Mtype = 'Physical'
        self.Crit = 0.0625
        self.Priority = 0
        self.PP = 20
        self.Accuracy = 85
    def attack(mon1, self, mon2):
        damage = Damage(mon1, self, mon2)
        mon2.HP = mon2.HP - damage
        return
    
class Fire_Punch:
    def __init__(self):
        self.name = 'Fire Punch'
        self.Etype = 'Fire'
        self.power = 75
        self.Mtype = 'Physical'
        self.Crit = 0.0625
        self.Priority = 0
        self.PP = 15
        self.Accuracy = 100
        self.Effect_Chance = 0.1
        self.Effect = 'Burn'
    def attack(mon1, self, mon2):
        damage = Damage(mon1, self, mon2)
        mon2.HP = mon2.HP - damage
        mon2.Status = np.random.choice([self.Effect,'none'], 1, p=[self.Effect_Chance,1-self.Effect_Chance])
        return    

class Ice_Punch:
    def __init__(self):
        self.name = 'Ice Punch'
        self.Etype = 'Ice'
        self.power = 75
        self.Mtype = 'Physical'
        self.Crit = 0.0625
        self.Priority = 0
        self.PP = 15
        self.Accuracy = 100
        self.Effect_Chance = 0.1
        self.Effect = 'Freeze'
    def attack(mon1, self, mon2):
        damage = Damage(mon1, self, mon2)
        mon2.HP = mon2.HP - damage
        mon2.Status = np.random.choice([self.Effect,'none'], 1, p=[self.Effect_Chance,1-self.Effect_Chance])
        return           

class Thunder_Punch:
    def __init__(self):
        self.name = 'Thunder Punch'
        self.Etype = 'Electric'
        self.power = 75
        self.Mtype = 'Physical'
        self.Crit = 0.0625
        self.Priority = 0
        self.PP = 15
        self.Accuracy = 100
        self.Effect_Chance = 0.1
        self.Effect = 'Paralysis'
    def attack(mon1, self, mon2):
        damage = Damage(mon1, self, mon2)
        mon2.HP = mon2.HP - damage
        mon2.Status = np.random.choice([self.Effect,'none'], 1, p=[self.Effect_Chance,1-self.Effect_Chance])
        return           
        
class Scratch:
    def __init__(self):
        self.name = 'Scratch'
        self.Etype = 'Normal'
        self.power = 40
        self.Mtype = 'Physical'
        self.Crit = 0.0625
        self.Priority = 0
        self.PP = 35
        self.Accuracy = 100
    def attack(mon1, self, mon2):
        damage = Damage(mon1, self, mon2)
        mon2.HP = mon2.HP - damage
        return
    
class Vice_Grip:
    def __init__(self):
        self.name = 'Vice Grip'
        self.Etype = 'Normal'
        self.power = 55
        self.Mtype = 'Physical'
        self.Crit = 0.0625
        self.Priority = 0
        self.PP = 30
        self.Accuracy = 100
    def attack(mon1, self, mon2):
        damage = Damage(mon1, self, mon2)
        mon2.HP = mon2.HP - damage
        return

class Guillotine:
    def __init__(self):
        self.name = 'Guillotine'
        self.Etype = 'Normal'
        self.power = 40
        self.Mtype = 'Physical'
        self.Crit = 0.0625
        self.Priority = 0
        self.PP = 5
        self.Accuracy = 30
    def attack(mon1, self, mon2):
        damage = Damage(mon1, self, mon2)
        if damage > 0:
            damage = mon2.HP
            mon2.HP = mon2.HP - damage            
        return

# Needs work to be turn dependent
class Razor_Wind:
    def __init__(self):
        self.name = 'Razor Wind'
        self.Etype = 'Normal'
        self.power = 80
        self.Mtype = 'Physical'
        self.Crit = 0.0625
        self.Priority = 0
        self.PP = 10
        self.Accuracy = 100 
        self.Turn = 2
    def attack(mon1, self, mon2):
        damage = Damage(mon1, self, mon2)
        mon2.HP = mon2.HP - damage
        return

class Swords_Dance:
    def __init__(self):
        self.name = 'Swords Dance'
        self.Etype = 'Normal'
        self.power = 0
        self.Mtype = 'Status'
        self.Crit = 0
        self.Priority = 0
        self.PP = 20
        self.Accuracy = 100
    def attack(mon1, self, mon2):
        mon1.Atk_Stage += 2
        return

class Cut:
    def __init__(self):
        self.name = 'Cut'
        self.Etype = 'Normal'
        self.power = 50
        self.Mtype = 'Physical'
        self.Crit = 0.0625
        self.Priority = 0
        self.PP = 30
        self.Accuracy = 100
    def attack(mon1, self, mon2):
        damage = Damage(mon1, self, mon2)
        mon2.HP = mon2.HP - damage
        return

class Gust:
    def __init__(self):
        self.name = 'Gust'
        self.Etype = 'Flying'
        self.power = 40
        self.Mtype = 'Special'
        self.Crit = 0.0625
        self.Priority = 0
        self.PP = 35
        self.Accuracy = 100
    def attack(mon1, self, mon2):
        damage = Damage(mon1, self, mon2)
        mon2.HP = mon2.HP - damage
        return

class Wing_Attack:
    def __init__(self):
        self.name = 'Wing Attack'
        self.Etype = 'Flying'
        self.power = 60
        self.Mtype = 'Physical'
        self.Crit = 0.0625
        self.Priority = 0
        self.PP = 35
        self.Accuracy = 100
    def attack(mon1, self, mon2):
        damage = Damage(mon1, self, mon2)
        mon2.HP = mon2.HP - damage
        return

# Another turn dependent move
class Fly:
    def __init__(self):
        self.name = 'Fly'
        self.Etype = 'Flying'
        self.power = 90
        self.Mtype = 'Physical'
        self.Crit = 0.0625
        self.Priority = 0
        self.PP = 15
        self.Accuracy = 95
    def attack(mon1, self, mon2):
        damage = Damage(mon1, self, mon2)
        mon2.HP = mon2.HP - damage
        return

# Another turn dependent move
class Bind:
    def __init__(self):
        self.name = 'Bind'
        self.Etype = 'Normal'
        self.power = 15
        self.Mtype = 'Physical'
        self.Crit = 0.0625
        self.Priority = 0
        self.PP = 20
        self.Accuracy = 85
    def attack(mon1, self, mon2):
        hits = np.random.choice([2,3,4,5], 1, p=[0.375, 0.375, 0.125, 0.125])
        for i in range(hits):
            if i == 0:
                damage = Damage(mon1, self, mon2)
                mon2.HP = mon2.HP - damage
                self.Crit = 0
            else:
                damage = Damage(mon1, self, mon2)
                mon2.HP = mon2.HP - damage
            if damage == 0:
                break
        return

class Slam:
    def __init__(self):
        self.name = 'Slam'
        self.Etype = 'Normal'
        self.power = 80
        self.Mtype = 'Physical'
        self.Crit = 0.0625
        self.Priority = 0
        self.PP = 20
        self.Accuracy = 75
    def attack(mon1, self, mon2):
        damage = Damage(mon1, self, mon2)
        mon2.HP = mon2.HP - damage
        return damage

class Vine_Whip:
    def __init__(self):
        self.name = 'Vine Whip'
        self.Etype = 'Grass'
        self.power = 45
        self.Mtype = 'Physical'
        self.Crit = 0.0625
        self.Priority = 0
        self.PP = 25
        self.Accuracy = 100
    def attack(mon1, self, mon2):
        damage = Damage(mon1, self, mon2)
        mon2.HP = mon2.HP - damage
        return





# Pound
# -type, power,phy/spec, priority, effect
    
