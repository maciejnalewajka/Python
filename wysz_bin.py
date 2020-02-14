#!/usr/bin/env python
# coding: utf-8

# In[12]:


def wysz_bin(lista, item):
    first = 0
    last = len(lista)-1
    while first <= last:
        mid = (first + last) // 2
        if lista[mid] == item:
            return True
        if item < lista[mid]:
            last = mid-1
        else:
            first = mid+1
    return False
        

