import numpy as np

def exponential_func(x,y):
    
    if y[1] > y[0]:
        xtemp = np.arange(min(x),max(x)+0.01,0.1)
        ytemp = np.exp(0.2*xtemp**2)
        ytemp = ytemp - min(ytemp)
        ytemp = ytemp/max(ytemp)
        ytemp = (max(y) - min(y))*ytemp + min(y)
    
    else:
        xtemp = np.arange(min(x),max(x)+0.01,0.1)
        ytemp = np.exp(-0.2*(xtemp**2))
        ytemp = ytemp - min(ytemp)
        ytemp = ytemp/max(ytemp)
        ytemp = (max(y) - min(y))*ytemp + min(y)
           
    return xtemp,ytemp

def gaussian_func(x,y):
    
    if y[1] > y[0]:
        sig = 2
        mu = max(x)
        xtemp = np.arange(min(x),max(x)+0.01,0.1)
        ytemp = np.exp(-((xtemp-mu*np.ones(len(xtemp)))/sig)**2)
        ytemp = ytemp - min(ytemp)
        ytemp = ytemp/max(ytemp)
        ytemp = (max(y) - min(y))*ytemp + min(y)
        
    else:
        sig = 2
        mu = max(x)
        xtemp = np.arange(min(x),max(x)+0.01,0.1)
        ytemp = np.exp(-((xtemp-mu*np.ones(len(xtemp)))/sig)**2)
        ytemp = ytemp - min(ytemp)
        ytemp = ytemp/max(ytemp)
        ytemp = (max(y) - min(y))*ytemp + min(y)
        y = ytemp[::-1]
        ytemp = y
        
    return xtemp,ytemp
