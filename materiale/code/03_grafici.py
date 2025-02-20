# pip install matplotlib
# pip install seaborn

# %%
import pandas as pd
import matplotlib.pyplot as plt

# Creiamo un dataset di esempio
data = {
    "Categoria": ["Elettronica", "Elettronica", "Abbigliamento", "Abbigliamento", "Elettronica", "Sport"],
    "Città": ["Milano", "Roma", "Milano", "Roma", "Napoli", "Milano"],
    "Vendite": [200, 150, 400, 300, 250, 100]
}

df = pd.DataFrame(data)
df_grouped = df.groupby("Categoria")["Vendite"].sum()
# %%
# df_grouped.plot(kind="bar", color="skyblue", edgecolor="black")
# plt.title("Vendite per categoria")
# plt.xlabel("Categoria")
# plt.ylabel("Vendite")
# plt.xticks(rotation=45)
# plt.grid()
# plt.show()
#plt.savefig("grafico_vendite.png", dpi=300)

# %%
import seaborn as sns

sns.set_theme(style="whitegrid")
plt.figure(figsize=(6, 4))
sns.boxplot(x="Categoria", y="Vendite", data=df, ci=None, palette="viridis")
plt.title("Vendite per categoria")
plt.show()

# %%
