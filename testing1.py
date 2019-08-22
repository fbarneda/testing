#!/usr/bin/env python
# coding: utf-8

# In[1]:


2-1


# In[2]:


7/4


# In[3]:


7 % 4


# In[4]:


23 %2


# In[5]:


20%3


# In[6]:


2**3


# In[9]:


mycalc=(2 +10) * (10 +3)


# In[10]:


print(mycalc)


# In[11]:


a = 10


# In[12]:


a + a


# In[13]:


a = a + a


# In[14]:


a


# In[15]:


type(a)


# In[16]:


my_income = 100

tax_rate = 0.1

my_taxes = my_income * tax_rate


# In[17]:


my_taxes


# In[18]:


'hello'


# In[19]:


"world"


# In[20]:


print("hello world")


# In[21]:


print("hello \nworld")


# In[22]:


len('1234')


# In[23]:


mystring = "Hello World"


# In[24]:


mystring


# In[27]:


mystring[0]


# In[28]:


mystring[-2]


# In[29]:


mystring[-3]


# In[30]:


mystring


# In[34]:


del my_income


# In[35]:


del my_taxes


# In[36]:


del mycalc


# In[38]:


mystring[2:]


# In[39]:


mystring[:-2]


# In[40]:


mystring = "abcdefghijk"


# In[44]:


print(mystring[:3])
"""Up to BUT not including, so 3 letters, no 'd'"""


# In[45]:


mystring[3:6]


# In[48]:


mystring[::2]


# In[49]:


mystring[::-1]


# In[55]:


w = ""
for letter in mystring:
    w = reversed(w)+letter
print(w)


# In[61]:


name = "Sam"


# In[62]:


name = "P"+name[1:]


# In[63]:


name


# In[64]:


letter = 'z'


# In[65]:


letter*10


# In[66]:


2+3


# In[67]:


'2'+'3'


# In[68]:


x = 'Hello World'


# In[69]:


x.upper()


# In[71]:


x.lower()


# In[72]:


x.split()


# In[73]:


x = "This is a string"


# In[78]:


x.split()


# In[85]:


"Sammy"[2:]


# In[86]:


print("this is a string {}".format('INSERTED'))


# In[88]:


print("The {2} {1} {0}".format('fox','brown','quick'))


# In[89]:


print("The {q} {b} {f}".format(f='fox',b='brown',q='quick'))


# In[90]:


result = 100/777


# In[91]:


result


# In[92]:


print("The result was {}".format(result))


# In[96]:


print("The result was {r:10.3f}".format(r=result))


# In[ ]:





# In[97]:


name = "Ferran"


# In[99]:


print("Hello, his name is {}.".format(name))


# In[102]:


print(f"Hello, his name is {name}")


# In[103]:


name = "Sam"
age = 3
print(f"{name} is {age} years old!")


# In[ ]:





# In[104]:


my_list = [1,2,3]


# In[105]:


my_list = ['STRING',200,1.2]


# In[106]:


print(my_list)


# In[107]:


len(my_list)


# In[108]:


my_list = ['one','two','three']


# In[109]:


my_list[0]


# In[110]:


my_list[1:]


# In[117]:


another_list = list(my_list[1:])


# In[118]:


another_list.append(my_list[0])


# In[113]:


type(my_list[1:])


# In[114]:


type(my_list[0])


# In[119]:


print(another_list)


# In[120]:


my_numbers = ['one','two','three','four','five']


# In[121]:


my_numbers[0] = 'ONE'


# In[122]:


my_numbers


# In[123]:


my_numbers.append("SIX")


# In[124]:


my_numbers


# In[125]:


my_numbers.append("SEVEN")


# In[126]:


my_numbers


# In[127]:


my_numbers.pop()


# In[128]:


my_numbers


# In[129]:


popped_item = my_numbers.pop()


# In[130]:


popped_item


# In[131]:


my_numbers.pop(0)


# In[132]:


my_numbers


# In[133]:


new_list = ['a','e','x','b','c']
num_list = [4,1,8,3]


# In[134]:


new_list.sort()


# In[135]:


new_list


# In[136]:


num_list


# In[137]:


num_list.sort()


# In[138]:


num_list


# In[140]:


num_list.reverse()


# In[141]:


num_list

