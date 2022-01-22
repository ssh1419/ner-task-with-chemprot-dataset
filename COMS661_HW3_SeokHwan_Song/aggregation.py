#!/usr/bin/env python
# coding: utf-8

# In[59]:


# Import and read dataset
import pandas as pd
import numpy as np

# Data Preprocess
from collections import defaultdict

# Aggregation
import random


# In[60]:


# Dataset path

df_1 = pd.read_csv('1' + '.tsv', sep='\t', header=None, names=["PMID", "TYPE", "START", "END", "TEXT"])
df_2 = pd.read_csv('2' + '.tsv', sep='\t', header=None, names=["PMID", "TYPE", "START", "END", "TEXT"])
df_3 = pd.read_csv('3' + '.tsv', sep='\t', header=None, names=["PMID", "TYPE", "START", "END", "TEXT"])
df_4 = pd.read_csv('4' + '.tsv', sep='\t', header=None, names=["PMID", "TYPE", "START", "END", "TEXT"])
df_5 = pd.read_csv('5' + '.tsv', sep='\t', header=None, names=["PMID", "TYPE", "START", "END", "TEXT"])
df_6 = pd.read_csv('6' + '.tsv', sep='\t', header=None, names=["PMID", "TYPE", "START", "END", "TEXT"])
df_7 = pd.read_csv('7' + '.tsv', sep='\t', header=None, names=["PMID", "TYPE", "START", "END", "TEXT"])
    
    
abstract = pd.read_csv('chemprot_test_abstracts.tsv', sep='\t', header=None, names=["PMID", "TITLE", "ABSTRACT"])


# In[61]:


abstract_final = []
for i in range(len(abstract)):
    line = []
    pmid = abstract.iloc[i]["PMID"]
    docu = abstract.iloc[i]["TITLE"]+ " " + abstract.iloc[i]["ABSTRACT"] 
    line = [pmid, docu]
    abstract_final.append(line)


# In[62]:


# NA is treated as NaN, so covert NaN to 'NA'
df_1['TEXT'] = df_1['TEXT'].replace(np.nan, 'NA', regex=True)
df_2['TEXT'] = df_2['TEXT'].replace(np.nan, 'NA', regex=True)
df_3['TEXT'] = df_3['TEXT'].replace(np.nan, 'NA', regex=True)
df_4['TEXT'] = df_4['TEXT'].replace(np.nan, 'NA', regex=True)
df_5['TEXT'] = df_5['TEXT'].replace(np.nan, 'NA', regex=True)
df_6['TEXT'] = df_6['TEXT'].replace(np.nan, 'NA', regex=True)
df_7['TEXT'] = df_7['TEXT'].replace(np.nan, 'NA', regex=True)


# In[63]:


df_3['PMID']=df_3['PMID'].fillna(0).astype(np.int64)
df_3['START']=df_3['START'].fillna(0).astype(np.int64)
df_3['END']=df_3['END'].fillna(0).astype(np.int64)


# In[64]:


for i in range(len(df_1['PMID'])):
    if df_1['PMID'].loc[i]==0:
        df_1['PMID'].loc[i] = None
        
for i in range(len(df_2['PMID'])):
    if df_2['PMID'].loc[i]==0:
        df_2['PMID'].loc[i] = None

for i in range(len(df_3['PMID'])):
    if df_3['PMID'].loc[i]==0:
        df_3['PMID'].loc[i] = None
        
for i in range(len(df_4['PMID'])):
    if df_4['PMID'].loc[i]==0:
        df_4['PMID'].loc[i] = None
        
for i in range(len(df_5['PMID'])):
    if df_5['PMID'].loc[i]==0:
        df_5['PMID'].loc[i] = None
        
        
for i in range(len(df_6['PMID'])):
    if df_6['PMID'].loc[i]==0:
        df_6['PMID'].loc[i] = None        
        
for i in range(len(df_7['PMID'])):
    if df_7['PMID'].loc[i]==0:
        df_7['PMID'].loc[i] = None
        
        
        
        
df_1=df_1.dropna()
df_2=df_2.dropna()
df_3=df_3.dropna()
df_4=df_4.dropna()
df_5=df_5.dropna()
df_6=df_6.dropna()
df_7=df_7.dropna()
df_1=df_1.reset_index(drop=True)
df_2=df_2.reset_index(drop=True)
df_3=df_3.reset_index(drop=True)
df_4=df_4.reset_index(drop=True)
df_5=df_5.reset_index(drop=True)
df_6=df_6.reset_index(drop=True)
df_7=df_7.reset_index(drop=True)

df_5['PMID']=df_5['PMID'].fillna(0).astype(np.int64)
df_5['START']=df_5['START'].fillna(0).astype(np.int64)
df_5['END']=df_5['END'].fillna(0).astype(np.int64)
        


# In[39]:


df_list = [df_1, df_2, df_3, df_4, df_5, df_6, df_7]


# In[40]:


for i in range(len(df_list)):
    for j in range(len(df_list[i])):
        data = df_list[i]
        sent = data.loc[j]
        pmid  = sent['PMID']
        start = sent['START']
        end = sent['END']
        typee = sent['TYPE']
        text = sent['TEXT']

        for k in range(len(abstract_final)):
            
            pmid_real = abstract_final[k][0]
                
            if pmid == pmid_real:
                
                docu = abstract_final[k][1]
                
                if docu[start:end] != text:
                    
                    df_list[i]['PMID'].loc[j] = None
                    
                    break
                    
                    
    df_list[i]=df_list[i].dropna()
    df_list[i]=df_list[i].reset_index(drop=True)


# In[42]:


# Data Preprocess
def data_prepro(df_list):
    """
    Data Preprocess
    """
    result = defaultdict(lambda: defaultdict(list))

    for i in range(len(df_list)):
        for j in range(len(df_list[i])):
            
            data = df_list[i]
            sent = data.loc[j]
            pmid  = sent['PMID']
            off = str(sent['START']) + "," + str(sent['END'])
            typee = sent['TYPE']
            text = sent['TEXT']

            store = result[pmid][off]
            a = 0
            if not store:
                result[pmid][off] = [[typee, text, [i+1]]]
                
            else:
                for k in range(len(store)):
                    if store[k][0] == typee:
                        result[pmid][off][k][2].append(i+1)
                        a = 777
                        break
                        
                if a != 777:
                    result[pmid][off].extend([[typee, text, [i+1]]])

    return result


# In[43]:


# Use the data preprocessing
final = data_prepro(df_list)


# In[44]:


# Get the all PMIDs
key = pd.DataFrame([(k) for k, v in final.items()], columns = ['PMID']  )


# In[45]:


# Majority voting, and make a list
result = []
for i in range(len(key['PMID'])):
    
    pmid = key['PMID'].iloc[i]
    
    for k, v in final[pmid].items():
        
        off = str(k)
        
        if len(final[pmid][off])==1:
            typee = final[pmid][off][0][0]
            text = final[pmid][off][0][1]
            off_1 = off.split(",")
            start = off_1[0]
            end = off_1[1]
            line = [pmid, typee, start, end, text]
            
            result.append(line)
        
        
        elif len(final[pmid][off])==2:
            if len(final[pmid][off][0][2]) < len(final[pmid][off][1][2]):
                typee = final[pmid][off][1][0]
                text = final[pmid][off][1][1]
                off_1 = off.split(",")
                start = off_1[0]
                end = off_1[1]
                line = [pmid, typee, start, end, text]
                result.append(line)

            elif len(final[pmid][off][0][2]) > len(final[pmid][off][1][2]):
                typee = final[pmid][off][0][0]
                text = final[pmid][off][0][1]
                off_1 = off.split(",")
                start = off_1[0]
                end = off_1[1]
                line = [pmid, typee, start, end, text]
                result.append(line)

            elif len(final[pmid][off][0][2]) == len(final[pmid][off][1][2]):
                typee = random.choice(['CHEMICAL', 'GENE'])
                text = final[pmid][off][0][1]
                off_1 = off.split(",")
                start = off_1[0]
                end = off_1[1]
                line = [pmid, typee, start, end, text]
                result.append(line)


# In[46]:


# Convert to the dataframe
final_output = pd.DataFrame(result, columns=['PMID', 'Type', 'start', 'end', 'text'])


# In[53]:


# Get output.tsv file
import csv

final_output.to_csv('output.tsv', header=False, sep='\t', index=False, encoding='utf-8')

