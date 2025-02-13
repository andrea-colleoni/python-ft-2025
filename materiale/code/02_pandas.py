#%% importazione
import pandas as pd

help(pd.DataFrame)
# %%

#%%
serie = pd.Series([1, 2, 3, 4], ['a', 'b', 'c', 'd'])
print(serie)


#%%
persone = pd.DataFrame({'Nome': ['Andrea', 'Maria', 'Paola'], 'Età': [45, 23, 28]})
#print(persone)
print(persone['Nome'])


# %%
persone['Cognome'] = ['Rossi', 'Verdi', 'Bianchi']

#%%
persone['Eta_Raddoppiata'] = persone['Età'] * 2
print(persone)

#%%
print(persone[persone['Età'] > 30])

#%%
auto = pd.read_csv('car_price_dataset.csv')
#print(auto.head())
auto['ConIVA'] = auto['Price'] * 1.22

#%%
iris = pd.read_json('iris.json')

#%% database SQL
from sqlalchemy import create_engine
# pip install sqlalchemy mssql
# url di connessione
conn = create_engine('mssql+pymssql://sa:passw0rd@localhost/AdventureWorks2019')
employees = pd.read_sql('SELECt * FROM [HumanResources].[Employee]', con=conn)


#%%
auto.info()
auto.describe()

#%% funzioni arbitrarie
astersik = lambda x: x + '*'

auto['BrandNew'] = auto['Brand'].apply(astersik)
#%%
auto['Model'] = auto['Model'].apply(astersik)

# %%
