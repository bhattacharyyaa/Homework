#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np

ar = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11,12]])
new_ar = ar * 2
print(new_ar)


# In[4]:


for row in ar:
    for element in row:
        print(element, end=" ")
    print()


# In[9]:


for element in ar.flat:
    print(element, end=" ")


# In[10]:


mport matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6]
y = [5, 6, 7, 8, 9, 10]
plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line plot")
plt.show()


# In[13]:


x = [3, 6, 9, 12]
y = [2, 8, 1, 10]
plt.plot(x, y, marker="o")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line plot with markers")
plt.show()


# In[21]:


x1 = [0, 1, 2, 3, 4, 5]
y1 = [2, 4, 6, 14, 10, 12]
x2 = [6, 7, 8, 9, 10]
y2 = [16, 18, 20, 22, 24]
plt.plot(x1, y1, linestyle="-", color="red", marker="o", markersize=10, markerfacecolor="green")


plt.show()


# In[54]:


x1 = [1, 2, 3]
y1 = [3, 4, 5]
x2 = [1, 3, 5]
y2 = [4, 8, 12]
x3 = [3, 4, 5]
y3 = [6, 12, 18]
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.show()


# In[50]:


marks = {'Andy':88, 'Amy':66, 'James': 90, 'Jules': 55, 'Arthur': 77}
plt.figure()
for student, grade in marks.items():
    plt.bar(student, grade)
plt.title("Student Grades")
plt.show()


# In[49]:


fig = plt.figure()
grades = [grade for grade in marks.values()]
students = [student for student in marks.keys()]
plt.pie(grades, labels=students)
plt.legend()
plt.title("Student Grades")
plt.show()


# In[5]:


fig, axes = plt.subplots(nrows=2, ncols=3)

axes[0, 0].set_title("Multiple lines")
axes[0, 1].set_title("Bar chart")
axes[0, 2].set_title("Pie chart")
axes[1, 0].set_title("Grid")
axes[1, 1].set_title("Scatter plot")
axes[1, 2].set_title("Histogram")



# In[ ]:





# In[ ]:




