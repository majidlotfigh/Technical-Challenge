#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sum of all the multiples of 3 or 5 below 1000
nums = [3, 5]

total = 0
for i in range(0,1000):
    if i%3 == 0 or i%5 == 0:
        total += i
print('the sum of all the multiples of 3 or 5 below 1000 is:')
print(total)


# In[2]:


#sum of the even-valued numbers of Fibonacci which do not exceed four million
even= 0
odd= 1
total = 0
while odd < 4000000:
    even, odd = odd, even + odd
    if even % 2:
        continue
    total += even
print('sum of the even-valued numbers of Fibonacci which do not exceed four million is:')
print(total)


# In[ ]:




