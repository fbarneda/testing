#!/usr/bin/env python
# coding: utf-8

# In[33]:


class Dog():
    
    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal'
    
    def __init__(self,breed,name,spots):
        
        # Atributes - These are USER DEFINED ATTRIBUTES
        # We take in the argument
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name
        
        # Expect boolean True/False
        self.spots = spots
    
    # OPERATIONS / ACTIONS == METHODS
    # DIFFERENCE BETWEEN METHOD AND FUNCTION:
    # A method is a function that is INSIDE a Class that will
    # work with the object in some way.
    def bark(self,number):
        print("WOOF! My name is {} and I bark {} times.".format(self.name,number))


# In[34]:


my_dog = Dog(breed='Lab',name='Sam',spots=False)


# In[18]:


type(my_dog)


# In[19]:


my_dog.species


# In[20]:


my_dog.name


# In[35]:


my_dog.bark(3)


# In[36]:


######################################


# In[54]:


class Circle():
    
    # CLASS OBJECT ATTRIBUTE
    
    pi = 3.14
    
    def __init__(self,radius=1):
        
        self.radius = radius
        # we use here radius(this is passed in), not self.radius
        # here we can use Circle.pi instead of self.pi, which is
        # noramlly better to show this is a class object attribute
        self.area = radius * radius * self.pi
        
    #METHOD
    def get_circumference(self):
        return self.radius * self.pi * 2


# In[55]:


my_circle = Circle(30)


# In[56]:


my_circle.pi


# In[57]:


my_circle.radius


# In[58]:


my_circle.area


# In[59]:


my_circle.get_circumference()


# In[60]:


######################################


# In[67]:


class Animal():
    
    def __init__(self):
        print("Animal Created!")
    
    def who_am_i(self):
        print("I am an animal")
    
    def eat(self):
        print("I am eatiing")


# In[75]:


class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
        
    #overriting method now:
    def who_am_i(self):
        print("I am a DOG")
        
    #Adding methods
    def bark(self):
        print("WOOF!")


# In[76]:


myanimal = Animal()


# In[77]:


my_dog = Dog()


# In[74]:


my_dog.who_am_i()


# In[78]:


my_dog.bark()


# In[79]:


######################################


# In[104]:


class Dog():
    
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return self.name + " says woof!"


# In[109]:


class Cat():
    
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return self.name + " says meow!"


# In[110]:


dog = Dog("dog")
cat = Cat("cat")


# In[111]:


print(dog.speak())


# In[112]:


print(cat.speak())


# In[115]:


for pet in [dog,cat]:
    print(type(pet))
    print(pet.speak())


# In[119]:


# This is an example of a Base class, not to be used, but imported
class Animal():
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


# In[117]:


myanimal = Animal('Fred')


# In[118]:


myanimal.speak()


# In[122]:


# here we crate a class dog and we import animal:
class Dog(Animal):
    
    # No need to add the init constructor
    
    # here we overrite the speak method from Animal
    def speak(self):
        return self.name + " says woof!"


# In[123]:


class Cat(Animal):
        
    # No need to add the init constructor
    
    # here we overrite the speak method from Animal
    def speak(self):
        return self.name + " says meow!"


# In[124]:


fido = Dog("Fido")


# In[125]:


isis = Cat("Isis")


# In[126]:


print(fido.speak())


# In[127]:


print(isis.speak())


# In[128]:


######################################


# In[129]:


mylist = [1,2,3]


# In[130]:


len(mylist)


# In[131]:


class Sample():
    pass


# In[132]:


mysample = Sample()


# In[133]:


len(mysample)


# In[134]:


print(mysample)


# In[135]:


print(mylist)


# In[136]:


######################################


# In[163]:


class Book():
    
    def __init__(self,title,author,pages):
        
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return f"{self.title} by {self.author}"
        
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("A book object has been deleted")


# In[168]:


b = Book("Python rockss","Jose",200)


# In[169]:


print(b)


# In[170]:


len(b)


# In[171]:


del b

