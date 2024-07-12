#!/usr/bin/env python
# coding: utf-8

# In[ ]:


3 + 7


# In[ ]:


print("hello")


# In[ ]:


name = "Lawrence"
age = 28


# In[ ]:


print(age)


# In[ ]:


# Initiates comment


# In[ ]:


# Can echo without 'print'
name


# # Variables and Values

# In[ ]:


# Variables can be used in calculations
print(age)
age = age + 3
print(age)


# In[ ]:


# Order of operations matters!
first = 1
second = first*5
first = 2

print(first)
print(second)


# In[ ]:


# Values have types. Types affect what you an do with them.
print(5 - 3)
# print("hello" - "h")


# In[ ]:


# 'len' function provides the length of characters in the paranthese
print(len("hello"))
# print(len(6))


# ## Challenge 1
# Explain what each operator does

# In[ ]:


# '//' function for floor operator; gives you main part of answer after division. For example this would normally result
# in 1 remainder 2, so only 1 will show.
print(5//3)

# '/' function for division
print(5/3)

# '%' function is opposite of floor operator where it gives you the remainder instead of the whole after division.
print(5%3)


# # Getting Help

# In[ ]:


# Rounding numbers is built in
round(3.14159)


# In[ ]:


# Rounds the number before the combo to 2 decimal places
round(3.14159,2)


# In[ ]:


# 'help' function
help(round)


# In[ ]:


# All functions return a new value
rounded_pi = round(3.14159,2)
print(rounded_pi)


# ## Challenge 2
# In what order do the operations happen?

# In[ ]:


help(min)


# In[ ]:


help(max)


# In[ ]:


# Smallest value assigned to 'radiance' variable
radiance = 1.0

# Maximum value of the MINIMUM of a submitted function
radiance = max(2.1,2.0+min(radiance, 1.1*radiance-0.5))

print(radiance)


# In[ ]:


# Break down these operations
radiance = 1.0

# 'arg' is argument
min_arg_2 = 1.1 * radiance - 0.5
print ("Min arg 2 =", min_arg_2)

min_result = min(radiance, min_arg_2)
print("Min result =", min_result)

radiance = max(2.1, 2.0 + min_result)
print(radiance)


# In[ ]:




