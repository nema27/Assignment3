##########################################
#### EXERCISE 1 30 MARKS############
###########################################
#
# Student name: L.Nemathaga
# Student no: 230451001
# Date: 17/06/24
# Assignment 3: Python
#
# Time to review all the basic data types we learned! This should be a
# relatively straight-forward and quick assignment.
##################
## Problem 1 - 10 Points##
##################

# Given the string:
s= 'fullstackslp'

# Use indexing to print out the following:
# 'f'
print(s[-12])

# 'p'
print(s[-1])

# 'stack'
print(s[4:9])

# 'slp'
print(s[9:12])

# 'cks'
print(s[7:10])

# Bonus: Use indexing to reverse the STRINGS
print(s[::-1])

##############
## Problem 2 - LISTS - 5 Marks##
##############

# Using keys and indexing, grab 'hello' from the following Dictionaries:

d1 = {'simple_key':'hello'}
print(d1['simple_key'])

d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])

###############
## Problem 4 - SETS - 4 Marks##
###############
# USe a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
#Your code here:
unique_values = set(mylist) 
print(unique_values)
###############
## Problem 5 - FORMATTING - 5 Marks##
###############
# You are given the variables:

age = 45
name = "Kyle"

# Use print formatting to print the following string
# "Hello my dog's name is Kyle and he looks 45 years old"
print("Hello, my dog's name is {} and he looks {} years old".format(name, age))
