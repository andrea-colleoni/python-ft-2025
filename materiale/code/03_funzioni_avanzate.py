# %%
import pandas as pd

# Creiamo un dataset di esempio
data = {
    "Categoria": ["Elettronica", "Elettronica", "Abbigliamento", "Abbigliamento", "Elettronica", "Sport"],
    "Città": ["Milano", "Roma", "Milano", "Roma", "Napoli", "Milano"],
    "Vendite": [200, 150, 400, 300, 250, 100]
}

df = pd.DataFrame(data)
df.head()


# %% groupby()
df_grouped = df.groupby("Categoria")["Vendite"].sum()

df_grouped_multi = df.groupby(["Categoria", "Città"])["Vendite"].sum()

print(df_grouped_multi)

# %% merge()
df_prodotti = pd.DataFrame({
    "ID_Prodotto": [1, 2, 3, 4],
    "Nome": ["Laptop", "Mouse", "Tastiera", "Monitor"]
})

df_prezzi = pd.DataFrame({
    "ID_Prodotto": [1, 2, 3, 5],
    "Prezzo": [1000, 50, 70, 150]
})

df_join = pd.merge(df_prodotti, df_prezzi,  how="left")
print(df_join)

# %% pivot()
df_pivot = df.pivot_table(values="Vendite", columns="Città", index="Categoria", aggfunc="sum", fill_value=0)


