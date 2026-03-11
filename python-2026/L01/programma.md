# 1. Lettura e analisi di PDF con Python (2–3h)

### Obiettivo

Estrarre dati *utili* da PDF semi-strutturati (report, tabelle, questionari), capire **quando funziona e quando no**.

### Contesto

* PDF ≠ formato dati
* PDF “testuale” vs PDF “scansione”

### Librerie

* `PyPDF2` / `pdfplumber` → testo
* `tabula-py` / `camelot` → tabelle
* `pytesseract` (+ Tesseract) → OCR

### Esempi

* Estrazione testo da report PDF
* Estrazione tabella → DataFrame Pandas
* Pulizia base dei dati estratti
* Mini-pipeline: PDF → pandas → CSV

### Limiti da chiarire

* Layout complessi = dolore
* OCR ≠ affidabile al 100%
* Serve sempre validazione umana

---

# 2. Approfondimenti Pandas / NumPy “da lavoro vero” (2–3h)

### Obiettivo

Passare da “lo uso” a **“lo uso bene e più veloce”**.

### Pandas (core)

* `groupby` avanzato
* `apply` vs `map` vs `vectorization`
* join/merge non banali
* datetime *come si deve*
* performance: copie inutili, dtype, `categorical`

### NumPy

* broadcasting (spiegato con esempi visivi)
* maschere booleane
* differenza reale tra numpy e pandas

### Esempi

* Dataset statistico reale (survey, KPI, serie temporali)
* Refactor di codice “lento ma leggibile” → “veloce e pulito”

---

# 3. Interrogazioni SQL da Python (2–3h)

### Obiettivo

Integrare Python con database aziendali.

### Contesto

* Python **non sostituisce SQL**
* Python **orchestra** SQL

### Stack

* `sqlite3` (per demo)
* `SQLAlchemy`
* `pandas.read_sql`

### Argomenti

* Connessioni
* Query parametrizzate (no SQL injection)
* Mapping SQL → DataFrame
* Quando fare join in SQL e quando in Pandas

### Esempi

* Query + analisi statistica
* Pipeline DB → pandas → grafico / output

### Confronto con SAS

* PROC SQL vs Python+SQL
* Vantaggi di integrazione

---

# 5️. Machine Learning: cosa è davvero utile (2–3h)

### Obiettivo

Smontare il mito del ML e usarlo **bene**.

### Contesto

* ML ≠ AI magica
* Statistica classica vs ML
* Quando usarlo *davvero*

### Stack

* `scikit-learn`

### Argomenti

* supervised vs unsupervised
* train/test split
* feature engineering (base)
* overfitting spiegato senza formule inutili

### Esempi

* classificazione semplice
* regressione
* clustering esplorativo