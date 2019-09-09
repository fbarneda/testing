#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = 25

def printer():
    
    x = 50
    return x


# In[2]:


print(x)


# In[3]:


print(printer())


# In[5]:


# lambda num:num**2


# In[13]:


# GLOBAL
name = 'THIS IS A GLOBAL STRING'

def greet():
    
    # ENCLOSING
    #name = "I'M ENCLOSING"
    
    def hello():
        
        #LOCAL
        #name = "I'M A LOCAL"
        
        print('Hello '+ name)
    
    hello()
    
greet()


# In[14]:


help(len)


# In[18]:


x = 50

def func(x):
    
    global x
    
    print(f'X is {x}')
    
    # LOCAL REASSIGMENT
    x = 200
    print(f'I JUST LOCALLY CHANGED X TO {x}')


# In[19]:


func(x)


# In[20]:


print(x)


# In[24]:


x = 50

def func():
    
    global x
    
    print(f'X is {x}')
    
    # LOCAL REASSIGMENT ON A GLOBAL VARIABLE
    x = 'NEW VALUE'
    print(f'I JUST LOCALLY CHANGED GLOBAL X TO {x}')

func()


# In[26]:


# BETTER TO NOT USE BLOBAL, JUST PASS THE PARAMETER, RETURN IT AND REASSIGN IT:


# In[31]:


x = 500

def func(x):
    
    print(f'X is {x}')
    
    # LOCAL REASSIGMENT
    x = 'NEW VALUE'
    print(f'I JUST LOCALLY CHANGED GLOBAL X TO -- {x}')
    return x

x = func(x)


# In[29]:


x


# In[ ]:





# In[ ]:





# In[ ]:




