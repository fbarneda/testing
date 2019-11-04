#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# PRINT AND VARIBLES #################################################################


# In[ ]:


age = 30


# In[ ]:


print(age) 


# In[ ]:


print(30) 


# In[ ]:


# NUMBERS #################################################################


# In[ ]:


age = 35 #INTEGER


# In[ ]:


PI = 3.14159 #FLOAT


# In[ ]:


floatdivison = 12/3


# In[ ]:


print(floatdivison) 


# In[ ]:


integerdivision = 12//3 # // removes the decimals, NOT rounding


# In[ ]:


integerdivision


# In[ ]:


# NUMBERS AND DIVISIONS - MOD #################################################################


# In[ ]:


myintegerdevision = 13//5


# In[ ]:


print(myintegerdevision) 


# In[ ]:


remainder = 13 % 5


# In[ ]:


print(remainder) 


# In[ ]:


x = 37
x = x % 2
print(x) # This is an odd number


# In[ ]:


# STRINGS #################################################################


# In[ ]:


my_string = "Hello, World!"


# In[ ]:


print(my_string)


# In[ ]:


string_with_quotes = "Hello, it's me."


# In[ ]:


another_with_quotes = "He said \"You are amazing!\" yesterday"


# In[ ]:


print(another_with_quotes)


# In[ ]:


multiline = """Hello, world.
My name is Ferran. Welcome to my program."""


# In[ ]:


print(multiline)


# In[ ]:


name = "Ferran"
greeting = "Hello " + name
print(greeting)


# In[ ]:


age = 29
age_as_str = str(age)
print("I am " + age_as_str)


# In[ ]:


# STRING FORMATTING #################################################################


# In[ ]:


age = 29
age_as_str = str(age)
print(f"I am {age_as_str}") # STRING FORMATTING - f string available from Python 3.6+


# In[ ]:


name = "Ferran"
greeting = f"How are you, {name}?"
print(greeting)


# In[ ]:


name = "Bob"


# In[ ]:


print(greeting)


# In[ ]:


name = "Ferran"


# In[ ]:


final_greeting = "How are you, {}?"


# In[ ]:


ferran_greeting = final_greeting.format(name)


# In[ ]:


print(ferran_greeting)


# In[ ]:


name = "Ferran"
final_greeting = "How are you, {}?"
ferran_greeting = final_greeting.format(name)
print(ferran_greeting)


# In[ ]:


name = "Ferran"
final = "How are you, {}?".format(name)
print(final)


# In[ ]:


# USER INPUT #################################################################


# In[ ]:


my_name = "Ferran"
your_name = "Rolf"
print(f"Hello {your_name}, my name is {my_name}.")


# In[ ]:


my_name = "Ferran"
your_name = input("Please enter your name")
print(f"Hello {your_name}, my name is {my_name}.")


# In[2]:


age = int(input("Enter your age: "))
print(f"You have lived for {age * 12} months.)")
# You want to give a meaninful name to a varible,
# better use {months} -- months = age_num * 12, than just the multiplication.


# In[5]:


seconds_lived = int(input("What is your age?"))*12*30*24*60*60
print(f"I have lived for {seconds_lived} seconds")


# In[8]:


x = input("enter num")
double = x * 2
print(f"your num doubled is {x} ")


# In[1]:


# BOOLEANS #################################################################


# In[2]:


truthy = True


# In[3]:


Falsy = False


# In[4]:


age = 20
is_over_age = age>18


# In[5]:


is_over_age


# In[6]:


is_twnety = age == 20


# In[7]:


is_twnety


# In[10]:


my_number = 5
user_number = int(input("Enter a number: "))
matches = my_number == user_number


# In[11]:


# AND and OR #################################################################


# In[12]:


age = int(input("Enter your age: "))


# In[13]:


can_learn_programming = age > 0 and age < 150


# In[14]:


can_learn_programming


# In[17]:


print(f"You can learn programming: {can_learn_programming}")


# In[26]:


age = int(input("Enter your age: "))
usually_working = age < 18 or age > 65
print(f"At {age}, you are usually not working: {usually_working}")


# In[27]:


print(bool(35))


# In[28]:


print(bool("Rolf"))


# In[29]:


print(bool(0))


# In[30]:


x = True and False


# In[31]:


print(x)


# In[34]:


#AND gives you the first value if it is FALSE, otherwise it gives you the SECOND value


# In[35]:


x = 35 and 0
print(x)


# In[36]:


#OR gives you the first value if it is True, otherwise it gives you the second value.


# In[38]:


x = 35 or 0
print(x)


# In[43]:


name = input("Enter your name ")
surname = input("Enter your surname ")
greeting = name or f"Mr. {surname}"
print(greeting)


# In[44]:


print(not True)


# In[46]:


# not - will give you back the oposite Boolian


# In[47]:


cmp = 15>20 or 17<20
print(cmp)


# In[48]:


x = True
cmp = x and 18
print(cmp)


# In[50]:


age = int(input("Enter your age: "))
side_job = True
print(age > 18 and age)


# In[51]:


# LISTS #################################################################


# In[53]:


friends = ["Rolf","Bob","Anne"]


# In[54]:


friends[0]


# In[55]:


len(friends)


# In[7]:


friends = [
           ["Rolf",24],
           ["Bob",30],
           ["Anne",27]
          ]


# In[8]:


friends[0][0]


# In[4]:


friends.append("Jen")


# In[62]:


friends


# In[5]:


friends.remove(["Bob",30])


# In[6]:


friends


# In[9]:


# TUPLES #################################################################


# In[18]:


short_tuple = "Rolf","Bob" #When you add a COMMA it turns it into a TUPLE


# In[11]:


type(short_tuple)


# In[12]:


a_bit_clearer = ("Rolf","Bob")


# In[13]:


type(a_bit_clearer)


# In[14]:


tuple_in_a_list = [("Rolf","Bob")]


# In[17]:


type(tuple_in_a_list[0][0])


# In[22]:


#the only way to add an element to a tuple is to define a new variable and add a new element, ie:
tuple_friends = ("Rolf","Bob")
add_a_friend = tuple_friends + ("Jen",)


# In[23]:


add_a_friend


# In[24]:


# SETS #################################################################


# In[25]:


# They don't hold order and they don't contain duplicate elements


# In[26]:


# { } WILL BECOME A SET // [ ] will BECOME A LIST // ( ) WILL BECOME A TUPLE


# In[27]:


art_friends = {"Rolf","Anne"}


# In[28]:


science_friends = {"Jen","Charlie"}


# In[29]:


art_friends.add("Jen")


# In[30]:


art_friends


# In[31]:


art_friends.add("Jen")


# In[32]:


art_friends


# In[33]:


#Nothing added, no duplicates


# In[34]:


art_friends.remove("Jen")


# In[35]:


art_friends


# In[51]:


# WHY SETS ARE USEFUL COMPARED TO LISTS AND TUPLES ##############################################
# You use them ONLY becuase you can perform some operations


# In[38]:


art_friends.add("Jen")


# In[39]:


art_friends


# In[40]:


science_friends


# In[52]:


art_but_not_science = art_friends.difference(science_friends) 
#elements on one list that are not in the another list -- difference


# In[42]:


art_but_not_science


# In[43]:


science_but_not_art = science_friends.difference(art_friends)


# In[44]:


science_but_not_art


# In[54]:


not_in_both = art_friends.symmetric_difference(science_friends)
#elements that are not in both lists -- symmetric_difference


# In[46]:


not_in_both


# In[53]:


art_and_science = art_friends.intersection(science_friends)
#elements that are in both lists -- intersection


# In[48]:


art_and_science


# In[55]:


all_friends = art_friends.union(science_friends)
#all elements that are in both lists -- union


# In[50]:


all_friends


# In[67]:


# DICTIONARY #################################################################
# Useful when you have a key and you want to get a value back, like in a regular dictionary
# They KEEP ORDER, in which you added keys to them, 1st key added will always be 1st
# In Python 3.7 order is KEPT - before that the order was not guaranteed


# In[58]:


friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}


# In[59]:


print(friend_ages["Rolf"])


# In[60]:


# Accessing a key in a dictionary and setting a value in it:
friend_ages["Bob"] = 20


# In[61]:


friend_ages


# In[63]:


friend_ages["Rolf"] = 25


# In[64]:


friend_ages


# In[69]:


# You have multiple friends and you want to store muliple details about each friend
# best way to do it is to use a LIST or TUPLE of DICTIONARIES, ie:
friends = (
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27}
)


# In[75]:


print(f'My name is {friends[0]["name"]} and I am {friends[0]["age"]} years old.')


# In[78]:


friends = [
    ("Rolf Smith",24), 
    ("Adam Wool",30), 
    ("Anne Pun",27)
]


# In[79]:


friend_ages = dict(friends)


# In[80]:


print(friend_ages)


# In[81]:


type(friend_ages)


# In[83]:


# LENGHT AND SUM FUNCTION #################################################################


# In[84]:


grade = [80,75,90,100]


# In[85]:


total = sum(grade)


# In[86]:


total


# In[88]:


lenght = len(grade) # Lenght of list


# In[89]:


avg = total / lenght


# In[90]:


print(avg)


# In[126]:


lottery_numbers = {13, 21, 22, 5, 8}
"""
A player looks like this:
{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}
Define a list with two players (you can come up with their names and numbers).
"""
players = [
    {'name': 'Ferran','numbers': {1, 22, 3, 4, 5}},
    {'name': 'Jenny','numbers': {1, 2, 33, 4, 5}}
]
"""
For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers. We still cannot use f-strings in this exercise.
You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
"""
player_name_one = str(players[0]['name'])
player_name_two = str(players[1]['name'])

intersection_p_one = len((lottery_numbers.intersection(players[0]['numbers'])))
intersection_p_two = len((lottery_numbers.intersection(players[1]['numbers'])))

print("Player {} got {} numbers right".format(player_name_one,intersection_p_one))
print("Player {} got {} numbers right".format(player_name_two,intersection_p_two))


# In[127]:


# JOINING A LIST #################################################################


# In[128]:


friends = ["Rolf","Anne","Charlie"]


# In[134]:


print(f"My friends are {friends}.")


# In[140]:


comma_separated = ", ".join(friends)


# In[142]:


print(f"My friends are {comma_separated}.")


# In[ ]:




