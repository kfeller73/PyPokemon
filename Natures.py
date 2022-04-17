# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 21:40:06 2021

@author: Keyton Feller
"""
import numpy as np
        
def Nat(nature):
    if nature == 'Adamant':
        return np.array([1.1, 1.0, 0.9, 1.0, 1.0])
    if nature == 'Brave':
        return np.array([1.1, 1.0, 1.0, 1.0, 0.9])
    if nature == 'Lonely':
        return np.array([1.1, 0.9, 1.0, 1.0, 1.0])
    if nature == 'Naughty':
        return np.array([1.1, 1.0, 1.0, 0.9, 1.0])
    if nature == 'Bold':
        return np.array([0.9, 1.1, 1.0, 1.0, 1.0])
    if nature == 'Impish':
        return np.array([1.0, 1.1, 0.9, 1.0, 1.0])
    if nature == 'Lax':
        return np.array([1.0, 1.1, 1.0, 0.9, 1.0])
    if nature == 'Relaxed':
        return np.array([1.0, 1.1, 1.0, 1.0, 0.9])
    if nature == 'Mild':
        return np.array([1.0, 0.9, 1.1, 1.0, 1.0])
    if nature == 'Modest':
        return np.array([0.9, 1.0, 1.1, 1.0, 1.0])
    if nature == 'Quiet':
        return np.array([1.0, 1.0, 1.1, 1.0, 0.9])
    if nature == 'Rash':
        return np.array([1.0, 1.0, 1.1, 0.9, 1.0])
    if nature == 'Calm':
        return np.array([1.0, 1.0, 0.9, 1.1, 1.0])
    if nature == 'Careful':
        return np.array([1.0, 1.0, 0.9, 1.1, 1.0])
    if nature == 'Gentle':
        return np.array([1.0, 0.9, 1.0, 1.1, 1.0])
    if nature == 'Sassy':
        return np.array([1.0, 1.0, 1.0, 1.1, 0.9])
    if nature == 'Hasty':
        return np.array([1.0, 0.9, 1.0, 1.0, 1.1])
    if nature == 'Jolly':
        return np.array([1.0, 1.0, 0.9, 1.0, 1.1])
    if nature == 'Naive':
        return np.array([1.0, 1.0, 1.0, 0.9, 1.1])
    if nature == 'Timid':
        return np.array([0.9, 1.0, 1.0, 1.0, 1.1])
    else:
        return np.array([1.0, 1.0, 1.0, 1.0, 1.0])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        