#!/usr/bin/env python
# coding: utf-8

# In[1]:


2 == 2


# In[2]:


2 == 1


# In[4]:


'hello' == 'bye'


# In[5]:


2.0 == 2


# In[6]:


3 != 3


# In[7]:


4 != 5


# In[8]:


2>1


# In[9]:


1<2


# In[10]:


2<=2


# In[11]:


2>=2


# In[ ]:





# In[12]:


1 < 2 < 3 # 1 is less than 2 and 2 is less than 3


# In[13]:


1 < 2 and 2 < 3 # 1 is less than 2 and 2 is less than 3


# In[14]:


'h' == 'h' and 2 == 2


# In[16]:


1 == 1 or 2 == 2


# In[17]:


1 == 0 or 2 == 2


# In[19]:


1 == 1.2 or 2 == 0


# In[20]:


1 == 1


# In[21]:


not 1 == 1 # asking for the OPPOSITE Boolean


# In[22]:


not (1 == 1) # asking for the OPPOSITE Boolean


# In[25]:


hungry = True


# In[27]:


if hungry:
    print("I'm hungry!")
else:
    print("I'm not hungry!")


# In[32]:


loc = 'Store'

if loc == 'Auto Shop':
    print("Cars are cool!")
elif loc == 'Bank':
    print("Money is cool")
elif loc == 'Store':
    print("Welcome to the store!")
else:
    print("I do not know much.")


# In[34]:


name = 'ammy'

if name == 'Frankie':
    print("Hello Frankie!")
elif name == 'Sammy':
    print("Hello Sammy")
else:
    print("I don't know you")


# In[ ]:





# In[ ]:





# In[35]:


mylist = [1,2,3,4,5,6,7,8,9,10]


# In[36]:


for number in mylist:
    print(number)


# In[42]:


for number in mylist:
    if number % 2 == 0:
        print(number)
    else:
        print(f"{number} odd")


# In[43]:


num_sum = 0

for num in mylist:
    num_sum += num
print(num_sum)


# In[46]:


for letter in 'Hello World':
    print(letter)


# In[47]:


t = (1,2,3)

for item in t:
    print(item)


# In[48]:


mylist = [(1,2),(3,4),(5,6),(7,8)]


# In[49]:


len(mylist)


# In[55]:


# TUPPLE UNPACKING
for a,b in mylist:
    print('(' + str(a)+','+str(b) + ')')


# In[54]:


for item in mylist:
    print(item)


# In[66]:


d = {'k1':1,'k2':2,'k3':3}
for key,value in d.items():
    print(f"{key} value: {value}")


# In[ ]:





# In[ ]:





# In[73]:


x = 0

while x < 5:
    print(f"The current value of x is {x}")
    x += 1
else:
    print("Else is not less than 5")


# In[ ]:





# In[ ]:





# In[75]:


x = [1,2,3]

for item in x:
    pass


# In[83]:


x = [1,2,3]

for item in x:
    if item == 1:
        pass
    print(item)


# In[90]:


x = 0
while x < 5:
    print(x)
    x+=1
    if x == 2:
        break