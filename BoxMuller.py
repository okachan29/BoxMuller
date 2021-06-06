import math
import gc
import time
from random import random
import numpy as np
import matplotlib.pyplot as plt


def main():
    print("平均値を入力してください：")
    ave=int(input())
    max=ave
    print("分散を入力してください：")
    v=float(input())
    var=math.sqrt(v)
    print("標本数を入力してください：")
    num=int(input())
    data1=[]
    N=0
    for i in range(num):
        X=random()
        Y=random()
        z=math.sqrt(-2*math.log(X))*math.cos(2*math.pi*Y)
        z=var*z+ave
        data1.append(z)
        N+=1
    compare(data1)
    fig = plt.figure()
    ax = fig.add_subplot(2,1,1,facecolor='black',ylim=(0,2000),xlim=(-10+ave,10+ave))
    ax.set_title(str(N)+"       \u03bc="+str(ave)+"      \u03c3^2="+str(v))
    ax.hist(data1, bins=10,align='mid',facecolor='green',rwidth=5)
    
    sx = sorted(data1)
    sy = [i/num for i in range(num)]
    ax2 = fig.add_subplot(2,1,2,facecolor='black',ylim=(0,1),xlim=(-10+ave,10+ave))
    ax2.plot(sx, sy)
    fig.show() 
    input()

    
def compare(data1):
    print(np.var(data1))
    

if __name__=='__main__':
    main()