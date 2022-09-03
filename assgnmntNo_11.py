#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Answer no 1
#Write a Python program to find words which are greater than given length k
sntnc = "Hello sir inueron is best platform"
length = 4
print([word for word in sntnc.split() if len(word) > length])


# In[2]:


#Answer no 2
#Write a Python program for removing i-th character from a string
test_str = "IneuronForCoding"
print("The original string is:"+test_str)

new_str = ""
for i in range(len(test_str)):
    if i != 2:
        new_str = new_str +test_str[i]
        
print("The string after removal of i'th character :" + new_str)


# In[4]:


#Answer no 3
#Write a Python program to split and join a string
def split_string(string):
    list_string = string.split(' ')
    return list_string

def join_string(list_string):
    string = '-'.join(list_string)
    return string

if __name__ == '__main__':
    string = 'Ineuron For Coding'
    
    list_string = split_string(string)
    print(list_string)
    
    new_string = join_string(string)
    print(new_string)


# In[6]:


#Answer no 4
#Write a Python to check if a given string is binary string or not
def check(string):
    p = set(string)
    s = {'0','1'}
    
    if s == p or p == {'0'} or p == {'1'}:
        print("Yes")
    else:
        rint("No")
        
if __name__ == '__main__':
    string = "101010000111"
    
    check(string)


# In[8]:


#Answer no 5
#Write a Python program to find uncommon words from two Strings
def uncommon_word(A,B):
    
    count = {}
    
    for word in A.split():
            
            count[word] = count.get(word,0)+1
    
    for  word in B.split():
        count[word] = count.get(word,0)+1
        
    return [word for word in count if count[word]==1]
A = "Ineuron For Coding"
B = "Ineuron is best For Coding"

print(uncommon_word(A,B))
        


# In[10]:


#Answer no 6
#Write a Python to find all duplicate characters in string
string = "We are dreamers , we never giveup"
duplicates = []
for char in string:
    if string.count(char)> 1:
        if char not in duplicates:
            duplicates.append(char)
print(*duplicates)


# In[11]:


#Answer no 7
#Write a Python Program to check if a string contains any special character
import re
def run(string):
    regex = re.compile('[!@#$%^&*(){}]')
    if(regex.search(string)== None):
        print("string is accepted")
        
    else:
        print("string is not accepted")
        
if __name__ == '__main__':
    string = "WE@code@#"
    
    run(string)


# In[ ]:




