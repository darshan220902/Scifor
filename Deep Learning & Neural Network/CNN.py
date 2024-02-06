#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np


# In[2]:


(X_train, y_train) , (X_test, y_test) = keras.datasets.mnist.load_data()


# In[3]:


X_train.shape


# In[4]:


X_test.shape


# In[5]:


X_train=X_train/255
X_test=X_test/255


# In[6]:


X_train.shape


# In[7]:


y_train.shape


# In[8]:


X_train = X_train.reshape(-1,28,28,1)
X_train.shape


# In[9]:


X_test = X_test.reshape(-1,28,28,1)
X_test.shape


# In[10]:


model = keras.Sequential([
    
    layers.Conv2D(30, (3,3), activation='relu', input_shape=(28, 28,1)),
    layers.MaxPooling2D((2,2)),
 
    layers.Flatten(),
    layers.Dense(100, activation='relu'),
    keras.layers.Dense(10, activation='sigmoid')
])


# In[11]:


model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=5)


# In[12]:


y_train[:5]


# In[13]:


model.evaluate(X_test,y_test)


# In[14]:


y_pred=model.predict(X_test)
y_pred[1]


# In[15]:


plt.matshow(X_test[1])


# In[16]:


np.argmax(y_pred[1]) 


# In[ ]:


# matshow and y_pred are same so model works good

