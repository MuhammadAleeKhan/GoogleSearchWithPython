#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#pip install google


# In[5]:


from googlesearch import search
query = "Python Tutorial"
for i in search(query, tld = 'com.pk', lang = 'en', num = 10, start = 0, stop = 10, pause = 2):
    print(i)

