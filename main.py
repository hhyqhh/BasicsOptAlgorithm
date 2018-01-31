# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 20:18:34 2018

@author: hh
"""
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy import *

from _TestFunction import problem        
from optimizer import GradientDescent
from _visualization import ShowTrack_3D



def getOptimizer(ID):
    if ID == '1':
        opt = GradientDescent()
    elif ID == '2':
        opt = GradientDescent()
    else :
        opt = None
    return opt



def showResult(prob,opt):
    real_x = prob.Global_min[0]
    real_y = prob.Global_min[1]
    real_min_value = prob.Global_min[-1]
    
    find_x = opt.X_LIST[-1]
    find_y = opt.Y_LIST[-1]
    find_min_value = opt.Z_LIST[-1]


    print("Real Global minimum: f(%f,%f)=%f" % (real_x,real_y,real_min_value))
    print("Find Global minimum: f(%f,%f)=%f" % (find_x,find_y,find_min_value))

if __name__ == '__main__':
    
    
    print('---------ProblemID---------')
    print('1.Booth function')
    print('2.McCormick  function')  
    print('3.Ackley function')
    print('4.')
    print('5.')
    print('..........')
    probID = input("please input ProblemID:")
    
    
    print('--------AlgorithmID--------')
    print('1.GradientDescent')
    print('..........')
    AlgID = input("please input AlgorithmID:")
    
    
  #  probID ='5'
  #  AlgID ='1'
    AlgID_Decoder = {'1':'Booth','2':'McCormick','3':'Ackley','4':'GoldsteinPrice','5':'Himmelblau'}
    
    
    prob = problem(AlgID_Decoder[probID])
    opt = getOptimizer(AlgID)
    
    opt.run(prob)
    
 #   print(opt.Z_LIST)
    showResult(prob,opt)

    
    image = ShowTrack_3D(prob,opt)
    image.show()
    
    
   
       
    