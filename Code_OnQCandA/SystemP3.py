# -*- coding: utf-8 -*-
'''
Created on Sun Jan 12 13:47:53 2020

@author: Stian B. Soeisdal

Content: First algorithm on the 3 dimensional probability vectors.
Taking a iterated function system guven by A_1, A_2,..., where
   |x1|   |a1_i b1_i c1_i||x1|
A_i|x2| = |a2_i b2_i c2_i||x2|
   |x3|   |a3_i b3_i c3_i||x3|
and apply it to a inital set.
Here five iterations are chosen to be ploted.
'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def SystemOnP3(a, x, y, pltit=' ', savpng=0, pltnum=np.array([1,2,3,4,5])):
    # System info
    set_num, sys_num, seg_len, z = len(x), len(a), len(x[0]), 1-x-y
    Sx, Sy, Sz = np.array([1.,0.,0.]), np.array([0.,1.,0.]), np.array([0.,0.,1.])
    
    # Set up figure and plot the initial state
    fig = plt.figure(figsize=(8,12))
    fig.suptitle(pltit, fontsize=16)
    ax = fig.add_subplot(321, projection='3d')
    ax.plot_trisurf(Sx, Sy, Sz, color='r', alpha=0.2)
    for i in range(set_num):
        ax.plot_trisurf(x[i], y[i], z[i], color='k')
    ax.view_init(30, 30), plt.title('Initial set')
    
    fignum = 322  # For plotting certain iterations
    for n in range(pltnum[-1]):
        # Allocate new segments
        seg_num = set_num*sys_num**(n+1)
        newx = np.zeros((seg_num, seg_len))
        newy = np.zeros((seg_num, seg_len))
        newz = np.zeros((seg_num, seg_len))
        
        if n in pltnum-1: # Set up subplot
            ax = fig.add_subplot(fignum, projection='3d')
            ax.plot_trisurf(Sx, Sy, Sz, color='r', alpha=0.2)
            ax.view_init(30, 30), plt.title('Iteration {}'.format(n+1))
            ax.set_xlim3d([0, 1]), ax.set_ylim3d([0, 1]), ax.set_zlim3d([0, 1])
            fignum = fignum + 1
        
        for k in range(seg_num): # Update segmants
            k_sys, k_set = np.remainder(k,sys_num), int(k/sys_num)
            newx[k] = a[k_sys,0,0]*x[k_set] + a[k_sys,0,1]*y[k_set] + a[k_sys,0,2]*z[k_set]
            newy[k] = a[k_sys,1,0]*x[k_set] + a[k_sys,1,1]*y[k_set] + a[k_sys,1,2]*z[k_set]
            newz[k] = a[k_sys,2,0]*x[k_set] + a[k_sys,2,1]*y[k_set] + a[k_sys,2,2]*z[k_set]
            
            if n in pltnum-1: # Plot segments for chosen iterations
                ax.plot_trisurf(newx[k], newy[k], newz[k], color='k')
        x, y, z = newx, newy, newz
        
        if n==pltnum[-1]-1: # After last iteration, save and show plot
            plt.subplots_adjust(top=0.95, bottom=0.02, left=0.05,
                                right=0.95, hspace=0.05, wspace=0.0)
            if savpng != 0:
                plt.savefig(savpng, dpi = 400)
            plt.show()

if __name__ =='__main__':
    #-----------------Systems-----------------
    
    plttit = 'System generating the Sierpinski triangle'
    A = np.array([np.matrix([[1, 1/2, 1/2],
                             [0, 1/2,   0],
                             [0,   0, 1/2]]),
                  np.matrix([[1/2, 0,   0],
                             [1/2, 1, 1/2],
                             [  0, 0, 1/2]]),
                  np.matrix([[1/2,   0, 0],
                             [  0, 1/2, 0],
                             [1/2, 1/2, 1]])])
    savefile = 'Fig_P3_1.png'
    # The five chosen iterations that will be ploted
    plotnums = np.array([1,2,3,4,6]) 
    '''
    plttit = 'Second system on the 3-dim probability vectors'
    r = (np.sqrt(5)-1)/2
    A = np.array([np.matrix([[1, 1-r, 1-r],
                             [0,   r, 0.0],
                             [0, 0.0,   r]]),
                  np.matrix([[  r, 0, 0.0],
                             [1-r, 1, 1-r],
                             [0.0, 0,   r]]),
                  np.matrix([[1-r, 0.0, 0],
                             [0.0, 1-r, 0],
                             [  r,   r, 1]])])
    savefile = 'Fig_P3_2.png'
    # The five chosen iterations that will be ploted
    plotnums = np.array([1,2,3,4,8]) 
    '''
    #-----------------Inital set-----------------
    
    # All P^3 vectors
    X, Y, Z = np.array([[1.,0.,0.]]), np.array([[0.,1.,0.]]), np.array([[0.,0.,1.]])
    '''
    # Exsample of subset
    X = np.array([[0.5,0.5,0.0], [0.3,0.0,0.]])
    Y = np.array([[0.0,0.5,0.5], [0.0,0.3,0.]])
    Z = np.array([[0.5,0.0,0.5], [0.7,0.7,1.]])
    '''
    SystemOnP3(A, X, Y, plttit, savefile, plotnums)