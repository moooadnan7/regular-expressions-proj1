#!/usr/bin/env python
# coding: utf-8

# In[39]:


with open("re.txt") as x:
    text=x.read()
import re
names=[]
emails=[]
numbers=[]
for i in text.splitlines():
    name=re.findall(r"[Mr.MsMrs]*\s[ a-z A-Z]*\s[ a-z A-Z]+\s",i)
    number=re.findall(r"\d?-?\(?\d{3}\)?-?\d{3}-\d{4}",i)
    email=re.findall(r"[\w+\.-]+@[a-z\d\.-]+\.[a-z]+",i)
    emails.extend(email)
    names.extend(name)
    numbers.extend(number)
print("names :",names)
print("emails :",emails)
print("numbers :",numbers)

