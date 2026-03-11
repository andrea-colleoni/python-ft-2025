# 1️⃣ Apertura (20–30 min)

## PDF ≠ formato dati

Un PDF è:

* un formato di impaginazione
* una descrizione grafica (coordinate, font, box)
* NON un formato strutturato come JSON, XML, CSV

Quindi:

* Non esistono “righe”
* Non esistono “colonne”
* Esiste solo testo posizionato nello spazio

### Tipi di PDF

| Tipo          | Cosa contiene    | Estraibile facilmente? |
| ------------- | ---------------- | ---------------------- |
| PDF testuale  | Testo reale      | ✅ Sì                   |
| PDF scansione | Solo immagine    | ❌ Serve OCR            |
| PDF misto     | Testo + immagini | ⚠ Dipende              |

Mostra questo comando per capire se un PDF contiene testo:

```python
from PyPDF2 import PdfReader

reader = PdfReader("file.pdf")
print(reader.pages[0].extract_text())
```

Se ritorna `None` → è una scansione.

---

# 2️⃣ Estrazione testo – pdfplumber (40 min)

Tra `PyPDF2` e `pdfplumber`, per didattica scegli **pdfplumber**:

* più stabile
* supporta bounding box
* migliore per layout

## Installazione

```bash
pip install pdfplumber
```

---

## PDF di test collaudato

Usa questo PDF pubblico (report ONU, molto usato nei test):

```
https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf
```

Oppure (meglio per report reale):

```
https://www.sec.gov/files/form-10k.pdf
```

Scaricalo prima.

---

## Estrazione semplice

```python
import pdfplumber

with pdfplumber.open("report.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        print(text)
```

Spiega:

* `.pages`
* `.extract_text()`
* perdita della struttura

---

## Estrazione con coordinate

Mostra che il testo ha posizione:

```python
with pdfplumber.open("report.pdf") as pdf:
    page = pdf.pages[0]
    words = page.extract_words()

    for w in words[:10]:
        print(w)
```

Output esempio:

```python
{'text': 'Annual', 'x0': 72.0, 'x1': 120.3, 'top': 80.2, ...}
```

Qui puoi spiegare:

* coordinate X/Y
* ricostruzione layout
* perché le colonne non sono “vere colonne”

---

# 3️⃣ Estrazione Tabelle (45–60 min)

Qui inizia il divertimento.

## Librerie

* `tabula-py` (richiede Java)
* `camelot` (molto potente)
* `pdfplumber` (estrazione semplice)

Per semplicità didattica: **pdfplumber + camelot**

---

## PDF test con tabelle funzionanti

Ottimo esempio pubblico:

```
https://camelot-py.readthedocs.io/en/master/_static/pdf/foo.pdf
```

Scaricalo come `tables.pdf`

---

## Metodo 1: pdfplumber

```python
import pdfplumber
import pandas as pd

with pdfplumber.open("tables.pdf") as pdf:
    page = pdf.pages[0]
    table = page.extract_table()

df = pd.DataFrame(table[1:], columns=table[0])
print(df)
```

Qui puoi mostrare:

* prima riga = header
* resto = dati

---

## Metodo 2: camelot (più robusto)

Installazione:

```bash
pip install camelot-py[cv]
```

Codice:

```python
import camelot

tables = camelot.read_pdf("tables.pdf", pages="1")

print(tables)
print(tables[0].df)
```

Esempio conversione CSV:

```python
tables[0].to_csv("output.csv")
```

Spiega i due approcci:

```python
camelot.read_pdf("file.pdf", flavor="lattice")
camelot.read_pdf("file.pdf", flavor="stream")
```

| Modalità | Funziona quando            |
| -------- | -------------------------- |
| lattice  | tabelle con linee visibili |
| stream   | tabelle senza linee        |

Fai vedere che una delle due spesso fallisce.

Questo è un punto didattico importantissimo.

---

# 4️⃣ OCR con pytesseract (30–40 min)

Qui devi far capire che cambia tutto.

## Installazione

Serve:

* Tesseract installato nel sistema
* pip install pytesseract
* pip install pdf2image

---

## Pipeline OCR

```python
from pdf2image import convert_from_path
import pytesseract

pages = convert_from_path("scanned.pdf")

for i, page in enumerate(pages):
    text = pytesseract.image_to_string(page, lang="ita")
    print(text)
```

Spiega:

* conversione PDF → immagini
* OCR → testo grezzo
* errori tipici: O/0, I/1

---

## Dimostrazione errore

Mostra come OCR sbaglia:

```python
text = pytesseract.image_to_string(page)
print(text)
```

Poi fai cercare un valore numerico con regex e mostra che non sempre lo trova.

---

# 5️⃣ Mini pipeline reale (30 min)

Obiettivo:

PDF con tabella → pandas → pulizia → CSV

```python
import camelot
import pandas as pd

tables = camelot.read_pdf("tables.pdf", pages="1")
df = tables[0].df

# Pulizia base
df.columns = df.iloc[0]
df = df[1:]
df = df.reset_index(drop=True)

# Rimozione simboli
df["Amount"] = df["Amount"].str.replace("$", "").astype(float)

df.to_csv("clean_output.csv", index=False)
```

Qui puoi spiegare:

* pulizia colonne
* conversione tipi
* validazione

---

# 6️⃣ Limiti (fondamentale, 15–20 min)

Qui devi essere brutalmente onesto.

## Layout complessi

* Tabelle spezzate su più pagine
* Colonne non allineate
* Box grafici

→ Le librerie falliscono.

---

## OCR non è magia

* qualità scansione
* font
* rumore
* lingua

OCR produce testo probabilistico.

---

## Punto chiave da far passare

> L’estrazione PDF è sempre un compromesso.
> In produzione serve sempre validazione.

Se l’azienda può fornire:

* CSV
* Excel
* API
* XML

→ Meglio mille volte.

---

# 7️⃣ Struttura consigliata della lezione (timeline)

| Tempo   | Attività                         |
| ------- | -------------------------------- |
| 0–20    | Cos’è un PDF davvero             |
| 20–60   | Estrazione testo                 |
| 60–120  | Tabelle con pdfplumber + camelot |
| 120–150 | OCR                              |
| 150–180 | Mini progetto finale             |

---

# 8️⃣ Materiale che puoi fornire agli studenti

Consiglierei:

* Cartella `/pdf_samples`

  * dummy.pdf
  * tables.pdf
  * scanned.pdf
* Notebook Jupyter pronto
* Esercizio finale:

  * estrai totale fattura
  * salva CSV pulito

---

# 9️⃣ Esercizio finale per loro

“Dato un PDF di report con tabella vendite:

1. estrai tabella
2. converti in DataFrame
3. rimuovi righe vuote
4. salva CSV
5. calcola totale colonna importi”
