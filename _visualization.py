# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 11:09:34 2018

@author: hh
"""

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy import *  

from _TestFunction import problem        
from optimizer import GradientDescent

class ShowTrack_3D(object):
    def __init__(self,prob,opt):
        self.prob = prob
        self.opt =  opt
    

    
    def show(self):
        fig = plt.figure()
        ax = Axes3D(fig)
        X_show = np.arange(self.prob.x_rang[0],self.prob.x_rang[1], 1)
        Y_show = np.arange(self.prob.y_rang[0],self.prob.y_rang[1], 1)
        
        X_length = np.shape(X_show)
        Y_length = np.shape(Y_show)
        
        X_length = X_length[0]
        Y_length = Y_length[0]
        
        Z_show = np.zeros(X_length*Y_length).reshape(X_length,Y_length)
        
        i=0;j=0
        for x in X_show:
            for y in Y_show:
                Z_show[i,j] = self.prob.getValue(x,y)
                j = j+1
            j =0
            i = i+1
                
        X_show,Y_show = np.meshgrid(X_show,Y_show)                
        ax.plot_surface(X_show,Y_show, Z_show, rstride=1, cstride=1, cmap='rainbow',alpha=0.5)
        ax.scatter(self.opt.X_LIST[0], self.opt.Y_LIST[0], self.opt.Z_LIST[0], s=40, c='r')
        ax.scatter(self.prob.Global_min[0],self.prob.Global_min[1],self.prob.Global_min[-1],s=40, c='b')
        ax.plot(self.opt.X_LIST, self.opt.Y_LIST, self.opt.Z_LIST, zdir='z', c='g', lw=3)    # plot 3D gradient descent
        plt.show()