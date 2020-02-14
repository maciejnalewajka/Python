#!/usr/bin/env python
# coding: utf-8

# In[23]:


def selection_sort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal= L[minIndx]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[minIndx]
            j += 1
        L[i], L[minIndx] = L[minIndx], L[i]
    return L

