#!/usr/bin/env python
# coding: utf-8

# In[1]:


mylist = [1,2,3]


# In[2]:


mylist.append(4)


# In[3]:


mylist


# In[4]:


mylist.pop()


# In[5]:


mylist


# In[6]:


help(mylist.insert)


# In[ ]:





# In[12]:


def name_function():
    '''
    DOCSTRING here, info about the function.
    Input: no input...
    '''
    print("Hello")


# In[11]:


name_function()


# In[22]:


def say_hello(name="there"):
    print('Hello ' + name)


# In[24]:


say_hello()


# In[26]:


res = say_hello("Ferran")


# In[29]:


res # res is JUST printing out NOT RETURNING anything (NoneType)


# In[28]:


type(res)


# In[30]:


def say_hello2(name="there"):
    return('Hello ' + name)


# In[32]:


res2 = say_hello2("Fer")


# In[33]:


res2


# In[34]:


def add(n1,n2):
    return n1+n2


# In[35]:


result  = add(20,30)


# In[36]:


result


# In[37]:


# Find out if the work "dog" is in a string?


# In[40]:


def dog_check(mystring):
    if 'dog' in mystring.lower():
        return True
    else:
        return False


# In[42]:


dog_check("Hello Dog")


# In[43]:


# SINCE 'if 'dog' in mystring' RETURNS A BOOLEAN, WE DON'T NEED THE 2 RETURNS


# In[44]:


def dog_check(mystring):
    return 'dog' in mystring.lower()


# In[45]:


dog_check("Hello Dog")


# In[60]:


def pig_latin(word):
    if word[0].lower() in 'aeiou':
        res = word+'ay'
    else:
        res = word[1:]+word[0]+'ay'
    return res


# In[61]:


pig_latin("fapple")
