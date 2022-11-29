#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


np.array([1,2,3,4])


# In[5]:


a = np.array([1,2,3,4])


# In[6]:


type(a)


# In[7]:


np.array([1,2,3.4,5])


# In[8]:


np.zeros(10, dtype = int)


# In[11]:


np.ones((3,3), dtype = int)


# In[12]:


np.ones((5,5), dtype = int)


# In[13]:


np.full((3,5), 3)


# In[14]:


np.random.normal(10, 4, (3,4))


# In[15]:


# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi


# In[16]:


np.random.randint(10, size = 10)


# In[22]:


a = np.random.randint(10, size = 10)


# In[20]:


np.sort(a)


# In[23]:


a.ndim


# In[24]:


a.shape


# In[25]:


a.size


# In[26]:


a.dtype


# In[36]:


b = np.random.randint(10, size = (3,5))


# In[37]:


print(b)


# In[38]:


b.ndim


# In[39]:


b.size


# In[40]:


b.shape


# In[41]:


b.dtype


# In[ ]:


#Reshape
#Verileri matriste yeniden şekillendirmeye yarıyor.


# In[42]:


np.arange(1,10)


# In[43]:


np.arange(1,10).reshape(3,3)


# In[44]:


a = np.arange(1,10)


# In[45]:


a


# In[46]:


b = a.reshape(1,9)


# In[47]:


b.ndim


# In[48]:


#Concatenation(Array Birleştirme)


# In[49]:


x = np.array([1,2,3])
y = np.array([4,5,6])


# In[50]:


np.concatenate([x,y])


# In[51]:


#iki boyut


# In[52]:


a = np.array([[1,2,3],
            [4,5,6]])


# In[53]:


np.concatenate([a,a])


# In[54]:


#splitting


# In[55]:


x = np.array([1,2,3,99,99,3,2,1])


# In[56]:


np.split(x, [3,5])


# In[57]:


a,b,c = np.split(x, [3,5])


# In[58]:


a


# In[59]:


b


# In[60]:


c


# In[65]:


m = np.arange(20).reshape(4,5)
m


# In[66]:


np.vsplit(m,[2])


# In[67]:


np.hsplit(m,[2])


# In[ ]:




