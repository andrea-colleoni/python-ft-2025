# pacchetto da installare => pip install openpyxl

# %%
import pandas as pd

percorso = "Global_Superstore2.xlsx"
try:
    df = pd.read_excel(percorso, sheet_name="Sheet1")

    df.head()
    df.info()

    # %%
    print(df.isnull().sum())
    # %%
    df_clean = df.dropna(subset=["Order Date", "Sales", "Profit", "Category"])

    # %%
    df_clean["Order Date"] = pd.to_datetime(df_clean["Order Date"], dayfirst=True)
    df_clean["Ship Date"] = pd.to_datetime(df_clean["Ship Date"], dayfirst=True)

    # %%
    df_clean["Order Year"] = df_clean["Order Date"].dt.year

    # %%
    df_pivot = df_clean.pivot_table(index="Order Year", columns="Category", values="Sales", aggfunc="sum")
    # %%
    percorso_out = "pivot_vendite.xlsx"
    with pd.ExcelWriter(percorso_out, engine="openpyxl") as writer:
        df_clean.to_excel(writer, "Dati")
        df_pivot.to_excel(writer, sheet_name="Pivot vendite")
except FileNotFoundError as fe:
    print(f'il file {percorso} non esiste')
except Exception as err:
    print(err)

