# -*- coding: utf-8 -*-
'''
Created on Sun Jan 12 13:47:53 2020

@author: Stian B. Soeisdal

Content: Second algorithm

'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def RandomOnM2(a, p, x0, zoom, pltit=' ', savpng=0):
    numits = 1000000 # Number of iterations
    # Get random array and allocate (x,y,z).
    K, X = np.random.rand(numits), np.zeros((numits+1,3))
    X[0] = x0
    # Show the density matrices
    Su = np.linspace(0, 2 * np.pi, 100)
    Sv = np.linspace(0, np.pi, 50)
    Sx = np.outer(np.cos(Su), np.sin(Sv))
    Sy = np.outer(np.sin(Su), np.sin(Sv))
    Sz = np.outer(np.ones(np.size(Su)), np.cos(Sv))
    
    for j in range(numits): # Geting the approximat attractor
        i = 0
        for k in range(len(p)): # Pick out A_i
            if K[j] >= sum(p[0:k]):
                i = k
            else:
                break
        x, y, z = X[j]
        X[j+1,0] = a[i,1,1]*x +a[i,1,2]*y +a[i,1,3]*z +a[i,1,0]
        X[j+1,1] = a[i,2,1]*x +a[i,2,2]*y +a[i,2,3]*z +a[i,2,0]
        X[j+1,2] = a[i,3,1]*x +a[i,3,2]*y +a[i,3,3]*z +a[i,3,0]
    # Plot
    fig = plt.figure(figsize=(5,10))
    fig.suptitle(pltit, fontsize=16)
    ax = fig.add_subplot(211, projection='3d')
    ax.view_init(20, 10), ax.set_xlim3d([zoom[0], zoom[1]])
    ax.set_ylim3d([zoom[2], zoom[3]]), ax.set_zlim3d([zoom[4], zoom[5]])
    ax.plot_surface(Sx, Sy, Sz, color=(1.,0.,0.,.1))
    ax.plot3D(X[:,0], X[:,1], X[:,2], 'k,', alpha=0.8)
    # Figure 2
    ax = fig.add_subplot(212, projection='3d')
    ax.view_init(20, 30), ax.set_xlim3d([zoom[0], zoom[1]])
    ax.set_ylim3d([zoom[2], zoom[3]]), ax.set_zlim3d([zoom[4], zoom[5]])
    ax.plot_surface(Sx, Sy, Sz, color=(1.,0.,0.,.1))
    ax.plot3D(X[:,0], X[:,1], X[:,2], 'k,', alpha=0.8)
    plt.subplots_adjust(top=1., bottom=-0.0, left=-0.05,
                        right=1.05, hspace=-0.05, wspace=-0.05)
    if savpng !=0:
        plt.savefig(savpng, dpi = 300)
    plt.show()

if __name__ =='__main__': # Example use, gives the system generating the Sierpinski triangle.
    # -----------------Systems-----------------
    '''
    # Sierpinski tetrahedron
    plttit = 'Random point approximation of \n the Sierpinski tetrahedron'
    r = 1/2
    A = np.array([np.matrix([[1.0, 0, 0, 0],
                             [0.0, r, 0, 0],
                             [0.0, 0, r, 0],
                             [1-r, 0, 0, r]]),
                  np.matrix([[1.0,                  0, 0, 0],
                             [(1-r)*np.sqrt(8./9.), r, 0, 0],
                             [0.0,                  0, r, 0],
                             [(r-1)/3.,             0, 0, r]]),
                  np.matrix([[1.0,                  0, 0, 0],
                             [(r-1)*np.sqrt(2./9.), r, 0, 0],
                             [(1-r)*np.sqrt(2./3.), 0, r, 0],
                             [(r-1)/3.,             0, 0, r]]),
                  np.matrix([[1.0,                  0, 0, 0],
                             [(r-1)*np.sqrt(2./9.), r, 0, 0],
                             [(r-1)*np.sqrt(2./3.), 0, r, 0],
                             [(r-1)/3.,             0, 0, r]])])
    P = np.array([0.25, 0.25, 0.25, 0.25])
    X0= np.array([0,0,1]) # Start point
    Zoom = np.array([-1,1, -1,1, -1,1]) #set axis
    savefile = 'Fig_M2_2R.png'
    '''
    '''
    # Fern
    plttit = 'Random point approximation \n of the Fern attractor'
    t = 0.900116
    A = np.array([np.matrix([[1.0, 0, 0, 0],
                             [0.0, 0, 0, 0],
                             [0.0, 0, 0, 0],
                             [0.0, 0, 0, 0.18]]),
                  np.matrix([[1.0,    0,    0,    0],
                             [0.0,    0.85, 0,   -0.1],
                             [0.0,    0,    0.85, 0],
                             [0.16*t, 0.1,  0,    0.85]]),
                  np.matrix([[1.0,    0,   0,   0],
                             [0.0,    0.3, 0,   0],
                             [0.0,    0,   0.2,-0.2],
                             [0.08*t, 0,   0.2, 0.2]]),
                  np.matrix([[1.0,    0,   0,   0],
                             [0.0,    0.3, 0,   0],
                             [0.0,    0,  -0.2, 0.2],
                             [0.08*t, 0,   0.2, 0.2]])])
    P = np.array([0.01, 0.85, 0.07, 0.07])
    X0= np.array([0,0,0]) # Start point
    Zoom = np.array([-0.7,0.1, -0.25,0.25, 0,0.8]) #set axis
    savefile = 'Fig_M2_5R.png'
    '''
    # Tree
    plttit = 'A tree attractor'
    A = np.array([np.matrix([[1.0, 0, 0, 0],
                             [0.0, 0, 0, 0],
                             [0.0, 0, 0, 0],
                             [-.6, 0, 0, .4]]),
                  np.matrix([[1.0, 0, 0, 0],
                             [0.0, 0, 0, 0],
                             [0.0, 0, 0, 0],
                             [-.9, 0, 0, .1]]),
                  np.matrix([[1.0, 0.0, 0.0, 0.0],
                             [0.0, .75, 0.0, 0.0],
                             [-.33, 0.0, .43, -.33],
                             [.05, 0.0, .33, .43]]),
                  np.matrix([[1.0, 0.0, 0.0, 0.0],
                             [0.1, .73, 0.0, 0.1],
                             [0.3, 0.0, .55, 0.3],
                             [0.2, -.1, -.3, .53]]),
                  np.matrix([[1.0, 0.0, 0.0, 0.0],
                             [0.1, .64, 0.0, 0.1],
                             [0.0, 0.0, .85, 0.0],
                             [0.4, -.1, 0.0, .64]]),
                  np.matrix([[1.0, 0.0, 0.0, 0.0],
                             [-.35, .42, 0.0, -.35],
                             [0.1, 0.0, .75, 0.1],
                             [.18, .35, -.1, .39]])])
    P = np.array([.035, .005, .215, .215, .215, .215])
    X0= np.array([0,0,0]) # Start point
    Zoom = np.array([-1,1, -1,1, -1,1]) #set axis
    savefile = 'Fig_M2_6R.png'
    
    RandomOnM2(A, P, X0, Zoom, plttit, savefile)