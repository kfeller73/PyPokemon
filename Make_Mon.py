# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 12:19:01 2021

@author: Keyton Feller
"""
import numpy as np
import pandas as pd
import time 
from Natures import Nat
import Moves

pokelist = pd.read_csv('Poke_mon.csv')
moves = pd.read_csv('Poke_moves.csv')

class Pokemon:
    stages = np.array
    def __init__(self, name, level, IV, EV, nature, moveset):
        self.name = name
        stats = pokelist.loc[pokelist['Name'] == name].iloc[0]
        self.type = [stats[2],stats[3]]
        self.level = level
        self.nature = nature
        nature = Nat(nature)
        self.Total = stats[4]
        self.HP =  int((2 * stats[5] + IV[0] + int(EV[0]/4)) * level/100) + level + 10
        
        self.Atk_Stage = 0 
        self.Def_Stage = 0
        self.Sp_Atk_Stage = 0
        self.Sp_Def_Stage = 0 
        self.Speed_Stage = 0 
        self.Accuracy_Stage = 0
        self.Evasion_Stage = 0
        
        stage = np.array([0.25, 0.28, 0.33, 0.40, 0.50, 0.66, 1.0, 1.50, 2, 2.5, 3, 3.5, 4])
        Prob_stage = np.array([0.33, 0.36, 0.43, 0.50, 0.60, 0.75, 1, 1.33, 1.66, 2, 2.5, 2.66, 3])
        
        Atk = int(int(2 * stats[6] + IV[1] + int(EV[1]/4) * level/100) + 5*nature[0])
        Def = int(int(2 * stats[7] + IV[2] + int(EV[2]/4) * level/100) + 5*nature[1])
        Sp_Atk = int(int(2 * stats[8] + IV[3] + int(EV[3]/4) * level/100) + 5*nature[2])
        Sp_Def = int(int(2 * stats[9] + IV[4] + int(EV[4]/4) * level/100) + 5*nature[3])
        Speed = int(int(2 * stats[10] + IV[5] + int(EV[5]/4) * level/100) + 5*nature[4])
        Accuracy = 100
        Evasion = 100
        
        self.Atk = Atk * stage[self.Atk_Stage+6]
        self.Def = Def * stage[self.Def_Stage+6]
        self.Sp_Atk = Sp_Atk * stage[self.Sp_Atk_Stage+6]
        self.Sp_Def = Sp_Def * stage[self.Sp_Def_Stage+6]
        self.Speed = Speed * stage[self.Speed_Stage+6]
        self.Accuracy = Accuracy * Prob_stage[self.Accuracy_Stage+6]
        self.Evasion = Evasion * Prob_stage[self.Evasion_Stage+6]
        
        
        self.moveset = moveset
        self.status = 'none'
        self.location = 'Surface'
    
    def IV(self):
        pass
    def EV(self):
        pass
    def stat_change(self, stat, stage):
        pass