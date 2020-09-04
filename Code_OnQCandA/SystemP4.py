# -*- coding: utf-8 -*-
'''
Created on Sun Jan 12 13:47:53 2020

@author: Stian B. Soeisdal

Content: First algorithm on 4 dimensional probability vectors.
Here the first three iterations are ploted.
'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plotsP4_with_three_iterations(a, x, y, z, savpng,pltit):
    # System info
    set_num, sys_num, seg_len, q = len(x), len(a), len(x[0]), 1-x-y-z
    Sx, Sy = np.array([1,0,0,1e-7]), np.array([0,1,0,1e-7])
    Sz, Sq = np.array([0,0,1,1e-7]), np.array([0,0,0,1-3e-7])
    
    # Set up figure and plot the initial state
    fig = plt.figure(figsize=(8,8))
    fig.suptitle(pltit, fontsize=16)
    ax = fig.add_subplot(221, projection='3d')
    ax.view_init(30, 25), plt.title('Initial set')
    ax.plot_trisurf(Sx, Sy, Sz, color=(1.,0.,0.,0.1))
    for i in range(set_num):
        ax.plot_trisurf(x[i], y[i], z[i], color=(0.1,0.4,1.,0.8))
    
    for n in range(3):
        # Set up subplot
        ax = fig.add_subplot(222+n, projection='3d')
        ax.view_init(30, 25), plt.title('Iteration {}'.format(n+1))
        ax.plot_trisurf(Sx, Sy, Sz, color=(1.,0.,0.,0.1))
        
        # Allocate new segments
        seg_num = set_num*sys_num**(n+1)
        newx, newy = np.zeros((seg_num,seg_len)), np.zeros((seg_num,seg_len))
        newz, newq = np.zeros((seg_num,seg_len)), np.zeros((seg_num,seg_len))
        # Update segmants and plot
        for k in range(seg_num):
            k_sys, k_set = np.remainder(k,sys_num), int(k/sys_num)
            newx[k] = (a[k_sys,0,0]*x[k_set] + a[k_sys,0,1]*y[k_set]
                       + a[k_sys,0,2]*z[k_set] + a[k_sys,0,3]*q[k_set])
            newy[k] = (a[k_sys,1,0]*x[k_set] + a[k_sys,1,1]*y[k_set]
                       + a[k_sys,1,2]*z[k_set] + a[k_sys,1,3]*q[k_set])
            newz[k] = (a[k_sys,2,0]*x[k_set] + a[k_sys,2,1]*y[k_set]
                       + a[k_sys,2,2]*z[k_set] + a[k_sys,2,3]*q[k_set])
            newq[k] = (a[k_sys,3,0]*x[k_set] + a[k_sys,3,1]*y[k_set]
                       + a[k_sys,3,2]*z[k_set] + a[k_sys,3,3]*q[k_set])
            ax.plot_trisurf(newx[k], newy[k], newz[k], color=(0.1,0.4,1.,0.8))
        x, y, z, q = newx, newy, newz, newq
        
        if n==2: # After last iteration, save and show plot
            plt.subplots_adjust(top=0.95, bottom=0.02, left=0.05,
                                right=0.95, hspace=0.05, wspace=0.0)
            plt.savefig(savpng, dpi = 400), plt.show()

if __name__ =='__main__':
    #-----------------Systems-----------------
    
    plotit = 'System generating the Sierpinski tetrahedron'
    A = np.array([np.matrix([[1, 1/2, 1/2, 1/2],
                             [0, 1/2, 0.0, 0.0],
                             [0, 0.0, 1/2, 0.0],
                             [0, 0.0, 0.0, 1/2]]),
                  np.matrix([[1/2, 0, 0.0, 0.0],
                             [1/2, 1, 1/2, 1/2],
                             [0.0, 0, 1/2, 0.0],
                             [0.0, 0, 0.0, 1/2]]),
                  np.matrix([[1/2, 0.0, 0, 0.0],
                             [0.0, 1/2, 0, 0.0],
                             [1/2, 1/2, 1, 1/2],
                             [0.0, 0.0, 0, 1/2]]),
                  np.matrix([[1/2, 0.0, 0.0, 0],
                             [0.0, 1/2, 0.0, 0],
                             [0.0, 0.0, 1/2, 0],
                             [1/2, 1/2, 1/2, 1]])])
    savfig = 'Fig_P4_1.png'
    
    #-----------------Inital set-----------------
    # All P^4 vectors
    X = np.array([np.array([1.,0.,0.,1e-9]),np.array([1.,0.,0.,1.])])
    Y = np.array([np.array([0.,1.,0.,1e-9]),np.array([0.,1.,0.,0.])])
    Z = np.array([np.array([0.,0.,1.,1e-9]),np.array([0.,0.,1.,0.])])
    Q = np.array([np.array([0.,0.,0.,1-3e-9]),np.array([0.,0.,0.,0.])])
    
    plotsP4_with_three_iterations(A, X, Y, Z, savfig, plotit)
    