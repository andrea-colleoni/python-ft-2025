#%%
import pandas as pd

df = pd.read_csv('train.csv')

#%%
nulli = df.isnull()


#%%
# Elimino non embarked
df.dropna(subset='Embarked', inplace=True)

#%%
eta_media = df['Age'].mean()
#%%
df['Age'].fillna(eta_media, inplace=True)
#%%
df.to_csv('titanic_mod.csv')
