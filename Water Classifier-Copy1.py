#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import cross_val_score

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as nn
import pickle 


# In[ ]:





# In[2]:


df=pd.read_csv('C:\\Users\\argha\\Project MCA\\Water_pond_tanks_2021.csv',encoding='cp1252')


# In[3]:


df


# In[4]:


df.dropna()


# In[5]:


col=list(df.columns)
col


# In[6]:


col2=["code","name","type","state","tempMin","tempMax","do2Min","do2Max","phMin","phMax","conMin","conMax","bodMin","bodMax","nMin","nMax","fcMin","fcMax","tcMin","tcMax"]


# In[7]:


r,c=df.shape
for i in range(c):
    df.rename(columns={col[i]: col2[i]}, inplace=True)


# In[8]:


df=df.dropna()
df


# In[9]:


for i in range(4,c):
  df[col2[i]]= pd.to_numeric(df[col2[i]], errors='coerce')


# In[10]:


y=[]
tempMin=list(df['tempMin'])
tempMax=list(df['tempMax'])
do2Min=list(df['do2Min'])
do2Max=list(df['do2Max'])
phMin=list(df['phMin'])
phMax=list(df['phMax'])
conMin=list(df['conMin'])
conMax=list(df['conMax'])
bodMin=list(df['bodMin'])
bodMax=list(df['bodMax'])
nMin=list(df['nMin'])
nMax=list(df['nMax'])
fcMin=list(df['fcMin'])
fcMax=list(df['fcMax'])
tcMin=list(df['tcMin'])
tcMax=list(df['tcMax'])


# In[11]:


r,c=df.shape


# In[12]:


for i in range(r):
    if tcMax[i]<=50 and phMin[i]>=6.5 and phMax[i]<=8.5 and do2Max[i]>=6 and bodMin[i]<=2:
        y.append("A")
    elif tcMax[i]<=500 and phMin[i]>=6.5 and phMax[i]<=8.5 and do2Max[i]>=5 and bodMin[i]<=3:
        y.append("B")
    elif tcMax[i]<=5000 and phMin[i]>=6 and phMax[i]<=9 and do2Max[i]>=4 and bodMin[i]<=3:
        y.append("C")
    elif phMin[i]>=6.5 and phMax[i]<=8.5 and do2Max[i]>=4 and nMin[i]<=1.2:
        y.append("D")
    elif phMin[i]>=6 and phMax[i]<=8.5 and conMax[i]<=2250:
        y.append("E")
    else:
        y.append("X")


# In[13]:


len(y)


# In[14]:


df["Class"]=y


# In[15]:


df


# In[16]:


df=df.dropna()
df2 = df.loc[df['Class'] != 'X']
df3 = df.loc[df['Class'] == 'X']


# In[17]:


df2=df2.dropna()


# In[18]:


X=df2[df2.columns[6:20]]
Y=df2['Class']


# In[19]:



X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.4, random_state=42)


# In[20]:


clf=DecisionTreeClassifier(random_state=0)
y=clf.fit(X_train,y_train)


# In[21]:


y_pred=y.predict(X_test)
print(y_pred)


# In[22]:


print(metrics.accuracy_score(y_test, y_pred))


# In[23]:


from sklearn import tree
print(confusion_matrix(y_test, y_pred))
tree.plot_tree(clf)


# In[24]:


from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))


# In[27]:


df3=df3.dropna()
X2=df3[df3.columns[6:20]]


# In[28]:


y_pred2=y.predict(X2)
print(y_pred2)



# In[ ]:




pickle.dump(clf, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))