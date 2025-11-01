#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Task 1

#Getting the values from user
num1 = int(input("Enter the number 1 :"))
num2 = int(input("Enter the number 2 :"))

#Basic mathematical operation
add = num1+num2
sub = num1-num2
Prod = num1*num2
Divi = num1/num2
mod = num1%num2
Expo = num1**num2

#Result
print(f"The additon of {num1} and {num2} is {add}.")
print(f"The subtraction of {num1} and {num2} is {sub}.")
print(f"The Multiplication of {num1} and {num2} is {Prod}.")
print(f"The Division of {num1} and {num2} is {Divi}.")
print(f"The Modulus of {num1} and {num2} is {mod}.")
print(f"The Exponentiation of {num1} and {num2} is {Expo}.") 



# In[7]:


#Task 2
#library
import numpy as np

#list with 10 elements 
list1 = [20,30,80,45,75,15,90,100,40,10]

# List functions 
#length function on list
print("The length of list1 :",len(list1))
# Maximum function on list 
print("The maximum value in list1 :",max(list1))
# Mininmum function on list
print("The minimum value in list1 :",min(list1))
# Append function on list 
list1.append(50)
print("The adding of new element in list1 :" ,list1)
# remove function on list 
list1.remove(15) 
print("The removing of a element in list1 :",list1)
#list in acsending order
list1.sort()
print("Ascending order of list1 :",list1)
#list in decending order 
list1.sort(reverse=True)
print("Descending order of list1 :",list1)

#Converting list into numpy array 
array1 = np.array(list1)
print("Created numpy array -",array1)
#numpy operation
#mean
mean_value = np.mean(array1)
print("The mean value of array1 :",mean_value)
#median
median_value = np.median(array1)
print("The median value of array1 :",median_value)
#standard deviation
std_value = np.std(array1)
print("The standard deviation of array1 :",std_value)


# In[4]:


# Task 3

#Dictionay
student = {"Name":"Komathy","Age":20,"Course":"Data Science And AI","Marks":90}
print(student)
# Printing using loops 
for key, value in student.items():
    print(key, ":", value)

#adding new key
student["grade"]="A"
print(student)

#sets
set1={"Machine Learning","Artificial Intelligence","Deep Learning","Web Development","Machine Learning"}
print("Unique courses set :",set1)

#set operations 
SetA={"R","C++","python","CSS","Sql"}
SetB={"Graphs","Games","CSS","Sql","Database"}

# union of SetA and SetB
union = SetA.union(SetB)
print("Union of Set A and Set B is - ",union)
# Intersection of SetA and SetB
intersection = SetA.intersection(SetB)
print("Intersection of Set A and Set B is - ",intersection)
# Difference of SetA and SetB
Diff = SetA.difference(SetB)
print("Difference of Set A and Set B is - ",Diff)


# In[10]:

# Task 4

# Creating a text file named student_data.txt
file1 = open("student_data.txt", "w")

# Student details 
file1.write("Name: Komathy, Course: Data Science, Marks: 90\n")
file1.write("Name: Ramesh, Course: Data Science, Marks: 70\n")
file1.write("Name: Suresh, Course: AI, Marks: 95\n")
file1.write("Name: Anjali, Course: Data Science, Marks: 90\n")
file1.write("Name: Aravind, Course: Data Science, Marks: 100\n")
file1.write("Name: Prem, Course: AI, Marks: 90\n")
file1.write("Name: Jenifer, Course: ML, Marks: 80\n")
file1.write("Name: Venila, Course: Data Science, Marks: 50\n")
file1.write("Name: Rahul, Course: ML, Marks: 90\n")

# Closing the file
file1.close()

# names with marks above 75
with open("student_data.txt", "r") as file:
    for line in file:
        parts = line.strip().split(",")  
        name = parts[0].split(":")[1].strip()   
        marks = int(parts[2].split(":")[1].strip())  
        
        if marks > 75:  
            print(name)


# In[ ]:




