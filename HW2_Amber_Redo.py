#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=0
while n<10:
    print(n)
    if n==5:
        break 
    n+=1

    


# In[3]:


n = 0
while n < 5:
  print(n)
  n += 1
else:
  print(n, "is not less than 5")
    


# In[23]:


fruits = ["banana", "orange", "grape", "apple", "mango"]
for fruit in fruits:
  if fruit == "apple":
    print("Is apple a fruit?")
    break
  print("I like " + fruit)


# In[6]:


n = 1
total = 0
while n <= 30:
  total += n
  n += 1
print(total)


# In[12]:


grade = 68
if grade >= 90:
  letter_grade = "A"
elif grade >= 80:
  letter_grade = "B"
elif grade >= 70:
  letter_grade = "C"
elif grade >= 60:
  letter_grade = "D"
else:
  letter_grade = "F"
print(letter_grade)


# In[11]:


grades = {"Fiona": 91, "Rob": 60, "Josie": 76,"Mark": 90, "Steven": 85}


# In[12]:


for kid, grade in grades.items():
  print(kid + ": " + str(grade))


# In[15]:


total = 0
for grade in grades.values():
  total += grade
mean_grade = total / len(grades)

max_grade = max(grades.values())
min_grade = min(grades.values())
print("Mean grade:", mean_grade)
print("Max grade:", max_grade)
print("Min grade:", min_grade)


# In[22]:


for key in grades.keys():
  if "J" in key:
    continue
  print(key)


# In[ ]:





# In[ ]:




