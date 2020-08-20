# -*- coding: utf-8 -*-
'''
Created on Sun Jan 12 13:47:53 2020

@author: Stian B. Soeisdal

Content: Second algorithm on the 3 dimensional probability vectors.
For random i, apply A_i to point and plot. Repeat for new point.
   |x1|   |a1_i b1_i c1_i||x1|
A_i|x2| = |a2_i b2_i c2_i||x2|
   |x3|   |a3_i b3_i c3_i||x3|
'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def RandomApproximationOfAttractor(a,p,x0,pltit):
    numits = 1000000 # Number of iterations
    # Get random array and allocate (x,y,z).
    K, X = np.random.rand(numits), np.zeros((numits+1,3))
    X[0] = x0 # Initialize (x,y,z).
    # Probability vectors
    Sx, Sy, Sz = np.array([1.,0.,0.]), np.array([0.,1.,0.]), np.array([0.,0.,1.])
    
    for j in range(numits): # Geting the approximat attractor
        for k in range(len(p)): # Pick out A_i
            if K[j] >= sum(p[0:k]):
                i = k
            else:
                break
        x, y, z = X[j]
        X[j+1] = (a[i,0,0]*x+a[i,0,1]*y+a[i,0,2]*z, a[i,1,0]*x+a[i,1,1]*y+a[i,1,2]*z,
                  a[i,2,0]*x+a[i,2,1]*y+a[i,2,2]*z)
    
    # Plot
    fig = plt.figure(figsize=(9,9))
    ax = fig.add_subplot(111, projection='3d')
    ax.view_init(30, 30), plt.title(pltit, fontsize=16)
    ax.plot_trisurf(Sx, Sy, Sz, color='r', alpha=0.2)
    ax.plot3D(X[:,0], X[:,1], X[:,2], 'k,')
    plt.savefig('Fig_P3_R.png', dpi = 300), plt.show()

if __name__ =='__main__':
    #-----------------Systems-----------------
    '''
    plotit = 'Random point approximation of the Sierpinski triangle'
    A = np.array([np.matrix([[1, 1/2, 1/2],
                             [0, 1/2,   0],
                             [0,   0, 1/2]]),
                  np.matrix([[1/2, 0,   0],
                             [1/2, 1, 1/2],
                             [  0, 0, 1/2]]),
                  np.matrix([[1/2,   0, 0],
                             [  0, 1/2, 0],
                             [1/2, 1/2, 1]])])
    pp = np.array([1/3, 1/3, 1/3])
    '''
    plotit = 'Random point approximation for the second 3-dim system'
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
    pp = np.array([0.4, 0.4, 0.2])
    
    #-----------------Inital point-----------------
    X0 = np.array([0,0,1])
    
    RandomApproximationOfAttractor(A,pp,X0,plotit)