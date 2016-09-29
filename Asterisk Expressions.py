# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 14:40:48 2016

@author: Karthick Perumal
"""

n = int('1')

def check(t):
    counter = 0
    for i in range(len(t)):
        #print('t[i] is ', t[i])
        if t[i] == '*':            
            counter = counter +1
            #print(counter)
            if counter == 3:
                return False
        else:            
            counter = 0
            
    return True

def calculate(t):
    y = t.split('*')
    i = 0
    while i < (len(y)):
        print(y[i])
        i = i +1
            
            
    print(y)

for i in range(n):
    t = "3*2**3**2**5"
    if (t[0] == '*' or t[-1] == '*'):
        print('Syntax Error')
        break
    else:
        status = check(t)
        if status:  
            calculate(t)
                #if t[i] == '*' and t[i+1] == '*':
                
        else:
            print('Syntax Error')
            
            
