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
# keep_default_na => attenzione quando i valori sono letteralmente 'NA'!!
# na_values='' => permette di specificare quali siano i valori da interpretare come NA
# dtype={'Age': str} => serve per forzare il tipo di una colonna
# .astype(int) => permette di convertire il tipo di un valore in fase di creazione di una nuova colonna

# Attezione all'encoding del file dati (caratteri non latini potrebbero dare errori in lettura/caricamento)
auto = pd.read_csv('car_price_dataset.csv', )
# print(auto.head()) => stampa le prime n righe
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
