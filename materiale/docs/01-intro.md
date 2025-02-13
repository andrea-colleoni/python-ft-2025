## **📍 Sezione Introduttiva: Allineamento su Python (45-60 minuti)**

### **1️⃣ Verifica del Setup dell’Ambiente (15 minuti)**  
- ✅ **Controllo dell’installazione di Python**  
  ```bash
  python --version
  pip --version
  ```
- ✅ **Verifica di pip e moduli essenziali**  
  ```bash
  pip install pandas numpy seaborn jupyter
  ```
- ✅ **Avvio di un ambiente interattivo** (Jupyter Notebook o VS Code)  
  - Creazione di un file `.ipynb` o `.py` di prova  
  - Esecuzione di un semplice script:
    ```python
    print("Ambiente pronto!")
   ```

---

### **2️⃣ Fondamenti di Python per il Data Processing (30-40 minuti)**  

#### 🔹 **Strutture dati fondamentali**  
- **Liste**  
  ```python
  numeri = [1, 2, 3, 4, 5]
  print(numeri[0])  # Accesso
  numeri.append(6)  # Aggiunta
  ```
- **Dizionari**  
  ```python
  persona = {"nome": "Alice", "età": 30}
  print(persona["nome"])  # Accesso
  persona["età"] = 31     # Modifica
  ```
- **Set e Tuple** (concetti base)

#### 🔹 **Controllo del flusso**  
- **Condizioni**
  ```python
  if persona["età"] > 18:
      print("Adulto")
  ```
- **Cicli for e while**
  ```python
  for numero in numeri:
      print(numero)
  ```

#### 🔹 **Funzioni di base**  
```python
def saluta(nome):
    return f"Ciao, {nome}!"

print(saluta("Luca"))
```

---

### **3️⃣ Mini-Quiz o Verifica Pratica (10 minuti)**  
Un esercizio pratico veloce:
- Creare una lista di numeri da 1 a 10
- Filtrare solo i numeri pari usando un ciclo
- Creare un dizionario con il numero come chiave e il suo quadrato come valore

---

## 📂 **Struttura Base di un Progetto Python**

```plaintext
progetto_python/
├── main.py               # Script principale per avviare il progetto
├── requirements.txt      # Dipendenze del progetto
├── README.md             # Documentazione di base del progetto
├── data/                 # File di dati esterni (CSV, JSON, ecc.)
│   └── dataset.csv
├── src/                  # Codice sorgente del progetto
│   ├── __init__.py       # Rende la cartella un modulo Python
│   ├── modulo_a.py       # Un modulo specifico
│   └── modulo_b.py       # Un altro modulo
└── tests/                # Test del progetto
    └── test_modulo_a.py
```

---

## ✅ **1️⃣ Importazione di Moduli Interni**

Se vuoi importare una classe o funzione da un file all'altro:

### **Esempio:**  
📄 `src/modulo_a.py`
```python
def saluta(nome):
    return f"Ciao, {nome}!"
```

📄 `main.py`
```python
from src.modulo_a import saluta

print(saluta("Marco"))
```

### **Import Relative (quando si lavora dentro la stessa cartella)**  
📄 `src/modulo_b.py`
```python
from .modulo_a import saluta

def saluto_speciale(nome):
    return saluta(nome).upper()
```

---

## 📊 **2️⃣ Gestione di File Esterni**

### **Leggere un file CSV da una cartella `data/`:**
```python
import pandas as pd

# Percorso relativo
df = pd.read_csv("data/dataset.csv")
print(df.head())
```

### **Best Practice:**  
- Mantieni i dati esterni in una cartella dedicata (`data/`).
- Usa percorsi relativi per la portabilità.

---

## 🗂️ **3️⃣ Virtual Environment e Dipendenze**

Crea un ambiente virtuale per gestire le dipendenze:
```bash
python -m venv corso
source corso/bin/activate  # Linux/Mac
corso\Scripts\activate     # Windows
```
Installa pacchetti:
```bash
pip install pandas numpy
pip freeze > requirements.txt
```
Per ripristinare l’ambiente:
```bash
pip install -r requirements.txt
```

---

## 🌍 **1️⃣ Cosa sono gli Environment?**

Un **environment (ambiente virtuale)** è un ambiente isolato che contiene una specifica versione di Python e i pacchetti necessari per un progetto.

### **Perché sono utili?**  
- Evitano conflitti tra librerie di progetti diversi.  
- Permettono di testare software con versioni diverse di Python o pacchetti.  
- Facilitano la gestione delle dipendenze in team di lavoro.

---

## ⚙️ **2️⃣ Come si Creano?**

### **Con `venv` (modulo standard di Python):**

1. **Crea un nuovo ambiente virtuale:**
   ```bash
   python -m venv nome_ambiente
   ```

2. **Attiva l’ambiente:**
   - **Linux/Mac:** 
     ```bash
     source nome_ambiente/bin/activate
     ```
   - **Windows:** 
     ```bash
     nome_ambiente\Scripts\activate
     ```

3. **Installa pacchetti nell’ambiente attivo:**
   ```bash
   pip install pandas numpy
   ```

4. **Disattiva l’ambiente:**
   ```bash
   deactivate
   ```

---

## 🔄 **3️⃣ Cambiare o Gestire Environment**

- **Verificare l’ambiente attivo:**
  ```bash
  which python  # Linux/Mac
  where python  # Windows
  ```

- **Passare da un ambiente all’altro:**
  Basta disattivare l’ambiente corrente con `deactivate` e attivare il nuovo ambiente come descritto sopra.

---

## 🧹 **4️⃣ Pulizia e Gestione delle Dipendenze**

- **Eliminare un ambiente:**  
  Basta cancellare la cartella:
  ```bash
  rm -rf nome_ambiente  # Linux/Mac
  rmdir /s nome_ambiente  # Windows
  ```

- **Gestire le dipendenze:**  
  - **Esporta le dipendenze in un file:**
    ```bash
    pip freeze > requirements.txt
    ```
  - **Importa le dipendenze su un nuovo ambiente:**
    ```bash
    pip install -r requirements.txt
    ```

---

## 🧪 **5️⃣ Esercizio per il Corso**

1. Crea un ambiente virtuale chiamato `env_test`.  
2. Attivalo e installa `pandas` e `matplotlib`.  
3. Esporta le dipendenze in `requirements.txt`.  
4. Disattiva l’ambiente e ricrea tutto da zero in un altro ambiente.  

---


## 📓 **Cos'è Jupyter Notebook?**

Jupyter Notebook è un ambiente interattivo che consente di scrivere e eseguire codice Python in celle. È particolarmente utile per:
- **Data Analysis** e **Data Visualization**
- **Documentazione integrata** con testo e codice
- **Esecuzione interattiva** e sperimentazione rapida

---

## 🛠️ **1️⃣ Installazione e Avvio**

### **Installazione:**
Se non è già installato:
```bash
pip install notebook
```
Oppure, con **JupyterLab** (versione più moderna):
```bash
pip install jupyterlab
```

### **Avvio:**
```bash
jupyter notebook
# oppure
jupyter lab
```
Si aprirà automaticamente nel browser all’indirizzo `http://localhost:8888/`.

---

## 🚀 **2️⃣ Struttura di un Notebook**

Un notebook ha estensione `.ipynb` ed è composto da **celle**:

- 🔢 **Celle di Codice**: per scrivere ed eseguire codice Python.  
- 📝 **Celle di Testo (Markdown)**: per aggiungere documentazione, titoli, elenchi, formule matematiche.

### **Esempio di Cell di Codice:**
```python
import pandas as pd

# Caricamento di un dataset
df = pd.read_csv('data/dataset.csv')
df.head()
```

### **Esempio di Cell di Testo (Markdown):**
```markdown
# Analisi dei Dati 📊
Questo notebook mostra come caricare e analizzare un dataset.
```
Per eseguire una cella: **`Shift + Enter`**

---

## ⚡ **3️⃣ Funzionalità Utili**

- **Tab Completion**: scrivi `pd.re` e premi `Tab` per suggerimenti automatici.
- **Magic Commands** (per operazioni rapide):
  ```python
  %timeit sum(range(1000000))  # Misura il tempo di esecuzione
  %lsmagic                    # Mostra tutti i comandi magic disponibili
  ```

- **Grafici Inline**:
  ```python
  import matplotlib.pyplot as plt
  %matplotlib inline

  plt.plot([1, 2, 3], [4, 5, 6])
  plt.show()
  ```

---

## 📊 **4️⃣ Salvataggio e Esportazione**

- **Salvataggio automatico** mentre lavori.
- **Esportazione**: `File → Download as → PDF/HTML/Markdown` per condividere i risultati.

---

## 💡 **5️⃣ Esercizio Pratico per il Corso**

1. **Avvia un Jupyter Notebook.**  
2. **Crea una cella di codice:** carica un file CSV semplice (es. Titanic Dataset).  
3. **Aggiungi una cella di testo:** descrivi i dati caricati.  
4. **Visualizza un semplice grafico.**
