# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 10:17:41 2018

@author: hh
"""

import numpy as np
from sympy import *


from _TestFunction import problem  


class GradientDescent(object):
    def __init__(self,alpha = 0.01):
        self.alpha = alpha 
        self.X_LIST = []
        self.Y_LIST = []
        self.Z_LIST = []
        self.x_range = 0
        self.y_range = 0
    
    def run(self,prob):
        
        func = prob.getprob()
        X = prob.X
        Y = prob.Y
        
        dZx = func.diff(X)
        dZy = func.diff(Y)
        
        f_dZx = lambdify((X,Y), dZx)
        f_dZy = lambdify((X,Y), dZy)
        f_func = lambdify((X,Y), func)
        
        x = np.random.randint(prob.x_rang[0],prob.x_rang[1])
        y = np.random.randint(prob.y_rang[0],prob.y_rang[1])        
        
        for i in range(1000):
            z = f_func(x,y)
            temp_X = x-self.alpha*f_dZx(x,y)
            temp_Y = y-self.alpha*f_dZy(x,y)
            x = temp_X
            y = temp_Y
            self.X_LIST.append(x)
            self.Y_LIST.append(y)
            self.Z_LIST.append(z)
         
        
        
        
        