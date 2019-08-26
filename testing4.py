#!/usr/bin/env python
# coding: utf-8

# In[1]:


mylist = [1,2,3]


# In[4]:


for num in range(0,11,2):
    print(num)


# In[6]:


list(range(0,11,2))


# In[8]:


index_count = 0

for letter in 'abcde':
    print("At index {} the letter is {}".format(index_count,letter))
    index_count+=1


# In[9]:


index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count +=1


# In[24]:


# THE ENUMERATE FUNCTION, can take any interable object and returns
#index couter and the element itself

word = 'abcde'
for i,var in enumerate(word):
    print(i,var)


# In[34]:


mylist1 = [1,2,3,4,5,6,7,8,9,10]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]


# In[35]:


for item in zip(mylist1,mylist2,mylist3):
    print(item)


# In[36]:


list(zip(mylist1,mylist2,mylist3))


# In[39]:


'x' in [1,2,3] # Check if an object is in a list


# In[40]:


'x' in ['x','y']


# In[41]:


'a' in 'a world'


# In[42]:


'mykey' in {'mykey':345}


# In[43]:


d = {'mykey':345}


# In[44]:


345 in d.keys()


# In[45]:


345 in d.values()


# In[47]:


mylist = [10,20,30,40,100]


# In[48]:


min(mylist)


# In[49]:


max(mylist)


# In[50]:


# To IMPORTING functions from a Library:
from random import shuffle


# In[51]:


a = []
for n in range(11):
    a.append(n)


# In[52]:


a


# In[53]:


shuffle(a)


# In[54]:


a


# In[55]:


shuffle(a)


# In[56]:


a


# In[57]:


from random import randint


# In[58]:


randint(0,100)


# In[59]:


randint(0,100)


# In[60]:


randint(0,100)


# In[61]:


mynum = randint(0,100)


# In[62]:


mynum


# In[64]:


res = input("Enter a number here: ")


# In[65]:


type(res)


# In[66]:


float(res)


# In[67]:


int(res)


# In[68]:


res = int(input("Enter a number here: "))


# In[69]:


type(res)


# In[ ]:





# In[ ]:





# In[70]:


mystring = 'hello'


# In[71]:


mylist = []

for letter in mystring:
    mylist.append(letter)


# In[72]:


mylist


# In[75]:


mylist = [letter for letter in mystring] # FLATTING OUT FOR Loop


# In[74]:


mylist


# In[82]:


mylist = [num**2 for num in range(0,11)]


# In[80]:


mylist


# In[85]:


mylist = [x**2 for x in range(0,11) if x%2==0]


# In[86]:


mylist


# In[89]:


celcius = [0,10,20,34.5,38]
farenheit = [(9/5)*temp +32 for temp in celcius]


# In[90]:


farenheit


# In[95]:


farenheit = []

for temp in celcius:
    farenheit.append((9/5)*temp+32)


# In[96]:


farenheit


# In[97]:


#IF ELSE inside a List Comprehension:
result = [x if x%2==0 else 'ODD' for x in range(0,11)]
print(result)


# In[100]:


mylist = []

for x in [2,5,6]:
    for y in [1,10,1000]:
        mylist.append(x*y)
print(mylist)


# In[101]:


mylist = [x*y for x in [2,4,6] for y in [1,10,100]]
print(mylist)
