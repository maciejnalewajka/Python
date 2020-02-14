#!/usr/bin/env python
# coding: utf-8

# In[3]:


def insertion_sort(lista):
    for i in range(1, len(lista)):
        Val = lista[i]
        Ind = i
        while Ind>0 and lista[Ind-1]>Val:
            lista[Ind] = lista[Ind-1]
            Ind -= 1
        lista[Ind] = Val
    return lista

