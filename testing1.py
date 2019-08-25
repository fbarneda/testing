#!/usr/bin/env python
# coding: utf-8

# In[1]:


dic_key = {'key1':'value1','key2':'value2'}


# In[2]:


dic_key


# In[3]:


dic_key['key2']


# In[4]:


prices_lookup = {'apples':2.99,'oranges':1.99,'milk':5.80}


# In[5]:


prices_lookup['apples']


# In[7]:


d = {'k1':123,'k2':[0,1,2],'k3':{'insideKey':100}}


# In[8]:


d['k3']['insideKey']


# In[10]:


d['k2'][-1]


# In[11]:


d = {'key1':['a','b','c']}


# In[13]:


d['key1'][-1] = d['key1'][-1].upper()


# In[14]:


d


# In[15]:


d = {'k1':100,'k2':200}


# In[16]:


d


# In[17]:


d['k3'] = 300


# In[18]:


d


# In[19]:


d['k1'] = 'NEW VALUE'


# In[20]:


d


# In[21]:


d = {'k1': 100, 'k2': 200, 'k3': 300}


# In[22]:


d.keys()


# In[23]:


for key in d.keys():
    print(key)


# In[24]:


d.values()


# In[25]:


d.items()


# In[ ]:





# In[26]:


# TUPLES


# In[27]:


t = (1,2,3)


# In[28]:


mylist = [1,2,3]


# In[29]:


type(t)


# In[30]:


type(mylist)


# In[31]:


t = ('one',2)


# In[32]:


t[0]


# In[33]:


t[-1]


# In[34]:


t = ('a','a','b')


# In[46]:


t.count('a') # COUNT number of elements in tuple


# In[38]:


t.index('a')


# In[39]:


t.index('b')


# In[40]:


t


# In[42]:


mylist[0] = "NEW"


# In[43]:


mylist


# In[44]:


t[0] = "NEW"


# In[ ]:





# In[45]:


# SETS


# In[47]:


s = set()


# In[48]:


type(s)


# In[49]:


s


# In[50]:


s.add(1)


# In[51]:


s


# In[52]:


s.add(2)


# In[53]:


s


# In[54]:


s.add(2)


# In[55]:


s


# In[56]:


mylist = [1,1,1,1,2,2,2,2,2,3,3]


# In[59]:


set(mylist) # WE CAST it to a SET and we have only the UNIQUE values, UNORDERED


# In[ ]:





# In[60]:


# BOOLS


# In[61]:


True


# In[62]:


False


# In[63]:


type(False)


# In[64]:


1 > 2


# In[65]:


1==1


# In[71]:


b = None


# In[ ]:





# In[72]:


# FILES


# In[73]:


get_ipython().run_cell_magic('writefile', 'myfile.txt', 'Hello this is a text file\nthis is the second line\nthis is the third line')


# In[74]:


myfile = open('myfile.txt')


# In[75]:


myfile = open('whoops.txt')


# In[76]:


pwd


# In[77]:


myfile = open('myfile.txt')


# In[78]:


myfile.read()


# In[79]:


myfile.read()


# In[82]:


myfile.seek(0)


# In[83]:


contents = myfile.read()


# In[84]:


contents


# In[90]:


myfile.seek(0)


# In[91]:


myfile.readlines() # grab all lines in a list, each element is a line


# In[94]:


myfile.close() # best practise to close the process


# In[96]:


myfile = open('myfile.txt') # old way of doing things


# In[97]:


# new way of doing things:


# In[98]:


with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()
# with that, because of the indentation, no need to close the file


# In[99]:


contents


# In[100]:


with open('myfile.txt',mode='r') as myfile:
    contents = myfile.read()


# In[101]:


contents


# In[102]:


with open('myfile.txt',mode='w') as myfile:
    contents = myfile.read()


# In[6]:


get_ipython().run_cell_magic('writefile', 'my_new_file.txt', 'ONE ON FIRST\nTWO ON SECOND\nTHREE ON THIRD')


# In[7]:


with open('my_new_file.txt') as f:
    print(f.read())


# In[8]:


with open('my_new_file.txt',mode='a') as f:
    f.write('FOUR ON FOURTH')


# In[4]:





# In[9]:


with open('my_new_file.txt') as f:
    print(f.read())


# In[10]:


with open('qwertyuiop.txt',mode='w') as f:
    f.write('I CREATED THIS FILE!')


# In[12]:


with open('qwertyuiop.txt',mode='r') as f:
    print(f.read())

