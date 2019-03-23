# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 09:58:23 2018

@author: hecongcong
"""

######################净现值法(估算10年内)
##折现率

def discount_rate(i,time):
    time=time-1
    res=[1.0]
    tmp_rate=1.0
    for j in range(time):
        tmp_rate*=(1+i)
        discount=1/tmp_rate
        res.append(discount)
    return(res)
    

##净现值
#现金流出和现金流入函数
def Npv_10(inputs,outputs,rate,time):
    lens=len(inputs)
    diff=[]
    discount=discount_rate(rate,time)
    sums=0
    for i in range(lens):
        diff=inputs[i]-outputs[i]
        sums+=diff*discount[i]
    return(sums)
    
#净现金流函数
def Npv(inputs,rate,time):
    lens=len(inputs)
    discount=discount_rate(rate,time)
    npv=[]
    for i in range(lens):
        npv.append(inputs[i]*discount[i])
    return(npv)
    



#############################内含报酬率法(IRR)
def cal_Npv(inputs,rate):
    time=len(inputs)
    sums=inputs[0]
    tmp=1.0
    discount_rate=1.0
    for i in range(1,time):
        tmp*=(1+rate)
        discount_rate=1.0/tmp
        sums+=(inputs[i]*discount_rate)
    return(sums)



#####计算IRR，精度为a且大于0.
def cal_Irr(inputs,irr,a):
    import numpy as np
    left,right=0.0,0.0
    npv=cal_Npv(inputs,irr)
    if(np.abs(npv)<=a):
        return(irr)
    if(npv>0):
        left=irr
        irr+=0.1
        while(True):
            npv=cal_Npv(inputs,irr)
            if(np.abs(npv)<=a):
                return(irr)
            if(npv>0):
                irr+=0.1
            elif(npv<0):
                right=irr
                break
    elif(npv<0):
        right=irr
        irr-=0.1
        while(True):
            npv=cal_Npv(inputs,irr)
            if(np.abs(npv)<=a):
                return(irr)
            if(npv<0):
                irr-=0.1
            elif(npv>0):
                left=irr
                break
    ##二分法
    while(left<=right):
        mid=left+(right-left)/2
        npv=cal_Npv(inputs,mid)
        if(np.abs(npv)<=a):
            return(mid)
        if(npv>0):
            left=mid
        elif(npv<0):
            right=mid
    return(mid)
        
        

        
    









