#!/usr/bin/env python
# coding: utf-8

# In[2]:


def NWD_iter(a, b):
    while b != 0:
        a, b = b, a%b
    return a


# In[4]:


def NWD_rek(a, b):
    if b == 0:
        return a
    return NWD_rek(b, a%b)

