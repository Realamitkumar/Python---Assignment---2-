#!/usr/bin/env python
# coding: utf-8

# # Q1:
# 
# **Create the below pattern using nested for loop in Python**

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# In[46]:


rows = int(input("Enter\n"))
for i in range(rows + 1):
    for j in range(1 , i + 1):
        print("*", end = " " )
    print()  
    
for i in range(rows ,1 ,- 1):
    for j in range(1 , i ):
        print("*", end = " " )
    print()      


# # Q2: 
# **Write a Python program to reverse a word after accepting the input from the user.**

# In[19]:


user = input("Enter Here\n")
user[::-1]

