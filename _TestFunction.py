# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 10:21:58 2018

@author: hh
"""

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy import *

class problem(object):
    def __init__(self,name):
        self.name= name
        self.x_rang = []
        self.y_rang = []
        self.X = symbols('X')
        self.Y = symbols('Y')
        self.Z = symbols('Z', cls=Function)
        self.Global_min=[]

    def getprob(self):
        if self.name == 'Booth':
            self.x_rang = [-20,20]
            self.y_rang = [-20,20]
            
            # Global_min[X,Y,MIN]
            self.Global_min = [1,3,0]
            
            return self.Func_Booth()
        
        elif self.name == 'McCormick':
            self.x_rang = [-20,20]
            self.y_rang = [-20,20]
            
            # Global_min[X,Y,MIN]
            self.Global_min = [-0.54719,-1.54719,-1.9133]
            return self.Func_McCormick()
        
        elif self.name == 'Ackley':
            self.x_rang = [-10,10]
            self.y_rang = [-10,10]
            
            # Global_min[X,Y,MIN]
            self.Global_min = [0,0,0]
            return self.Func_Ackley()  
        
        elif self.name == 'GoldsteinPrice':
            self.x_rang = [-1,1]
            self.y_rang = [-1,1]
            self.Global_min = [0,-1,3]
            return self.Func_GoldsteinPrice()
        elif self.name == 'Himmelblau':
            self.x_rang = [-5,5]
            self.y_rang = [-5,5]
            self.Global_min = [3,2,0]
            return self.Func_Himmelblau()
        else :
            return None

    def getValue(self,x,y):
        f = lambdify((self.X,self.Y), self.getprob())
        return f(x,y)

#-----------function----------------------#
            
        
    def Func_Booth(self):
        X = self.X
        Y =self.Y
        Z = self.Z
        Z = (X +2*Y-7)**2+(2*X+Y-5)**2
        return Z
    
    def Func_Ackley(self):
        X = self.X
        Y =self.Y
        Z = self.Z
        Z = -20*exp(-0.2*sqrt(0.5*(X**2+Y**2)))-exp(0.5*(cos(2*pi*X)+cos(2*pi*Y)))+E+20
        return Z
        
    def Func_McCormick(self):
        X = self.X
        Y =self.Y
        Z = self.Z
        Z = sin(X+Y)+(X-Y)**2-1.5*X+2.5*Y+1
        return Z
    

    
    def Func_GoldsteinPrice(self):
        X = self.X
        Y =self.Y
        Z = self.Z
        Z = ((1+(X+Y+1)**2)*(19-14*X+3*X**2-14*Y+6*X*Y+3*Y**2))*(30+((2*X-3*Y)**2)*(18-32*X+12*X**2+48*Y-36*X*Y+27*Y**2))
        return Z
    
    
    def Func_Himmelblau(self):
        X = self.X
        Y =self.Y
        Z = self.Z
        Z = (X**2+Y-11)**2+(X+Y**2-7)**2
        return Z
    
    