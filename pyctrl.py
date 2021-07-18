import numpy as np
import sympy as sym
import pandas as pd
from mpmath import *
import matplotlib.pyplot as plt

s,t,x = sym.symbols('s t x', real = True)
x1,x2,x3 = sym.symbols('x1 x2 x3')

class pyctrl:
    
    
    def __init__(self):
        pass
    
    
    
    


    

    def numpy2sympy(self, M):
        return sym.Matrix(M)

    def ss2tf(self,A,B,C,D):
        '''this method converts from state space to transfer function
        inputs: A Matrix, B Matrix, C Matrix, D Matrix
        returns: transfer function'''
        A,B,C,D=self.numpy2sympy(A),self.numpy2sympy(B),self.numpy2sympy(C),self.numpy2sympy(D)   
        TF=C.transpose() * (sym.eye(A.shape[0])*s-A).inv() * B + sym.Matrix([D])
        TF=sym.simplify(TF)
        return TF



    def tf2ss(self,n,d,method='controllable'):
        
        
 
        
        '''
        converts transfer function to state space
        Parameters: numerator , denominator, method(controllable or observable)
        returns A,B,C,D Matrices
        
                
        
        '''
        if method=='observable':
            
            tf=sym.Poly(n,s)/sym.Poly(d,s)
            A=np.zeros((len(d)-1,len(d)-1))
            A[:,len(A)-1]=-1*d[1:][::-1]
            A[1:,0:len(A)-1]=np.eye(len(d)-2)
            if len(d) >len(n):
                
                B=n[::-1]
                B=np.append(np.zeros(len(A)-len(B)),B)
                C=np.append(np.zeros(len(A)-1),[1])
                D=0
            elif len(d)==len(n):
                D=sym.limit(tf,s,sym.oo)
                n=(tf-D)*sym.Poly(d,s)
                n=sym.Poly(sym.simplify(n),s)
                n=n.coeffs()
                B=n[::-1]
                B=np.append(np.zeros(len(A)-len(B)),B).astype(None)
                C=np.append(np.zeros(len(A)-1),[1])

            D=np.array([D]).astype(None)
                

                
                
            
        elif method=='controllable':
            
            tf=sym.Poly(n,s)/sym.Poly(d,s)

            A=np.zeros((len(d)-1,len(d)-1))
            A[len(A)-1,:]=-1*d[1:][::-1]
            A[0:len(A)-1,1:]=np.eye(len(d)-2)
            
            if len(d) >len(n):
                B=np.append(np.zeros(len(A)-1),[1])
                C=n[::-1]
                C=np.append(np.zeros(len(A)-len(C)),C)
                D=0
            elif len(d)==len(n):
                D=sym.limit(tf,s,sym.oo)
                n=(tf-D)*sym.Poly(d,s)
                n=sym.Poly(sym.simplify(n),s)
                n=n.coeffs()
                B=np.append(np.zeros(len(A)-1),[1])
                C=n[::-1]
                C=np.append(np.zeros(len(A)-len(C)),C).astype(None)
                

            D=np.array([D]).astype(None)

        return A,B,C,D


    
    def solve(self,A,B,x0,u):
        '''finds the system solution in S domain
        Parameters: A Matrix ,B Matrix,initial condtion Matrix,input u
        returns: system solution in time domain
        '''
        A,B,x0=self.numpy2sympy(A),self.numpy2sympy(B),self.numpy2sympy(x0)
        u=sym.laplace_transform(u, t, s, noconds=True)
        x=(sym.eye(A.shape[0])*s-A).inv()*x0 +(sym.eye(A.shape[0])*s-A).inv()*B*u
        x=sym.simplify(x)
        return x
            
    def isStable(self,A):
        '''checks whether a system is stable or not
        Parameters: A Matrix
        return True or False'''
        A=self.numpy2sympy(A)
        for i in A.eigenvals().keys():
            if i>0:
                return False
            else:
                return True


            

    def isObservable(self,A,C):
        '''checks whether a system is observable or not
        Parameters: A Matrix, C Matrix
        return True or False'''
        A,C=self.numpy2sympy(A),self.numpy2sympy(C)
        n=A.shape[0]        
        O=C.transpose()
        for i in range(n-1):
            O=O.row_insert(i+1,C.transpose()*A**(i+1))
        if O.rank()==n:
            return True
        else :
            return False




    def isControllable(self,A,B):
        '''checks whether a system is controllable or not
        Parameters: A Matrix, B Matrix
        return True or False'''
        A,B=self.numpy2sympy(A),self.numpy2sympy(B) 
        n=A.shape[0]
        c=B
        for i in range(n-1):
            c=c.col_insert(i+1,A**(i+1)*B)
            
        if c.rank()==n:
            return True
        else :
            return False

    def step(self,n,d,t=10,color=None):
        
        '''
        plots the step response of a transfer function
        
        Parameters: TF numerator, TF denominator, response time, line color
        The supported color abbreviations are the single letter codes

        =============    ===============================
        character        color
        =============    ===============================
        ``'b'``          blue
        ``'g'``          green
        ``'r'``          red
        ``'c'``          cyan
        ``'m'``          magenta
        ``'y'``          yellow
        ``'k'``          black
        ``'w'``          white
        =============    ===============================
        '''
        tf=sym.Poly(n,s)/sym.Poly(d,s)
        Sresp=(1/s)*tf #step response in s domain

        mp.dps = 15; mp.pretty = True
        tt = np.linspace(.001,t,100)
        fs = lambda s: eval(str(Sresp)) # Sresp as a lambda expression so that mpmath can deal with it
        y=[]                             
        for tti in tt:
            y.append(invertlaplace(fs,tti,method='talbot')) # numerically evaluating inverse laplace  
                                                            # for all pointss in tt array
        
        
        e_ss=sym.limit(1-tf,s,0)  # steady state error
        ssResp=1-e_ss
        plt.plot(tt,y,color=color)
        plt.axhline(ssResp, linestyle = 'dotted',color = 'g')
            

    def placePoles(self,A,B,*roots):
        '''
        finds gain k for pole placplacement using Ackermann's method
        Parameters: A Matrix,B Matrix, poles tuble
        returns: gain vector
        
        '''
        
        def roots2poly(*roots):
            from sympy import Symbol
            x = Symbol('x')
            whole =1
            for root in roots:
                whole *=(x-root)
            p=sym.poly(whole.expand(),x)
            p=p.all_coeffs()
            return p 
        
        p=roots2poly(*roots)


        A,B=self.numpy2sympy(A),self.numpy2sympy(B)  
        
        arr=np.zeros((1,A.shape[0]-1))
        arr=sym.Matrix(np.append(arr,[1])).transpose()
        
        
        n=A.shape[0]
        c=B
        for i in range(n-1):
            c=c.col_insert(i+1,A**(i+1)*B)
        
        Q=sym.zeros(A.shape[0])
        for i in range(len(p)):
            Q=Q+p[i]*A**(len(p)-1-i)
        
        return (arr * c.inv() * Q)  



            
                                                       
    



                                            
