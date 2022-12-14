#!/usr/bin/env python
# coding: utf-8

# In[5]:


grades = {'Ann': 81, 'Brock': 79, 'Chad': 84, 'Tally': 92, 'Joe': 67}

def get_grade(name):
  if name in grades:
    return grades[name]
  else:
    print("You cannot find this student's name")
grade = get_grade("joey")
print(grade)


# In[9]:


def mean_grade():
  total = 0
  for grade in grades.values():
    total += grade
  return total / len(grades)
mean_grade = mean_grade()
print(mean_grade)


# In[14]:


def num_squares(num):
  n = 0
  while n < num:
    print(n, n**2)
    n += 1
  print("greater than", num)
num_squares(8)


# In[18]:


def numbers(num):
  total = 0
  n = 1
  while n <= num:
    total += n
    n += 1
  print(total)
numbers(1111)


# In[24]:


def Sums(num):
  total = 0
  for n in range(1, num+1):
    total += n
    print(total)
Sums(3)


# In[39]:


from statistics import mean, stdev

def analyze_list(lst):
    mean_lst = mean(lst)
    sum_lst = sum(lst)
    stdev_lst = stdev(lst)
    print("Mean:", mean_lst)
    print("Sum:", sum_lst)
    print("Standard deviation:", stdev_lst)
lst=analyze_list(list(range(1, 100)))


# In[60]:


def mins(a, b, c, d):
    min_val = a
    if b < min_val:
        min_val = b
    if c < min_val:
        min_val = c
    if d < min_val:
        min_val = d
    return min_val
print(mins(500, 28, 1, 1004))


# In[68]:


def constrings(str_list):
    return str_list[0] + str_list[1] + str_list[2]
print(constrings(["Amber ", "was ", "here"]))


# In[ ]:




