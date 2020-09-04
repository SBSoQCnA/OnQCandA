# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 13:47:53 2020

@author: Stian B. Soeisdal

Content: First algorithm on the 2 dimensional probability vectors.
Taking a iterated function system guven by A_1, A_2,..., where
   |x1|   |a_i b_i||x1|
A_i|  | = |       ||  |
   |x2|   |c_i d_i||x2|
and apply it to a inital set and plot some of the first iterations.
"""
import numpy as np
import matplotlib.pyplot as plt

def SystemOnP2(a, x, savpng, pltit):
    # System info
    set_num, sys_num, y = len(x), len(a), 1-x
    Sx, Sy = np.array([0,1]), np.array([1,0])
    
    # Set up figure and plot the initial set
    fig, axs = plt.subplots(2, 2, figsize=(7,6))
    fig.suptitle(pltit, fontsize=16)
    axs[0,0].plot(Sx, Sy, 'r-', alpha=0.2, linewidth=1)
    for i in range(set_num):
        axs[0,0].plot(x[i], y[i], 'k-', linewidth=1.2)
        axs[1,1].plot(y[i], 0*y[i]+1,'k-', linewidth=1.2)
    axs[0,0].set_title('Initial set')
    axs[0,0].set_xlim(0, 1), axs[0,0].set_ylim(0, 1)
    axs[1,1].set_title('Comparing iterations (y-axis)'), axs[1,1].axis('off')
    N1, N2 = np.array([0,1]), np.array([1,0])
    
    for n in range(3):
        # Set up next sub plot
        if n <= 1:
            n1, n2 = N1[n], N2[n]
            axs[n1,n2].set_xlim(0, 1), axs[n1,n2].set_ylim(0, 1)
            axs[n1,n2].set_title('Iteration: {}'.format(n+1))
            axs[n1,n2].plot(Sx, Sy, 'r-', alpha=0.2, linewidth=1)
        
        # Update segmants and plot
        newx = np.zeros((set_num*sys_num**(n+1),2))
        newy = np.zeros((set_num*sys_num**(n+1),2))
        for k in range(set_num*sys_num**(n+1)):
            k_sys, k_set = np.remainder(k,sys_num), int(k/sys_num)
            newx[k] = a[k_sys,0,0]*x[k_set] + a[k_sys,0,1]*y[k_set]
            newy[k] = a[k_sys,1,0]*x[k_set] + a[k_sys,1,1]*y[k_set]
            if n <= 2:
                axs[n1,n2].plot(newx[k],newy[k],'k-', linewidth=1.2)
            axs[1,1].plot(newy[k],0*newx[k]-n,'k-', linewidth=1.2)
        x, y = newx, newy
        
        if n==2: # Save and show plot after last iteration
            plt.subplots_adjust(top=0.9, bottom=0.05, left=0.10,
                                right=0.95, hspace=0.35, wspace=0.35)
            plt.savefig(savpng, dpi = 200), plt.show()

if __name__ =='__main__': # Example use:
    #-----------------Systems-----------------
    
    # System generating the Cantor set.
    plttit = 'System that generates the Cantor set'
    A = np.array([np.matrix([[1, 2/3],
                             [0, 1/3]]),
                  np.matrix([[1/3, 0],
                             [2/3, 1]])])
    savefile = 'Fig_P2_1.png'
    '''
    # Another 
    plttit = 'Second system on the 2-dim probability vectors'
    A = np.array([np.matrix([[1, 1/2],
                             [0, 1/2]]),
                  np.matrix([[1/4, 0],
                             [3/4, 1]]),
                  np.matrix([[3/4, 1/2],
                             [1/4, 1/2]])])
    savefile = 'Fig_P2_2.png'
    '''
    #-----------------Inital set----------------- (given as its x-value)
    
    # All robability vectors
    X = np.array([[0,1]])
    
    '''
    # First and last third segments
    np.array([[0,1/3], [2/3, 1]])
    '''
    '''
    # First quarter and last half
    np.array([[0,1/4], [1/2, 1]])
    '''
    SystemOnP2(A, X, savefile, plttit)