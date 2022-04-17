# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 10:21:34 2021

@author: Keyton Feller
"""

import numpy as np
import pandas as pd
def Type_Check(move, mon2):
    chart = pd.read_csv('Type_Chart.csv')
    move_loc = np.where(chart['Types'] == move.Etype)
    mon_loc1 = np.where(chart['Types'] == mon2.Type[0])
    mon_loc2 = 1
    if len(mon2.Type) == 2:
        mon_loc2 = np.where(chart['Types'] == mon2.Type[1])
    chart = np.array(chart.iloc[:,1:])
    Type = chart[move_loc,mon_loc1] * chart[move_loc,mon_loc2]
    return Type

def Weather_Check(move, Battle):
    if Battle.weather == 'Harsh Sunlight' and move.Etype == 'Fire':
        Weather = 1.5
    if Battle.weather == 'Harsh Sunlight' and move.Etype == 'Water':
        Weather = 0.5
    if Battle.weather == 'Rain' and move.Etype == 'Fire':
        Weather = 0.5
    if Battle.weather == 'Rain' and move.Etype == 'Water':
        Weather = 1.5
    else:
        Weather = 1
    return Weather
    

def Dam_Mod(mon1, move, mon2, Battle):
    Crit = np.random.choice([2,1],1,p=[move.Crit, 1-move.Crit])
    Rand = np.random.uniform(low=0.85, high=1, size=1)
    STAB = 1
    if mon1.Type[0] == move.Etype or mon1.Type[1] == move.Etype:
        STAB = 2
    Type = Type_Check(move, mon2)
    Burn = 1
    if mon1.Status == 'Burn' and move.Mtype == 'Physical':
        Burn = 0.5
    Weather = Weather_Check(move, Battle)
    Mod = Crit * Rand * STAB * Type * Burn * Weather
    return Mod

def Damage(mon1, move, mon2):
    T = move.Accuracy * mon1.Accuracy / mon2.Evasion
    rand = np.random.uniform(low=1, high=100, size=1)
    if rand > T:
        Damage = 0
        print(f'{move.name} missed!')
        return Damage
    Mod = float(Dam_Mod(mon1, move, mon2))
    if move.Mtype == 'Physical':
        Damage = ((((2*mon1.level/5)+2) * move.power * mon1.Atk / mon2.Def / 50) + 2) * Mod
    if move.Mtype == 'Special': 
        Damage = ((((2*mon1.level/5)+2) * move.power * mon1.Sp_Atk / mon2.Sp_Def / 50) + 2) * Mod
    return int(Damage)

def Priority_Check():
    pass
    




