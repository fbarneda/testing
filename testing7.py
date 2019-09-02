#!/usr/bin/env python
# coding: utf-8

# In[19]:


# MAP function


# In[1]:


def square(num):
    return num**2


# In[2]:


my_nums = [1,2,3,4,5]


# In[6]:


map(square,my_nums) # WE HAVE TO ITERATE THROUGH THE OBJECT


# In[5]:


for item in map(square,my_nums):
    print(item)


# In[7]:


# ANOTHER WAY


# In[8]:


list(map(square,my_nums))


# In[9]:


# ANOTHER EXAMPLE, MORE COMPLEX


# In[10]:


def splicer(mystring):
    if len(mystring)%2==0:
        return "EVEN"
    else:
        return mystring[0]


# In[11]:


names = ['Andy','Eve','Sally']


# In[12]:


list(map(splicer,names))


# In[ ]:





# In[13]:


# FILTER function


# In[14]:


def check_even(num):
    return num%2==0


# In[15]:


mynumbers = [1,2,3,4,5,6]


# In[16]:


filter(check_even,mynumbers)


# In[17]:


list(filter(check_even,mynumbers))


# In[18]:


for n in filter(check_even,mynumbers):
    print(n)


# In[ ]:





# In[20]:


# LAMBDA EXPRESSION


# In[22]:


def square(num):
    result = num**2
    return result


# In[23]:


square(4)


# In[26]:


lambda num: num**2


# In[27]:


list(map(lambda num: num**2, my_nums))


# In[29]:


list(map(lambda num: num%2==0,mynumbers))


# In[30]:


list(filter(lambda num: num%2==0,mynumbers))


# In[31]:


names


# In[36]:


(list(map(lambda name: name[0],names)))


# In[ ]:
