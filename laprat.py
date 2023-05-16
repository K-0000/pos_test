import pandas as pd
import glob
import os

#Sale
df = pd.read_csv('14SR.csv')
group = df.groupby(['Date','Salesperson Name','Customer Name','Product Name','Saletype','Price']).agg({'Qty':'sum'})
group.to_csv('Byprice.csv')
df = pd.read_csv('Byprice.csv')
df['SoldTotal'] = df['Price'] * df['Qty']
print(df.head())
df2 = df.append(pd.DataFrame(df.SoldTotal.sum(), index = ["Total"], columns=[ "SoldTotal"]))
df2.to_csv('Byprice.csv')
group = df.groupby(['Product Name']).agg({'Qty':'sum'})
group.to_csv('Byproduct.csv')

#Cash
df = pd.read_csv('cash.csv')
otr = df[df["Type"]== "Out"]
itr = df[df["Type"]== "In"]
otr = otr.append(pd.DataFrame(otr.Ammount.sum(), index = ["Total"], columns=[ "Ammount"]))
otr.to_csv('OutCashreport.csv')
itr = itr.append(pd.DataFrame(itr.Ammount.sum(), index = ["Total"], columns=[ "Ammount"]))
itr.to_csv('InCashreport.csv')
ctr = df[df["Type"]== "Credit"]
ctr = ctr.append(pd.DataFrame(ctr.Ammount.sum(), index = ["Total"], columns=[ "Ammount"]))
ctr.to_csv('Creditreport.csv')

#Stockin
df = pd.read_csv('ST.csv')
stockin = df[df["Type"]== "Stock In"]
mix = df[df["Type"]== "Mixed"]
mix= mix.groupby(['Date','Product','Type']).agg({'Quantity':'sum'})
divide = df[df["Type"]== "Divide"]
divide= divide.groupby(['Date','Product','Type']).agg({'Quantity':'sum'})
damage = df[df["Type"]== "Damaged"]
damage= damage.groupby(['Date','Product','Type']).agg({'Quantity':'sum'})
print(stockin)
stockin.to_csv('stockin.csv')
print(divide)
divide.to_csv('divide.csv')
print(mix)
mix.to_csv('mix.csv')
print(damage)
mix.to_csv('damage.csv')
