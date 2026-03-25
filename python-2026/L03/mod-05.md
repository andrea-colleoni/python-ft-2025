# Machine Learning: cosa è davvero utile (2–3h)

## Messaggio chiave (apertura, 5 min)

> Il Machine Learning non è magia.
> È un modo per **trovare pattern nei dati quando le regole esplicite non bastano**.


> Se puoi scrivere una query SQL, probabilmente non ti serve ML.

Questa è un'ancora alla realtà.

---

# 1. Cos’è davvero il ML (15 min)

## Definizione concreta

> Un modello ML è una funzione che impara dai dati:
> input → output

Esempi:

* cliente → churn sì/no
* caratteristiche casa → prezzo
* comportamento → cluster

---

## Il concetto di “apprendimento”

### Esempio intuitivo

```text
Superficie → Prezzo

50mq → 100k  
80mq → 160k  
100mq → 210k
```

→ il modello impara la relazione

---

# 2. Supervised vs Unsupervised (15 min)

## Supervised

Hai etichetta (target)

* classificazione → categoria
* regressione → numero

Esempi:

* spam / non spam
* prezzo casa

---

## Unsupervised

Non hai target

* clustering
* segmentazione

Esempi:

* segmentazione clienti
* gruppi di comportamento

---

## Frase da incidere

> Se hai la risposta, è supervised.
> Se stai cercando la struttura, è unsupervised.

---

# Mini Cheat Sheet – `scikit-learn`

## Il flusso base (da memorizzare)

```python
# 1. split
X_train, X_test, y_train, y_test = train_test_split(X, y)

# 2. modello
model = SomeModel()

# 3. training
model.fit(X_train, y_train)

# 4. predizione
y_pred = model.predict(X_test)

# 5. valutazione
score = some_metric(y_test, y_pred)
```

Se capiscono questo, hanno già il 70% del gioco.

---

# Funzioni chiave

## `train_test_split`

Divide i dati in:

* **training set** → per imparare
* **test set** → per valutare

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)
```

### Concetti importanti

* `test_size=0.2` → 20% dati per test
* `random_state` → rende i risultati ripetibili

### Traduzione umana

> Alleno su una parte dei dati e verifico su dati mai visti.

---

## `model.fit(X, y)`

Allena il modello.

```python
model.fit(X_train, y_train)
```

### Cosa succede davvero

* il modello “impara” una relazione tra input (`X`) e output (`y`)

### Traduzione umana

> Qui il modello studia.

---

## `model.predict(X)`

Fa previsioni usando il modello già addestrato.

```python
y_pred = model.predict(X_test)
```

### Output

* classificazione → classi (0/1)
* regressione → numeri

### Traduzione umana

> Qui il modello viene interrogato.

---

## Metriche di valutazione

### `accuracy_score`

Per classificazione

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
```

### Significato

> Percentuale di risposte corrette

---

### (Opzionale) `mean_squared_error`

Per regressione

```python
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, y_pred)
```

### Significato

> Quanto le previsioni sono lontane dai valori reali

---

# Modelli usati

## `DecisionTreeClassifier`

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(max_depth=3)
```

* modello semplice
* facile da capire
* tende a overfittare se non limitato

---

## `LinearRegression`

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
```

* usato per predire valori numerici
* assume relazione lineare

---

## `KMeans`

```python
from sklearn.cluster import KMeans

model = KMeans(n_clusters=3)
```

* clustering (unsupervised)
* raggruppa dati simili

---

# Concetti fondamentali

## `X` vs `y`

* `X` → caratteristiche (input)
* `y` → target (output)

```python
X = df[['Age', 'Pclass']]
y = df['Survived']
```

---

## Training vs Test

* training → il modello impara
* test → il modello viene giudicato

---

## Overfitting (in una riga)

> Il modello impara troppo bene i dati di training e fallisce su quelli nuovi.

---

# Pattern mentale corretto

Non devono pensare:

> “Uso DecisionTree”

Devono pensare:

1. Che problema ho?
2. Ho un target?
3. Che tipo di output voglio?
4. Solo dopo → scelgo il modello

---

# Warning finale

> Se copi questo schema senza capire i dati, non stai facendo Machine Learning.
> Stai eseguendo codice.

---

# Regressione Lineare

## Cos’è (in una frase)

Trova una **retta (o piano)** che approssima la relazione tra variabili.

## Come ragiona

> “Se X cresce, quanto cresce Y?”

Esempio:

* metri quadri → prezzo casa

## Cosa produce

Un **numero continuo** (es. 185.000 €)

## Pro

* semplice
* interpretabile
* veloce

## Contro

* funziona male se la relazione **non è lineare**

## Immagine mentale

> Una linea che cerca di stare “il più vicino possibile” a tutti i punti

---

# Decision Tree

## Cos’è (in una frase)

Un modello che prende decisioni tramite una serie di **if/else**

## Come ragiona

> “Se età > 30 → vai a destra, altrimenti a sinistra”

Esempio:

* età, sesso → sopravvivenza (Titanic)

## Cosa produce

* classificazione → sì/no
* oppure numeri (versione regressione)

## Pro

* facile da capire
* gestisce bene dati non lineari

## Contro

* tende a **overfittare** (memorizza troppo)

## Immagine mentale

> Un diagramma a blocchi pieno di domande

---

# K-Means

## Cos’è (in una frase)

Divide i dati in **gruppi simili tra loro** senza sapere le etichette.

## Come ragiona

> “Questi punti sono vicini → stanno nello stesso gruppo”

## Cosa produce

* un’etichetta di cluster (0, 1, 2…)

## Pro

* semplice
* utile per esplorazione dati

## Contro

* devi scegliere tu il numero di cluster
* non sempre i gruppi hanno senso reale

## Immagine mentale

> Tante nuvole di punti, ognuna con un “centro”

---

# Confronto rapido (utile da dire a voce)

* Regressione lineare → **prevedo un numero**
* Decision tree → **prendo decisioni**
* K-means → **scopro gruppi**

---

# Chiusura forte (consigliata)

> Non esiste “l’algoritmo migliore”.
> Esiste quello giusto per il problema.


# 3. Primo esempio (classificazione) (30 min)

## Dataset (Kaggle semplice e pulito)

Consiglio:

* **Titanic** (perfetto didatticamente)

---

## Codice completo

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# carica dataset
df = pd.read_csv("titanic.csv")

# pulizia base
df = df[['Survived', 'Pclass', 'Sex', 'Age']].dropna()
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# feature / target
X = df[['Pclass', 'Sex', 'Age']]
y = df['Survived']

# split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# modello
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# predizione
y_pred = model.predict(X_test)

# valutazione
print("Accuracy:", accuracy_score(y_test, y_pred))
```

---

## Cosa si capisce QUI

* `fit` = apprendimento
* `predict` = uso del modello
* `train/test` = non barare

---

## Esercizio 1

> Cambiare modello:

* `DecisionTree` → `LogisticRegression`

---

# 4. Overfitting (20 min)

Qui devi si vede la differenza.

## Spiegazione semplice (senza formule)

> Overfitting = il modello memorizza invece di capire

### Esempio umano

* studente che impara a memoria vs uno che capisce

---

## Demo veloce

```python
model = DecisionTreeClassifier(max_depth=None)  # overfit facile
```

vs

```python
model = DecisionTreeClassifier(max_depth=3)
```

→ confronta accuracy train/test

---

## Frase forte

> Se il tuo modello è perfetto, probabilmente è sbagliato.

---

# 5. Regressione (20 min)

## Caso semplice

Prezzo casa (puoi usare anche un CSV Kaggle tipo Housing)

---

## Codice

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)
```

---

## Concetto chiave

> Qui non stai classificando → stai stimando un valore continuo

---

## Esercizio 2

> Prevedere prezzo vs classificare fascia prezzo

---

# 6. Clustering (unsupervised) (20 min)

## Dataset semplice

Puoi usare:

* clienti (anche fake)
* oppure subset Kaggle

---

## Codice

```python
from sklearn.cluster import KMeans

model = KMeans(n_clusters=3)

df_cluster = df[['Age', 'Fare']].dropna()

model.fit(df_cluster)

df_cluster['Cluster'] = model.labels_
```

---

## Cosa dire chiaramente

* non c’è “giusto o sbagliato”
* stai creando gruppi

---

## Esercizio 3

> Cambiare numero cluster e osservare

---

# 7. Feature Engineering (15 min)

Qui fai il ponte con pandas (molto importante)

## Esempio Titanic

```python
df['FamilySize'] = df['SibSp'] + df['Parch']
```

---

## Messaggio chiave

> I modelli non sono intelligenti.
> I dati sì.

---

# 8. Scikit-learn: perché è potente (10 min)

Notare che:

* API coerente (`fit`, `predict`)
* cambi modello in 1 riga
* pipeline rapide

---

## Demo veloce

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(X_train, y_train)
```

---

# 9. Quando NON usare ML (fondamentale, 10 min)

Non usare ML se:

* hai poche righe
* puoi scrivere regole
* non puoi spiegare il risultato

---

## Frase finale da lasciare

> Il ML è utile quando i dati sono troppi o troppo complessi per le regole.
> Non quando vuoi fare qualcosa di “figo”.

---

# Mini progetto finale (30 min opzionale)

> Costruire un modello che:

1. pulisce dati
2. allena modello
3. stampa metriche

---

# Nota critica

Se vediamo:

* Titanic
* accuracy
* albero decisionale

Si potrebbe pensare:

> “ok, ML = lanciare 4 righe di sklearn”

Questo è **pericoloso**.

Per evitarlo, devi ribadire 3 cose:

1. il 70% del lavoro è nei dati
2. il modello è la parte facile
3. capire *quando usarlo* vale più che usarlo

