# 🫁 NSCLC Virtual Biopsy: EGFR Mutation Predictor

## Descrierea Proiectului
Acest proiect dezvoltă un sistem inteligent tip "biopsie virtuală" pentru a asista medicii radiologi și oncologi în diagnosticarea și tratamentul cancerului pulmonar (Non-Small Cell Lung Cancer - NSCLC). 

Sistemul propus elimină necesitatea unei proceduri invazive imediate, analizând texturile, forma și intensitatea din scanările CT (prin intermediul pipeline-urilor de Radiomics) pentru a prezice **mutația genetică EGFR**. Această predicție ghidează rapid medicii către prescrierea tratamentelor țintite corespunzătoare.

## ⚙️ Instalare și Configurare (Setup)
Pentru a asigura reproductibilitatea proiectului și pentru a evita conflictele între librării, te rugăm să folosești mediul virtual local (`venv`).

### 1. Crearea mediului virtual
Deschide terminalul în folderul principal al proiectului și rulează:
```bash
python -m venv venv
```

### 2. Activarea mediului virtual
* **Pe Windows:**
  ```bash
  venv\Scripts\activate
  ```
* **Pe macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```
*(Odată activat, ar trebui să vezi prefixul `(venv)` în linia de comandă.)*

### 3. Instalarea dependențelor
Instalează pachetele necesare rulând:
```bash
pip install -r requirements.txt
```

### 4. Rularea aplicației (Interfața de bază - Etapa 1)
Pentru a porni interfața web dezvoltată cu Streamlit, rulează:
```bash
streamlit run app.py
```
Aplicația se va deschide automat într-un tab nou în browser-ul tău implicit la adresa `http://localhost:8501`.