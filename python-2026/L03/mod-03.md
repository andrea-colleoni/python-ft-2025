# Interrogazioni SQL da Python (versione aula reale)

## Obiettivo

Non “usare Python con SQL”, ma:

> usare Python per **automatizzare flussi dati sopra SQL Server**

---

# 1. Setup rapido (10–15 min)

```python
import pyodbc

conn_str = (
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=localhost\\SQLEXPRSS;"
    "Database=Northwind;"
    "UID=python;"
    "PWD=python;"
    "TrustServerCertificate=Yes;"
)

conn = pyodbc.connect(conn_str)
```

### Primo test serio (non banale)

```python
cursor = conn.cursor()

cursor.execute("SELECT TOP 5 * FROM Customers")

for row in cursor.fetchall():
    print(row)
```

Vediamo subito una cosa importante:

* il risultato è **tuple-based**
* quindi **poco usabile per analisi**

Transizione naturale → pandas

---

# 2. Dal DB al DataFrame (30 min)

## Il salto di qualità

```python
import pandas as pd

query = "SELECT TOP 100 * FROM Orders"

df = pd.read_sql(query, conn)

print(df.head())
```

### Qui abbiamo:

* `pyodbc` = basso livello
* `pandas.read_sql` = livello produttivo

---

## Esercizio 1 (facile ma utile)

> Estrarre gli ordini con:

* OrderDate
* CustomerID
* Freight

```sql
SELECT OrderID, CustomerID, OrderDate, Freight
FROM Orders
```

### Task:

* caricarli in pandas
* convertire `OrderDate` in datetime
* calcolare:

  * media Freight
  * numero ordini per cliente

---

# 3. Query parametrizzate (fondamentale, 20 min)

Qui devi martellare: **SQL injection esiste anche in Python**

## Esempio SBAGLIATO

```python
customer = "ALFKI"

query = f"SELECT * FROM Customers WHERE CustomerID = '{customer}'"
```

## Esempio CORRETTO

```python
query = "SELECT * FROM Customers WHERE CustomerID = ?"

df = pd.read_sql(query, conn, params=[customer])
```

### Esercizio 2

> Estrarre ordini di un cliente passato da input

Bonus:

* prova input malevolo (`' OR 1=1 --`)

---

# 4. SQL vs Pandas: chi deve fare cosa (20–25 min)

## Regola pratica

* SQL → filtri, join, aggregazioni grosse
* pandas → pulizia, feature engineering, visualizzazione

---

## Caso studio concreto

### Versione 1 (tutto in pandas — sbagliata)

```python
df_orders = pd.read_sql("SELECT * FROM Orders", conn)
df_customers = pd.read_sql("SELECT * FROM Customers", conn)

df = df_orders.merge(df_customers, on="CustomerID")
```

### Versione 2 (giusta)

```sql
SELECT o.OrderID, o.OrderDate, c.Country
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
```

```python
df = pd.read_sql(query, conn)
```

---

## Esercizio 3 (molto importante)

> Numero ordini per paese

### Step richiesti:

1. farlo in SQL
2. farlo in pandas
3. confrontare

---

# 5. Pipeline reale DB → pandas → CSV (30 min)

## Esempio completo

```python
query = """
SELECT 
    o.OrderID,
    o.OrderDate,
    c.Country,
    o.Freight
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
"""

df = pd.read_sql(query, conn)

# pulizia veloce
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# feature
df['Year'] = df['OrderDate'].dt.year

# aggregazione
report = df.groupby(['Country', 'Year'])['Freight'].mean().reset_index()

# export
report.to_csv("report_freight.csv", index=False)
```

---

## Esercizio 4 (molto concreto)

> Generare un report CSV con:

* fatturato medio per paese
* per anno

---

# 6. Pipeline inversa: CSV → SQL (25–30 min)

## Step

```python
df = pd.read_csv("report_freight.csv")

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO FreightReport (Country, Year, AvgFreight)
        VALUES (?, ?, ?)
    """, row['Country'], int(row['Year']), float(row['Freight']))

conn.commit()
```

---

## Variante più smart

```python
from sqlalchemy import create_engine

engine = create_engine(
    "mssql+pyodbc://python:python@localhost\\SQLEXPRSS/Northwind?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
)

df.to_sql("FreightReport", engine, if_exists="replace", index=False)
```

---

## Esercizio 5

> Caricare un CSV dentro SQL Server

---

# 7. Confronto con SAS (10–15 min)

## PROC SQL vs Python

SAS:

* tutto dentro SAS
* pipeline rigide

Python:

* SQL + pandas + file + API
* molto più flessibile

Importante:

> Python non è meglio di SQL.
> È meglio **per costruire sistemi attorno a SQL**.

---

# 8. Chiusura (messaggio chiave)

Se vuoi lasciare qualcosa che resti:

> Chi usa Python per fare SELECT * sta sprecando Python.
> Chi usa Python per orchestrare dati sta facendo ingegneria.

---

## Mini progetto (30 min opzionale)

> “Costruisci uno script che:

1. prende un cliente in input
2. estrae i suoi ordini
3. calcola metriche
4. salva un report CSV”

---

# 📚 Fonti e link

* SQLite docs
  [https://docs.python.org/3/library/sqlite3.html](https://docs.python.org/3/library/sqlite3.html)

* Pandas SQL
  [https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html)

* SQLAlchemy
  [https://docs.sqlalchemy.org/](https://docs.sqlalchemy.org/)

* SQL Injection (OWASP)
  [https://owasp.org/www-community/attacks/SQL_Injection](https://owasp.org/www-community/attacks/SQL_Injection)

* Pandas vs SQL guide
  [https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html)

---

# 💡 Chiusura didattica

Messaggio chiave da far passare:

> SQL estrae i dati
> Python li trasforma
> Pandas li analizza


# 🔶 MODULO SQL → AdventureWorks

Qui puoi fare davvero il salto di qualità.

## Database: AdventureWorks

---

# Tabelle chiave da usare

* `Sales.SalesOrderHeader`
* `Sales.SalesOrderDetail`
* `Production.Product`
* `Person.Person`
* `Sales.Customer`

---

# 🔥 Esempio 1 — Query realistica

## SQL

```sql
SELECT 
    p.Name AS ProductName,
    SUM(d.LineTotal) AS Revenue
FROM Sales.SalesOrderDetail d
JOIN Production.Product p ON d.ProductID = p.ProductID
GROUP BY p.Name
ORDER BY Revenue DESC
```

---

## Python

```python
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mssql+pyodbc://user:password@localhost/AdventureWorks?driver=ODBC+Driver+17+for+SQL+Server"
)

query = """
SELECT 
    p.Name AS ProductName,
    SUM(d.LineTotal) AS Revenue
FROM Sales.SalesOrderDetail d
JOIN Production.Product p ON d.ProductID = p.ProductID
GROUP BY p.Name
"""

df = pd.read_sql(query, engine)
```

---

# 🔥 Esempio 2 — Pipeline completa

```python
df["Revenue"] = df["Revenue"].astype(float)

top10 = df.nlargest(10, "Revenue")

print(top10)
```

---

# 🔥 Esempio 3 — SQL vs Pandas (didattico forte)

## SQL

```sql
SELECT 
    YEAR(OrderDate) AS Year,
    SUM(TotalDue) AS Revenue
FROM Sales.SalesOrderHeader
GROUP BY YEAR(OrderDate)
```

## Pandas

```python
df = pd.read_sql("SELECT OrderDate, TotalDue FROM Sales.SalesOrderHeader", engine)

df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["Year"] = df["OrderDate"].dt.year

df.groupby("Year")["TotalDue"].sum()
```

---

# 💣 Punto didattico importante (spingilo forte)

Notare questo errore:

```python
# ERRORE CLASSICO
df = pd.read_sql("SELECT * FROM Sales.SalesOrderDetail", engine)
```

Chiediti:

> davvero voglio portarmi 1 milione di righe in RAM?

---

# ✔ Versione corretta

```python
df = pd.read_sql("""
SELECT ProductID, LineTotal
FROM Sales.SalesOrderDetail
WHERE LineTotal > 1000
""", engine)
```

---

# 🔥 Esercizi reali (non accademici)

## Esercizio 1

* Top 10 prodotti per fatturato
* Grafico

## Esercizio 2

* Fatturato per anno
* Crescita %

## Esercizio 3

* Cliente top spender
* join tra 3 tabelle

---

# 🔁 Ponte Kaggle ↔ SQL

Fagli vedere questo scenario:

1. Kaggle dataset (CSV)
2. caricato in SQL Server
3. interrogato via Python

```python
df = pd.read_csv("dataset.csv")
df.to_sql("kaggle_data", engine, if_exists="replace", index=False)
```

