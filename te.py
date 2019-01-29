#!/bin/python3

import os
import sys

class heap:
    
    def __init__(self):
        self.arr=[0]
        self.size=0
        
    def insert(self,value):
        self.arr.append(value)
        self.size+=1
        self.set_new_heap(self.size)
        
    def r_top(self):
        k=self.arr[1]
        self.arr[1]=self.arr[self.size]
        self.arr.pop()
        self.size-=1
        self.set_heap()
        return k

class min_heap(heap):
        
    def set_new_heap(self,i):
        while i//2>0:
            if self.arr[i//2]>self.arr[i]:
                self.arr[i//2],self.arr[i]=self.arr[i],self.arr[i//2]
                i=i//2
            else:
                break
        
    def set_heap(self):
        i=1
        while 2*i<=self.size:
            m=self.min_child(i)
            if self.arr[i]>self.arr[m]:
                self.arr[i],self.arr[m]=self.arr[m],self.arr[i]
                i=m
            else:
                break
    
    def min_child(self,i):
        if 2*i+1>self.size:
            return 2*i
        else:
            if self.arr[2*i+1]<self.arr[2*i]:
                return 2*i+1
            else:
                return 2*i
        
        
class max_heap(heap):
        
    def set_new_heap(self,i):
        while i//2>0:
            if self.arr[i//2]<self.arr[i]:
                self.arr[i//2],self.arr[i]=self.arr[i],self.arr[i//2]
                i=i//2
            else:
                break
                
    def set_heap(self):
        i=1
        while 2*i<=self.size:
            m=self.max_child(i)
            if self.arr[i]<self.arr[m]:
                self.arr[i],self.arr[m]=self.arr[m],self.arr[i]
                i=m
            else:
                break
                
    def max_child(self,i):
        if 2*i+1>self.size:
            return 2*i
        else:
            if self.arr[2*i+1]>self.arr[2*i]:
                return 2*i+1
            else:
                return 2*i
        

def runningMedian(a):
    '''
    k=sorted(a)
    ans=[]
    for _ in range(a_count):
        s=len(k)                       # results in timeout
        if s%2==0:
            ans.append((k[s//2]+k[s//2-1])/2)
            k.remove(a[s-1])
        else:
            ans.append(float(k[s//2]))
            k.remove(a[s-1])
    
    return reversed(ans)
    '''
    
    mih=min_heap()
    mah=max_heap()
    ans=[a[0],(a[0]+a[1])/2]
    mih.insert(max(a[0],a[1]))
    mah.insert(min(a[0],a[1]))
    for i in range(2,len(a)):
        if a[i]<=ans[-1]:
            mah.insert(a[i])
        else:
            mih.insert(a[i])

        if mih.size==mah.size:
            k=(mih.arr[1]+mah.arr[1])/2
            print(mih.arr[1],mah.arr[1])
            print(k)
            ans.append(k)
        elif abs(mih.size-mah.size)==1:
            if mih.size>mah.size:
                ans.append(mih.arr[1])
            else:
                ans.append(mah.arr[1])
        else:
            if mih.size>mah.size:
                mah.insert(mih.r_top())
            else:
                mih.insert(mah.r_top())
        
            if mih.size>mah.size:
                ans.append(mih.arr[1])
            else:
                ans.append(mah.arr[1])
                
    return ans
    
if __name__ == '__main__':
    a = []

    for _ in range(int(input())):
        a.append(int(input()))

    result = runningMedian(list(map(float,a)))

    print('\n'.join(map(str, result)))


