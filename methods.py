import math
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np
from graphics import *

def arcedgepoints(x0,y0,r,alpha,phi):
    return [x0+r*np.cos(phi+alpha), y0+r*np.sin(phi+alpha)]

def makegridpoints(extremepts, radius):
    gridsx = []
    gridsy = []
    #print(min(extremepts), max(extremepts))
    for i in range(int(min(extremepts)[0]),int(max(extremepts)[0]), int(2*radius*np.cos(np.pi/3))):
        for j in range(int(min(extremepts)[1]),int(max(extremepts)[1]), int(2*radius*np.sin(np.pi/3))):
            gridsx += [i]
            gridsy += [j]
    for i in range(int(min(extremepts)[0] - radius*np.cos(np.pi/3)),int(max(extremepts)[0] + radius*np.cos(np.pi/3)), int(2*radius*np.cos(np.pi/3))):
        for j in range(int(min(extremepts)[1]- radius*np.sin(np.pi/3)),int(max(extremepts)[1] + radius*np.cos(np.pi/3)), int(2*radius*np.sin(np.pi/3))):
            gridsx += [i]
            gridsy += [j]
    return gridsx, gridsy

def getextremepts(extremepts):
    ptsx = []
    ptsy = []
    for x,y in extremepts:
        ptsx += [x]
        ptsy += [y]
    
    pt1 = [max(ptsx),max(ptsy)]
    pt2 = [max(ptsx),min(ptsy)]
    pt3 = [min(ptsx),max(ptsy)]
    pt4 = [min(ptsx),min(ptsy)]
    return pt1, pt2, pt3, pt4

def plotarc(ax, center, point1, point2):
    r = 163*2*2
    #center of the ellipse
    x = center[0]; y = center[1]
    # angle
    alpha = 0
    theta1 = np.pi/2 - np.arctan2(*(np.array(point1)-np.array(center)))
    theta2 = np.pi/2 - np.arctan2(*(np.array(point2)-np.array(center)))
    ax.add_patch(Arc((x, y), r, r,
                     theta1=np.rad2deg(theta1), theta2=np.rad2deg(theta2), 
                     edgecolor='g', lw=1.1))
    
def plotarcr(ax, radius, center, point1, point2):
    r = radius
    #center of the ellipse
    x = center[0]; y = center[1]
    # angle
    alpha = 0
    theta1 = np.pi/2 - np.arctan2(*(np.array(point1)-np.array(center)))
    theta2 = np.pi/2 - np.arctan2(*(np.array(point2)-np.array(center)))
    ax.add_patch(Arc((x, y), r, r,
                     theta1=np.rad2deg(theta1), theta2=np.rad2deg(theta2), 
                     edgecolor='g', lw=1.1))

    
def get_intercetions(x0, y0, r0, x1, y1, r1):
    # circle 1: (x0, y0), radius r0
    # circle 2: (x1, y1), radius r1

    d=math.sqrt((x1-x0)**2 + (y1-y0)**2)

    # non intersecting
    if d > r0 + r1 :
        return None
    # One circle within other
    if d < abs(r0-r1):
        return None
    # coincident circles
    if d == 0 and r0 == r1:
        return None
    else:
        a=(r0**2-r1**2+d**2)/(2*d)
        h=math.sqrt(r0**2-a**2)
        x2=x0+a*(x1-x0)/d   
        y2=y0+a*(y1-y0)/d   
        x3=x2+h*(y1-y0)/d     
        y3=y2-h*(x1-x0)/d 

        x4=x2-h*(y1-y0)/d
        y4=y2+h*(x1-x0)/d

        return (x3, y3, x4, y4)
    
def intersection(center, radius, p1, p2):

    """ find the two points where a secant intersects a circle """

    dx, dy = p2[0] - p1[0], p2[1] - p1[1]

    a = dx**2 + dy**2
    b = 2 * (dx * (p1[0] - center[0]) + dy * (p1[1] - center[1]))
    c = (p1[0] - center[0])**2 + (p1[1] - center[1])**2 - radius**2

    discriminant = b**2 - 4 * a * c
    assert (discriminant > 0), 'Not a secant!'

    t1 = (-b + discriminant**0.5) / (2 * a)
    t2 = (-b - discriminant**0.5) / (2 * a)

    return Point(dx * t1 + p1[0], dy * t1 + p1[1]), Point(dx * t2 + p1[0], dy * t2 + p1[1])