#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[35]:


l=[9,3,3, 9, 3, 9, 7, 9]
ans=0
list=[]
for i in l:
    c=l.count(i)
    res=[int(x) for x in str(c)]
    q=len(res)
   
    for j in range(0,q):
        if res[j]%2!=0 not in list:
            list.append(ans)
            ans=i
            
            print(ans)
            


# In[ ]:




