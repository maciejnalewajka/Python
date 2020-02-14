#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1

def heapify(t, n, i): 
    lar = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and t[i] < t[l]: 
        lar = l 
    if r < n and t[lar] < t[r]: 
        lar = r 
    if lar != i: 
        t[i],t[lar] = t[lar],t[i]
        heapify(t, n, lar)

def heapSort(l): 
    n = len(l) 
    for i in range(n, -1, -1): 
        heapify(l, n, i) 
    for i in range(n-1, 0, -1): 
        l[i], l[0] = l[0], l[i]
        heapify(l, i, 0)
    return l


# In[2]:


#2

def opt_heapsort(s):                               
    sl = len(s)                                    

    def swap(pi, ci):                              
        if s[pi] < s[ci]:                          
            s[pi], s[ci] = s[ci], s[pi]            

    def sift(pi, unsorted):                        
        i_gt = lambda a, b: a if s[a] > s[b] else b
        while pi*2+2 < unsorted:                   
            gtci = i_gt(pi*2+1, pi*2+2)            
            swap(pi, gtci)                         
            pi = gtci                              
    # heapify                                      
    for i in range(int((sl/2)-1), -1, -1):              
        sift(i, sl)                                
    # sort                                         
    for i in range(sl-1, 0, -1):                   
        swap(i, 0)                                 
        sift(0, i)  
    return l


# In[ ]:




