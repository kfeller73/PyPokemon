# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 10:27:12 2020

@author: keyto
"""
import numpy as np
import pandas as pd
import time 
import os
os.chdir(r'C:\Users\Keyton Feller\Desktop\PyPokemon')
from Natures import Nat
import Moves
from Make_Mon import Pokemon


    

IV = [0,0,0,0,0,0]
EV = [0,0,0,0,0,0]
nature = [1,1,1,1,1,1]
mon1 = Pokemon('Pikachu', 50, IV, EV, 'none', [Moves.Pound()])
mon2 = Pokemon('Pidgey', 50, IV, EV, 'none', [Moves.Pound()])

while mon1.HP > 0 and mon2.HP > 0:
    # ability check (intimidate, etc)
    # weather check?
    # speed check for priority mon
    # status check
    # fast mon attack
    # attack effects (should happen in step before)
    #








