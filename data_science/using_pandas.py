import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")
'''
XYZ_web={'day':[1,2,3,4,5,6],'visitors':[1000,700,6000,1000,400,350],'bounce_rate':[20,20,23,15,10,34]}
df=pd.DataFrame(XYZ_web)
print(df)
print(df.head())
print(df.head(2)) #prints only first two rows 
print(df.tail(3)) #prints only last 3 rows

df1=pd.DataFrame({"HPI":[80,90,70,60],"Int_rate":[2,1,2,3],"IND_GDP":[50,45,45,67]},index=[2001,2002,2003,2004])
print(df1)
df2=pd.DataFrame({"HPI":[80,90,70,60],"Int_rate":[2,1,2,3],"IND_GDP":[50,45,45,67]},index=[2005,2006,2007,2008])

#merging
mer=pd.merge(df1,df2)
print(mer)
merg=pd.merge(df1,df2, on="HPI") #merges only on HPI
print(merg)
 
d1=pd.DataFrame({"int_rate":[2,1,2,3],"ind_gdp":[50,45,45,67]},index=[2001,2002,2003,2004])
d2=pd.DataFrame({"low_tier_HPI":[50,45,67,34],"unemployment":[1,3,5,6]},index=[2001,2003,2004,2004])

#joining
print(d1.join(d2))

dfm=pd.DataFrame({"day":[1,2,3,4],"visitors":[200,100,450,500],"bounce_rate":[20,45,60,10]})
print(dfm)
dfm.set_index("day",inplace=True) #replaces index
print(dfm) 
#dfm.plot()
#plt.show()
dfm=dfm.rename(columns={"visitors":"users"}) #renames column
print(dfm)
sd=dfm.reindex(columns=['day','visitors']) #will print only these 2 columns
print(sd)
#concatenation
print(pd.concat([df1,df2]))

#data munging i.e  conversion of files, one into another is also done through pandas

#statistics
from statistics import mean,median,mode,variance 
print(mean([3,4,5,3,4,5,2,7,7,9]))
print(median([3,5,6,7,2,9,6]))
print(mode([1,1,1,1,3,4,4,4,6,7,8,9]))
print(round(variance([1,1,3,4,5,6,7,8,9,3]),2))
'''
dat=pd.DataFrame({'Country':['Russia','India','USA','Israel','China','UK'],'Rankings':[10,13,7,15,18,16],'GDP':[100,90,110,75,130,120]})
print(dat,'\n')
print(dat.describe(),'\n')  # Summary statistics 
print(dat.info())
print(dat.sort_values(by=['Rankings','GDP'],ascending=[True,False],inplace=False))
k=pd.DataFrame({'k1':['one']*4+['two']*4,'k2':[1,2,3,2,4,5,4,5]})
print(k)
print(k.drop_duplicates())
print(dat.sort_values(by='GDP',ascending=[True],inplace=False))

foodata = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami','corned beef', 'Bacon', 'pastrami', 'honey ham','nova lox'],'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print(foodata)

meat_to_animal = {
'bacon': 'pig',
'pulled pork': 'pig',
'pastrami': 'cow',
'corned beef': 'cow',
'honey ham': 'pig',
'nova lox': 'salmon'
}
#create a new variable i.e column
foodata['animal'] = foodata['food'].map(str.lower).map(meat_to_animal)
print(foodata)
foodata['price']=[100,300,500,200,400,250,700,900,600]
print(foodata)
print(foodata[3:6])  # prints rows with index 3 to 6
print(foodata.loc[:,['food','ounces']])  # prints all rows of the 2 columns mentioned
print(foodata.iloc[3])  # prints 4th row , index is 3
print(foodata.iloc[3:5,0:3])  # prints rows 3,4 of columns 0,1 and 2
print(foodata.iloc[[1,3,5],[0,2]]) # prints 1,3,5 rows of columns 0 and 2
print(foodata.iloc[:,:-1].values)  # prints all rows of all colums except the last in an array format

k=pd.Series([1,999,45,33,-3,0,-.09])
print('\n',k)
k.replace(999,np.nan,inplace=True)
print(k)
k.replace([45,-3],16,inplace=True)
print(k)

print('\n',list(foodata.iloc[:,0]))
