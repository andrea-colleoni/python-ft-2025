# 2. Approfondimenti Pandas / NumPy “da lavoro vero”

### Obiettivo

Passare da “lo uso” a **“lo uso bene e più veloce”**, con focus su performance e praticità quotidiana.

---

## 1️⃣ Setup iniziale

```python
import pandas as pd
import numpy as np

# Opzionale: visualizzazione più chiara dei DataFrame
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 20)
pd.set_option('display.float_format', '{:.2f}'.format)
```

Esempio dataset simulato “survey / KPI”:

```python
np.random.seed(42)
df = pd.DataFrame({
    'employee': np.random.choice(['Alice','Bob','Charlie','Diana'], size=20),
    'department': np.random.choice(['Sales','Tech','HR'], size=20),
    'month': pd.date_range('2026-01-01', periods=20, freq='M'),
    'sales': np.random.randint(50, 500, size=20),
    'hours_worked': np.random.randint(120, 200, size=20)
})

df.head()
```

---

## 2️⃣ Pandas avanzato

### 2.1 GroupBy complesso

```python
# Totale vendite per dipartimento e media ore lavorate
agg = df.groupby('department').agg(
    total_sales=('sales','sum'),
    avg_hours=('hours_worked','mean')
).reset_index()
print(agg)
```

* `agg()` permette di fare più operazioni su colonne diverse.
* `reset_index()` evita multi-index fastidiosi.

---

### 2.2 Apply vs Map vs Vectorization

```python
# Map veloce su una colonna singola
df['bonus_map'] = df['sales'].map(lambda x: x*0.05)

# Apply su più colonne
df['efficiency_apply'] = df.apply(lambda row: row.sales / row.hours_worked, axis=1)

# Vectorization: più veloce
df['efficiency_vect'] = df['sales'] / df['hours_worked']

# Confronto performance
%timeit df['sales'].map(lambda x: x*0.05)
%timeit df.apply(lambda row: row.sales / row.hours_worked, axis=1)
%timeit df['sales'] / df['hours_worked']
```

💡 **Regola pratica:** preferire sempre vectorization → molto più veloce e leggibile.

---

### 2.3 Join / Merge non banali

```python
dept_info = pd.DataFrame({
    'department': ['Sales','Tech','HR'],
    'manager': ['Mara','Luca','Sara'],
    'budget': [10000, 20000, 5000]
})

df_merged = df.merge(dept_info, on='department', how='left')
print(df_merged.head())
```

* `how='left'` mantiene tutti i record del DataFrame principale.
* Puoi usare anche `how='outer','inner','right'`.

---

### 2.4 DateTime come si deve

```python
df['month'] = pd.to_datetime(df['month'])

# Estrazione anno e trimestre
df['year'] = df['month'].dt.year
df['quarter'] = df['month'].dt.quarter

# Filtrare per range di date
df_jan = df[(df['month'] >= '2026-01-01') & (df['month'] <= '2026-03-31')]
```

💡 Attenzione: le date in stringa vs datetime non sono intercambiabili → converti sempre con `pd.to_datetime()`.

---

### 2.5 Performance: copie inutili, dtype, categorical

```python
# Prima: stringhe come object → pesante
print(df.dtypes)

# Ottimizzazione: convertire colonne categoriali
df['employee'] = df['employee'].astype('category')
df['department'] = df['department'].astype('category')

# Verifica memoria
print(df.info(memory_usage='deep'))
```

* Convertire colonne con pochi valori unici in `category` riduce RAM e accelera groupby/join.
* Evitare di fare `df_copy = df` se non serve: molte operazioni Pandas fanno già copie implicite.

---

## 3️⃣ NumPy avanzato

### 3.1 Broadcasting

```python
arr = np.array([1,2,3])
mat = np.ones((3,3))

# Somma riga singola a ogni riga
print(mat + arr)  # broadcasting
```

* Broadcasting = allineamento automatico di dimensioni compatibili.
* Fondamentale per vectorization e performance.

---

### 3.2 Maschere booleane

```python
# Tutti i record con vendite > 300
mask = df['sales'] > 300
high_sales = df[mask]
print(high_sales)

# Maschera combinata
high_efficiency = df[(df['sales']/df['hours_worked'] > 2.5) & (df['department']=='Tech')]
print(high_efficiency)
```

---

### 3.3 Differenza reale tra NumPy e Pandas

```python
# NumPy puro
sales = np.array(df['sales'])
hours = np.array(df['hours_worked'])
efficiency_np = sales / hours  # velocissimo
```

* **NumPy** = array multidimensionali, operazioni numeriche velocissime
* **Pandas** = DataFrame/Serie con etichette, ottimo per dataset “da lavoro reale”, ma leggermente più lento su operazioni numeriche pure
* Regola: usare Pandas per manipolazione e NumPy per calcoli pesanti / vettorializzati.

---

## 4️⃣ Refactor codice lento → veloce

### Lento ma leggibile

```python
efficiency = []
for i, row in df.iterrows():
    efficiency.append(row['sales']/row['hours_worked'])
df['efficiency'] = efficiency
```

### Veloce e pulito

```python
df['efficiency'] = df['sales'] / df['hours_worked']
```

* Senza cicli espliciti → vectorization.
* Meglio performance, leggibile, facile da mantenere.

---

## 5️⃣ Mini pipeline “da lavoro vero”

```python
# Groupby avanzato + join + filter
result = (
    df.merge(dept_info, on='department', how='left')
      .assign(efficiency=lambda x: x['sales']/x['hours_worked'])
      .query('efficiency > 2')
      .groupby(['department','manager'])
      .agg(total_sales=('sales','sum'), avg_efficiency=('efficiency','mean'))
      .reset_index()
)
print(result)
```

* Qui combiniamo tutto: merge, lambda, query, groupby multiplo, aggregazioni.
* Esempio tipico da lavoro reale.
