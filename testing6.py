#!/usr/bin/env python
# coding: utf-8

# In[1]:


# *args ARGUMENTS *kwargs KEY WORD ARGUMENTS


# In[8]:


def myfunc(a,b):
    return sum((a,b))*0.05


# In[9]:


myfunc(40,60)


# In[10]:


def myfunc(a,b,c=0,d=0,e=0):
    return sum((a,b))*0.05


# In[16]:


myfunc(1,1,1,1,1)


# In[17]:


def myfunc(*args):
    return sum(args)*0.05


# In[18]:


myfunc(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)


# In[21]:


def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print("My fruit of choice is {}".format(kwargs['fruit']))
    else:
        print("I did not find any fruit here")


# In[22]:


myfunc(fruit='apple',veggie='lettuce')


# In[23]:


def myfunc(*args,**kwargs):
    print("I would like {} {}".format(args[0],kwargs['food']))


# In[24]:


myfunc(1,2,3,4,5,6,fruit="orange",food="eggs")

