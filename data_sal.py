# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:16:37 2019

@author: Ravi
"""
import pandas as pd
import numpy as np
import seaborn as sns
sal = pd.read_csv("C:\\Users\\ravi\\Desktop\\INDRAS ACADEMY\\R programming\\Salaries1\\Salaries.csv")
len(sal)
sal.columns
sal.Id.unique()
sal.EmployeeName.unique()
len(sal.JobTitle.unique())
sal.BasePay.unique()
sal.OvertimePay.unique()
sal.OtherPay.unique()
sal.Benefits.unique()
sal.TotalPay.unique()
sal.TotalPayBenefits.unique()
sal.Year.unique()
sal.Notes.unique()
sal.Agency.unique()
sal.Status.unique()

#sal
#sal['Benefits'].isnull().sum(axis=1)
#print['sal'].isnull()

###heat map of sal
sns.heatmap(sal.isnull(),yticklabels=False,cbar=False,cmap='viridis')
#checking number of null values
sal.isnull().sum()
#checking Not Provided & 0
len(sal[sal.Benefits==0])
len(sal[sal.Benefits=='Not Provided'])
#created data frame
df=pd.DataFrame(sal)
#dropping 11th column bcz its null
#sal1=df.drop(df.columns[10],axis=1)
#sal1.columns

# after deleting value checking heatmap
#sns.heatmap(sal1.isnull(),yticklabels=False,cbar=False,cmap='viridis')

#xxxxxxxxxxxx---------xxxxxxxxxxxxxx

#Benefits <----------
#finding mean values
mean_val=sal['Benefits'].mean()
#replacing non integer values by null values
sal['Benefits']=sal['Benefits'].replace('Not Provided',0).astype(float)
#finding mean again
mean_val = sal['Benefits'].mean()
#filling values back to that values
sal['Benefits']=sal['Benefits'].fillna(mean_val)
#checking again heatmap
sns.heatmap(sal.isnull(),yticklabels=False,cbar=False,cmap='viridis')

#-------------------------------------------------------------------

#for Basepay <----------
len(sal[sal.BasePay==0])
len(sal[sal.BasePay=='Not Provided'])
#xxxxxxxxxxxx---------xxxxxxxxxxxxxx
sal['BasePay']=sal['BasePay'].replace('Not Provided',0).astype(float)
mean_val = sal['BasePay'].mean()
sal['BasePay']=sal['Benefits'].fillna(mean_val)

#for Overtimepay <----------
len(sal[sal.OvertimePay==0])
len(sal[sal.OvertimePay=='Not Provided'])
#xxxxxxxxxxxx---------xxxxxxxxxxxxxx
sal['OvertimePay']=sal['OvertimePay'].replace('Not Provided',0).astype(float)
mean_val = sal['OvertimePay'].mean()
sal['OvertimePay']=sal['OvertimePay'].fillna(mean_val)


#for Otherpay <----------
len(sal[sal.OtherPay==0])
len(sal[sal.OtherPay=='Not Provided'])
#xxxxxxxxxxxx---------xxxxxxxxxxxxxx
sal['OtherPay']=sal['OtherPay'].replace('Not Provided',0).astype(float)
mean_val = sal['OtherPay'].mean()
sal['OtherPay']=sal['OtherPay'].fillna(mean_val)

###Visual Representation

#distplot
sns.distplot(sal['BasePay'],bins=20)
sns.distplot(sal['OvertimePay'],bins=20)
sns.distplot(sal['OtherPay'])
sns.distplot(sal['Benefits'])
sns.distplot(sal['TotalPay'])
sns.distplot(sal['TotalPayBenefits'])
sns.distplot(sal['Year'])


#Joint Plot year vs total pay
sns.jointplot(x='Year',y='TotalPay',data=sal,kind='hex')
sns.jointplot(x='Year',y='TotalPay',data=sal,kind='reg')
sns.jointplot(x='Year',y='TotalPay',data=sal,kind='kde')
sns.jointplot(x='Year',y='TotalPay',data=sal)


#Joint plot year vs overtime pay
sns.jointplot(x='Year',y='OvertimePay',data=sal,kind='hex')
sns.jointplot(x='Year',y='OvertimePay',data=sal,kind='reg')
sns.jointplot(x='Year',y='OvertimePay',data=sal,kind='kde')
sns.jointplot(x='Year',y='OvertimePay',data=sal)

#Joint Plot year vs TotalPayBenefits 
sns.jointplot(x='Year',y='TotalPayBenefits',data=sal,kind='hex')
sns.jointplot(x='Year',y='TotalPayBenefits',data=sal,kind='reg')
sns.jointplot(x='Year',y='TotalPayBenefits',data=sal,kind='kde')
sns.jointplot(x='Year',y='TotalPayBenefits',data=sal)

#Bar Plot Jobtitle vs total Pay
sns.barplot(x='JobTitle',y='TotalPay',data=sal)
#Bar Plot jobtital vs overtimepay
sns.barplot(x='JobTitle',y='OvertimePay',data=sal)
#Count Plot
sns.countplot(x='JobTitle',data=sal)
sns.countplot(x='Status',data=sal)

#box plot
sns.boxplot(x='JobTitle',y='TotalPay',data=sal,hue='Status')















