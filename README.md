# 🫁 NSCLC Virtual Biopsy: EGFR Mutation Predictor

## Project Description
This project develops a "virtual biopsy" intelligent system to assist radiologists and oncologists in diagnosing and treating lung cancer (Non-Small Cell Lung Cancer - NSCLC). 

The proposed system eliminates the need for an immediate invasive procedure by analyzing the textures, shape, and intensity of CT scans (via Radiomics pipelines) to predict the **EGFR genetic mutation**. This prediction quickly guides doctors toward prescribing appropriate targeted treatments.

## ⚙️ Installation and Setup
To ensure project reproducibility and avoid library conflicts, please use the local virtual environment (`venv`).

### 1. Create the virtual environment
Open the terminal in the main project folder and run:
```bash
python -m venv venv
```

### 2. Activate the virtual environment
* **On Windows:**
  ```bash
  venv\Scripts\activate
  ```
* **On macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```
*(Once activated, you should see the `(venv)` prefix in the command line.)*

### 3. Install dependencies
Install the required packages by running:
```bash
pip install -r requirements.txt
```

### 4. Run the application (Base Interface - Phase 1)
To start the web interface developed with Streamlit, run:
```bash
streamlit run app.py
```
The application will automatically open in a new tab in your default browser at `http://localhost:8501`.