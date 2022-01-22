#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import and read dataset
import pandas as pd
import numpy as np


# In[2]:


# Dataset path

output = pd.read_csv('output.tsv', sep='\t', header=None, names=["PMID", "TYPE", "START", "END", "TEXT"])

test = pd.read_csv('chemprot_test_entities.tsv', sep='\t', header=None, names=["PMID", "TYPE", "START", "END", "TEXT"])


# In[3]:


output=output.to_numpy().tolist()
test=test.to_numpy().tolist()


# In[4]:


# Evaluater
def evaluate(test, train):
    
    result_1 = []
    result_2 = []
    line_1 = []
  
    for i in range(len(train)):
        line_1 = train[i][1]
        result_1.insert(i, line_1)
        
        line_2 = []
        for j in range(len(test)):
            if train[i][0] == test[j][0]:
                if train[i][2] == test[j][2]:
                    if train[i][3] == test[j][3]:  
                        
                        line_2 = test[j][1]
                        result_2.insert(i, line_2)
                        
                        break
                
    return result_1, result_2


# In[118]:


# It takes little long (about 10 mins)
final = evaluate(test, output)


# In[874]:


pred = final[0] 
test = final[1]
num = len(pred)-len(test)
l = [None] * num
test = np.append(test, l)


# In[875]:


pred_df = pd.DataFrame(pred)
test_df = pd.DataFrame(test)


# In[876]:


pred_df = pred_df[0].replace(np.nan, '', regex=True)
test_df = test_df[0].replace(np.nan, '', regex=True)


# In[877]:


# Data Preprocess
pred_final = (np.array([pred_df])).tolist()
test_final = (np.array([test_df])).tolist()


# In[812]:


## pip install seqeval
## I used this library so it may be asked you to download this library to run it.


# In[878]:


import sklearn.metrics as s
pre, rec, f1, _ = s.precision_recall_fscore_support(test_final[0], pred_final[0],labels=['GENE', 'CHEMICAL'], average='micro')

print("precision: %f \n recall: %f \n F1: %f" % (pre,rec,f1))

