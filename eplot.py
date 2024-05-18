import os, sys, argparse, subprocess
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from splines import *


parser = argparse.ArgumentParser()

parser.add_argument('-f',dest='file_path', type=str, default='data.csv',help='Input File, Default = data.csv')
parser.add_argument('-o',dest='output', type=str, default='energy_diagram.pdf',help='Output Image Name, Default = energy_diagram.pdf')
parser.add_argument('-t',dest='func', type=str, default='gaussian',help='Spline Function (gaussian/exponential), Default = gaussian')
args = parser.parse_args()

def main(argv):

    color_list = ['red','blue']  # Update based on number of different channels to plot

    data = read_data(args.file_path)

    plt.figure(figsize=(20,5))

    for j in data:
        x,y = data[j][0],data[j][1]

        for i in range(0,len(x)-1,1):
            xtemp = [x[i],x[i+1]]
            ytemp = [y[i],y[i+1]]
            
            if args.func == 'exponential': new_x,new_y = exponential_func(xtemp,ytemp)
            if args.func == 'gaussian': new_x,new_y = gaussian_func(xtemp,ytemp)
            
            plt.plot(new_x, new_y,color='black',alpha=0.5)
            plt.scatter(xtemp,ytemp,color=color_list[int(j)-1],edgecolor='black',s=50)
        
    plt.xticks(np.arange(0,max(x)+1))
    plt.xlim(min(x)-1,max(x)+1)
    plt.ylim(min(y)-5,max(y)+5)
    plt.xlabel('Reaction Coordinate',fontsize=15)
    plt.ylabel('Energy (kcal/mol)',fontsize=15)

    plt.savefig(args.output) 

    return 

def read_data(file_path):
    
    data = {}
    with open(file_path) as f:
        f.readline()
        for fields in f:
            i = fields.rstrip().split(',')
            
            if i[3] in data: 
                data[i[3]][0] += [float(i[0])]
                data[i[3]][1] += [float(i[1])]
            else:
                data[i[3]] = [[],[]]
                data[i[3]][0] += [float(i[0])]
                data[i[3]][1] += [float(i[1])]
    
    return data

if __name__ == "__main__":
    main(sys.argv[1:])
