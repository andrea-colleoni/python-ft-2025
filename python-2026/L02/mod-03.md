# Interrogazioni SQL da Python (2–3h)

## Obiettivo

Integrare Python con database aziendali:

* Python **non sostituisce SQL**
* Python **orchestra SQL + analisi + output**

---

## Contesto

In un contesto reale:

```
Database (SQL)
      ↓
Python (query + logica)
      ↓
Pandas (analisi)
      ↓
Output (grafico, Excel, report)
```

Python è il **collante**, non il sostituto del database.

---

## Stack

* `sqlite3` → DB embedded per demo
* `SQLAlchemy` → layer di astrazione
* `pandas.read_sql` → ponte SQL → DataFrame

---

# 1️⃣ Setup iniziale

```bash
pip install pandas sqlalchemy
```

SQLite è già incluso in Python.

---

# 2️⃣ Connessione a un database (sqlite3)

```python
import sqlite3

conn = sqlite3.connect("azienda.db")
cursor = conn.cursor()
```

Creiamo una tabella di esempio:

```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS vendite (
    id INTEGER PRIMARY KEY,
    prodotto TEXT,
    quantita INTEGER,
    prezzo REAL,
    data TEXT
)
""")

conn.commit()
```

Inserimento dati:

```python
cursor.executemany("""
INSERT INTO vendite (prodotto, quantita, prezzo, data)
VALUES (?, ?, ?, ?)
""", [
    ("Laptop", 2, 1200, "2026-01-10"),
    ("Mouse", 10, 20, "2026-01-11"),
    ("Monitor", 3, 300, "2026-01-12")
])

conn.commit()
```

---

# 3️⃣ Query base

```python
cursor.execute("SELECT * FROM vendite")

rows = cursor.fetchall()

for row in rows:
    print(row)
```

---

# 4️⃣ Query parametrizzate (NO SQL Injection)

❌ SBAGLIATO:

```python
prodotto = "Laptop"
cursor.execute(f"SELECT * FROM vendite WHERE prodotto = '{prodotto}'")
```

✔️ CORRETTO:

```python
cursor.execute(
    "SELECT * FROM vendite WHERE prodotto = ?",
    ("Laptop",)
)
```

Perché:

* evita SQL injection
* gestisce automaticamente escaping

---

# 5️⃣ SQL → Pandas DataFrame

Qui cambia tutto.

```python
import pandas as pd

df = pd.read_sql("SELECT * FROM vendite", conn)

print(df)
```

Ora puoi usare tutto Pandas.

---

# 6️⃣ Query + analisi

```python
df["fatturato"] = df["quantita"] * df["prezzo"]

print(df.groupby("prodotto")["fatturato"].sum())
```

---

# 7️⃣ SQLAlchemy (approccio moderno)

SQLAlchemy è lo standard per connessioni DB in Python.

```python
from sqlalchemy import create_engine

engine = create_engine("sqlite:///azienda.db")

df = pd.read_sql("SELECT * FROM vendite", engine)
```

Vantaggi:

* compatibile con PostgreSQL, MySQL, SQL Server
* più portabile rispetto a `sqlite3`

---

# 8️⃣ Query parametrizzate con SQLAlchemy

```python
query = "SELECT * FROM vendite WHERE prezzo > :min_price"

df = pd.read_sql(query, engine, params={"min_price": 100})
```

---

# 9️⃣ Quando fare join in SQL vs Pandas

## Caso 1 — JOIN in SQL (consigliato)

```sql
SELECT v.prodotto, c.nome_cliente
FROM vendite v
JOIN clienti c ON v.cliente_id = c.id
```

✔️ Meglio quando:

* dataset grande
* join complessi
* database ottimizzato

---

## Caso 2 — JOIN in Pandas

```python
df1.merge(df2, on="id")
```

✔️ Meglio quando:

* dataset già in memoria
* logica di business complessa
* manipolazioni iterative

---

## Regola pratica

* JOIN pesanti → SQL
* Trasformazioni → Pandas

---

# 🔟 Pipeline reale

```python
df = pd.read_sql("""
SELECT prodotto, quantita, prezzo
FROM vendite
""", engine)

df["fatturato"] = df["quantita"] * df["prezzo"]

summary = df.groupby("prodotto")["fatturato"].sum()

print(summary)
```

---

# 1️⃣1️⃣ Output (grafico)

```python
import matplotlib.pyplot as plt

summary.plot(kind="bar")
plt.show()
```

---

# 1️⃣2️⃣ Output Excel

```python
df.to_excel("report.xlsx", index=False)
```

---

# 1️⃣3️⃣ Confronto con SAS

## SAS

### SAS

```sql
PROC SQL;
SELECT prodotto, SUM(fatturato)
FROM vendite
GROUP BY prodotto;
QUIT;
```

### Python

```python
df = pd.read_sql("SELECT * FROM vendite", engine)
df.groupby("prodotto")["fatturato"].sum()
```

---

## Differenze

| SAS             | Python         |
| --------------- | -------------- |
| integrato       | modulare       |
| PROC SQL        | SQL + Pandas   |
| meno flessibile | più ecosistema |
| enterprise      | open source    |

---

# 1️⃣4️⃣ Pattern reale aziendale

```
DB aziendale
   ↓
Query SQL (filtri, join)
   ↓
Python (logica, orchestrazione)
   ↓
Pandas (analisi)
   ↓
Output (Excel / grafici / API)
```

---

# 1️⃣5️⃣ Errori comuni (importantissimo)

❌ Caricare tutto il DB in Pandas
✔️ filtrare in SQL

❌ usare stringhe per query
✔️ usare parametri

❌ fare join enormi in Pandas
✔️ farli nel DB

---

# 1️⃣6️⃣ Esercizio

1. Creare DB SQLite
2. Inserire dati
3. Fare query filtrata
4. Caricare in Pandas
5. Calcolare fatturato
6. Esportare Excel

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

Fagli vedere questo errore:

```python
# ERRORE CLASSICO
df = pd.read_sql("SELECT * FROM Sales.SalesOrderDetail", engine)
```

Poi chiedi:

> davvero volete portarvi 1 milione di righe in RAM?

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

