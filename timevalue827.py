# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
def pv_fv(c,r,n,when=1,fv=0):
    c=np.array(c)
    r=np.array(r)
    if fv==0:
       if when==1:
            n=np.arange(1,n+1)
       else:
           n=np.arange(0,n)
       pv=c/(1+r)**n   
       return pv.sum()
    else:
       if when==1:
           n=sorted(np.arange(0,n),reverse=True)
       else:
           n=sorted(np.arange(1,n+1),reverse=True)
       fv=c*(1+r)**n
       return fv.sum()

c=20000
r=0.05
n=5
pv1=pv_fv(c,r,n,when=1)
print("普通年金PV:%.2f"%pv1)
pv2=pv_fv(c,r,n,when=0)
print("预付年金PV:%.2f"%pv2)



c=[100,200,300,100,500]
r=[0.04,0.05,0.06,0.08,0.1]
n=5
pv=pv_fv(c,r,n,)
print("年金PV:%.2f"%pv)
fv=pv_fv(c,r,n,fv=1)
print("年金FV:%.2f"%fv)


def pmt(r,n,pv=0,fv=0,when=1):
    fv=np.array(fv)
    pv=np.array(pv)
    r=np.array(r)
    if fv==0:
       if when==1:
            n=np.arange(1,n+1)
       else:
           n=np.arange(0,n)
       pv_pmt=pv/(1/((1+r)**n)).sum()   
       return pv_pmt
    else:
       if when==1:
           n=sorted(np.arange(0,n),reverse=True)
       else:
           n=sorted(np.arange(1,n+1),reverse=True)
       fv_pmt=fv/((1+r)**n).sum()
       return fv_pmt

pv=2000000
r=0.05/12
n=30*12
pmt1=pmt(r,n,pv)
print("月还:%.2f"%pmt1)

c0=10736
n0=n1=15*12
r0=0.05/12
r1=0.07/12
pv1=pv_fv(c0,r0,n0)
pv2=(pv-pv1)*(1+0.05)**15
pmt2=pmt(r1,n1,pv2)
print("15年后利率调整月还:%.2f"%pmt2)

fv=3000000
n=15*12
r=0.08/12
pmt3=pmt(r,n,fv=fv,when=0)
print("每月定投:%.2f"%pmt3)

#EAR=(1+APR/m)^m-1
#EAR=e^Rc-1
#Rc=m*ln(1+APR/m)

def npv_f(rate,cashflows):
    total=0.0
    for i,cashflow in enumerate(cashflows):
        total+=cashflow/(1+rate)**i
    return total

def irr_f(cashflows,interation=10000):
    rate=1.0
    inv=cashflows[0]
    for i in range(1,interation+1):
        rate*=(1-npv_f(rate,cashflows)/inv)
        # 计算（r1,NPV（r1）)这点的斜率，与x,y轴相交的截距，推导出r2,误差较大
    return rate

P_A=[-120,10,30,50,40,10]
irr_A=irr_f(P_A)
print("IRR of Project A:%.2f%%"%(irr_A*100))   

        
  
from matplotlib import pyplot as plt 
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']
    
pv=1000
r=0.08
n=10
t=np.linspace(0,n,n)
y2=pv*(1+r*t)
y3=pv*(1+r)**t
plt.figure(figsize=(10,8))
plt.plot(t,y2,'g--')
plt.plot(t,y3,'r-')    
    