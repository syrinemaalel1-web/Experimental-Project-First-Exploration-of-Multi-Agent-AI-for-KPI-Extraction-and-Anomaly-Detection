# Experimental Project — First Exploration of Multi-Agent AI for KPI Extraction and Anomaly Detection

> ⚠️ **Experimental / Personal Learning Project** — This is a first personal exploration of Multi-Agent AI systems. The project is not production-ready and is shared for educational and experimental purposes only.

---

## 📖 Overview

This project is a personal experiment exploring how **Multi-Agent AI architectures** can be applied to automatically extract Key Performance Indicators (KPIs) from financial PDF reports and detect anomalies in those KPIs.

The experiment was conducted on two real Tunisian company reports:
- **Attijari Bank Tunisie** — Q1 2024 financial report (banking sector)
- **Inetum Tunisie** — Q1 2024 financial report (digital services / tech sector)

The system combines **RAG (Retrieval-Augmented Generation)**, **LLM-based extraction**, and **statistical anomaly detection** in a pipeline orchestrated across multiple specialized agents.

---

## 🎯 Project Status

| Status | Description |
|--------|-------------|
| 🧪 **Experimental** | First personal exploration — not production-ready |
| ✅ **Partially functional** | Core pipeline executed and produced real outputs |
| ⚠️ **Not structured** | Code lives in Jupyter notebooks, no CLI or API |
| 📚 **Learning project** | Built to understand Multi-Agent AI concepts in practice |

---

## 💡 Motivation & Context

Traditional financial report analysis requires significant manual work: reading PDFs, locating the right tables, extracting specific figures, and comparing them to benchmarks. This project explores whether a chain of specialized AI agents can automate this process end-to-end on real financial documents.

**Key research questions explored:**
- Can RAG reliably locate specific financial metrics in PDF-extracted text?
- Can an LLM extract structured KPIs with high accuracy from financial documents?
- Can statistical methods detect anomalies in a small set of extracted KPIs?
- How can these steps be chained in a multi-agent pipeline?

---

## 🎯 Objectives

- **KPI Extraction** — Automatically identify and extract financial indicators (PNB, ROE, ROA, total bilan, etc.) from PDF reports
- **Advanced Analysis** — Compute derived metrics, apply sector benchmarks, classify KPIs by category
- **Anomaly Detection** — Flag KPI values that fall outside expected sectoral ranges using Z-scores and threshold rules
- **Multi-Agent Orchestration** — Chain specialized agents: PDF extraction → vectorstore → KPI agent → anomaly agent → report agent

---

## 🏗️ Architecture

```
[PDF Report]
     │
     ▼
┌─────────────────────────────────────┐
│  Agent 0 — PDF Text Extractor       │  (Docling)
│  PDF → plain text → chunked docs    │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│  RAG Pipeline                       │  (LangChain + ChromaDB)
│  Chunks → Embeddings → VectorStore  │  (sentence-transformers/all-MiniLM-L6-v2)
│  MMR Retrieval (top-k=5)            │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│  Agent 1 — Banking KPI Extractor    │  (LLM via Groq API)
│  Structured extraction of 14+ KPIs  │  (llama-3.1-8b-instant)
│  Confidence scoring per KPI         │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│  Agent 2 — Advanced KPI Analyzer    │  (LLM + pandas)
│  Derived metrics, sector benchmarks │
│  Categorization, trend analysis     │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│  Agent 3 — Anomaly Detector         │  (Z-score + sector thresholds)
│  Statistical detection              │
│  Severity scoring (low/med/high)    │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│  Agent 4 — Report Generator         │  (LLM + HTML/ReportLab)
│  Interactive HTML reports           │
│  PDF report generation              │
└─────────────────────────────────────┘
```

---

## 🤖 Agents — Roles & Implementation Status

| Agent | Name | Role | Status |
|-------|------|------|--------|
| Agent 0 | **PDF Extractor** | Converts PDF to text using Docling, chunks text for RAG | ✅ Working |
| Agent 1 | **Banking KPI Extractor** | LLM-based extraction of 14 standard banking KPIs from RAG context | ✅ Working |
| Agent 2 | **Advanced KPI Analyzer** | Computes additional derived metrics, applies sector benchmarks | ✅ Working |
| Agent 3 | **Anomaly Detector** | Z-score analysis + sector threshold comparison | ✅ Working |
| Agent 4 | **Report Generator** | Generates HTML interactive reports and PDF summaries | ✅ Partially working (HTML output confirmed) |

> **Note:** Agents are implemented as Python classes in Jupyter notebooks, not as independent microservices or async processes. "Multi-agent" here refers to the conceptual decomposition into specialized roles — coordination is sequential (notebook cell by cell), not truly concurrent or autonomous.

---

## 🛠️ Technologies & Frameworks

| Category | Tool / Library | Version |
|----------|---------------|---------|
| **LLM Inference** | [Groq API](https://groq.com) — `llama-3.1-8b-instant` | via openai-compatible API |
| **LLM Framework** | LangChain, langchain-openai | ≥ 0.2.0 |
| **PDF Extraction** | [Docling](https://github.com/DS4SD/docling) | latest |
| **Embeddings** | `sentence-transformers/all-MiniLM-L6-v2` | 384 dimensions |
| **Vector Store** | ChromaDB | local persistent |
| **Data Analysis** | pandas, numpy | ≥ 2.0, ≥ 1.24 |
| **Reporting** | ReportLab (PDF), HTML | ≥ 4.0.0 |
| **Notebooks** | Jupyter / JupyterLab | — |

---

## 📁 Project Structure

```
.
├── test.ipynb                          # Main notebook — Attijari Bank pipeline
│                                       # (PDF extraction, RAG, KPI extraction,
│                                       #  anomaly detection, reporting)
├── testin.ipynb                        # Second notebook — Inetum Tunisie pipeline
│                                       # (same pipeline, different document domain)
│
├── data/
│   ├── testrap.pdf                     # Attijari Bank Q1 2024 financial report
│   ├── testrap2.pdf                    # Attijari Bank additional document
│   ├── testrap3.pdf                    # Attijari Bank additional document
│   ├── testrap4.pdf                    # Inetum Tunisie report
│   └── bank_transactions_data_2.csv    # Sample banking transaction dataset
│
├── output/
│   ├── testrap_extracted.txt           # Text extracted from Attijari PDF
│   └── testinetum_extracted.txt        # Text extracted from Inetum PDF
│
├── requirements.txt                    # Python dependencies
├── .env.example                        # Environment variables template
└── .gitignore                          # Ignored files
```

> **Files not included in this repo:** `venv/`, `vectorstore_banking/`, `vectorstore_tech/` (ChromaDB local vector stores — regenerated on first run), large HTML reports.

---

## ✅ Real Results Obtained

### Attijari Bank Tunisie — Q1 2024

| Metric | Value | Found |
|--------|-------|-------|
| Produit Net Bancaire | 125,850,000 TND | ✅ |
| ROE Annualisé | 16.4% | ✅ |
| ROA Annualisé | 2.8% | ✅ |
| Coefficient d'exploitation | 52.6% | ✅ |
| Total Bilan | 8,750,000,000 TND | ✅ |
| Taux créances douteuses | 5.9% | ✅ |
| Ratio de solvabilité | 14.8% | ✅ |
| **KPI Success Rate** | **95.8%** (23/24 KPIs) | — |

**Anomalies detected (4):** Marge commerciale, Concentration deposits, Marge nette sur PNB (severity: HIGH), ROE Annualisé (severity: MODERATE). Note: some anomalies may reflect unit inconsistencies in the extraction.

### Inetum Tunisie — Q1 2024

| Metric | Value | Found |
|--------|-------|-------|
| Chiffre d'Affaires | 28,750,000 TND | ✅ |
| Croissance CA | 18.5% | ✅ |
| Marge Opérationnelle | 24.8% | ✅ |
| Effectif total | 1,450 collaborateurs | ✅ |
| **KPI Success Rate** | **78.3%** (47 KPIs extracted) | — |

---

## ⚙️ Prerequisites

- Python 3.8+
- A **Groq API key** (free tier available)
- `pip` and `venv`

> **Tesseract OCR** and **Poppler** may be required for `pytesseract` and `pdf2image` on some systems, but the primary PDF extraction uses Docling.

---

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/syrinemaalel1-web/Experimental-Project-First-Exploration-of-Multi-Agent-AI.git
cd Experimental-Project-First-Exploration-of-Multi-Agent-AI
```

### 2. Create and activate a virtual environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

> ⚠️ `torch` and `sentence-transformers` are large packages — first installation may take several minutes.

### 4. Configure environment variables

```bash
# Copy the template
copy .env.example .env       # Windows
cp .env.example .env         # macOS/Linux
```

Then edit `.env` and fill in your Groq API key:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🔑 API Keys

### GROQ_API_KEY

| | |
|---|---|
| **Variable name** | `GROQ_API_KEY` |
| **Role** | Provides access to the Groq LLM inference API, used by all LLM-based agents (KPI extraction, analysis, anomaly interpretation, report generation) |
| **Model used** | `llama-3.1-8b-instant` |
| **Where to get it** | [https://console.groq.com](https://console.groq.com) → Sign up (free) → API Keys → Create new secret key |
| **Where to place it** | In your local `.env` file: `GROQ_API_KEY=gsk_...` |
| **Cost** | Free tier available with generous rate limits |

---

## ▶️ Running the Project

The project is implemented in **Jupyter notebooks**. Launch Jupyter and open the notebooks:

```bash
# Make sure your virtual environment is activated
jupyter notebook
```

Then open:
- **`test.ipynb`** — Pipeline on Attijari Bank financial report
- **`testin.ipynb`** — Pipeline on Inetum Tunisie report

Run cells sequentially from top to bottom. Each notebook is self-contained and covers:
1. PDF text extraction (Docling)
2. Text chunking and embedding
3. ChromaDB vectorstore creation
4. RAG retrieval testing
5. KPI extraction (Agent 1)
6. Advanced KPI analysis (Agent 2)
7. Anomaly detection (Agent 3)
8. HTML/PDF report generation (Agent 4)

> **Important:** The vectorstores are created locally on first run. Ensure `GROQ_API_KEY` is set via environment variable before running any LLM-dependent cell.

---

## 📊 Example Usage

After running the pipeline in the notebook, you can interact with the agents directly:

```python
# Ask a specific question via RAG
ask_rag("Quel est le produit net bancaire au T1 2024?")
# → "Le produit net bancaire au T1 2024 est de 125 850 000 TND."

# Extract a specific KPI
kpi_extractor = create_kpi_extractor(retriever, llm)
result = kpi_extractor.extract_single_kpi("roe_annualise", show_details=True)
# → KPIResult(name='roe_annualise', value='16,4%', unit='%', period='T1 2024', confidence='high')

# Run full KPI extraction
report = kpi_extractor.extract_all_standard_kpis(show_progress=True)
# → Extracts 14 standard banking KPIs
```

---

## ⚠️ Limitations & Honest Assessment

### Technical Limitations
- **No real agent autonomy:** Agents are Python classes called sequentially in notebook cells — they do not communicate autonomously or handle failures adaptively
- **PDF encoding issues:** Docling sometimes produces malformed text (e.g., `´ etablissement` instead of `établissement`) which reduces retrieval quality for some queries
- **RAG retrieval inconsistency:** Duplicate chunks were observed in retrieval results; deduplication logic is basic
- **Anomaly detection calibrated for banking only:** The `testin.ipynb` anomaly agent uses banking sector benchmarks, which are inappropriate for the tech sector (Inetum)
- **No unit normalization:** Some extracted KPI values show unit inconsistencies (e.g., mixing TND, milliers TND, millions TND)
- **No error recovery:** If an LLM call fails, there is no retry or fallback logic

### Project-Level Limitations
- Code is in notebooks, not structured Python modules
- No unit tests
- No configuration management (hardcoded paths in cells)
- The pipeline is not reproducible in a single command — cells must be run manually
- `testin.ipynb` had connection errors during one session (visible in notebook output), indicating fragility against network issues

---

## 🚧 Experimental / Incomplete Parts

- **Agent coordination:** The "multi-agent" label is conceptual — no actual message-passing or agent orchestration framework (LangGraph, AutoGen, CrewAI, etc.) is used
- **Report Agent (Agent 4):** HTML reports were generated successfully; PDF generation via ReportLab was attempted but reliability varied
- **The `testin.ipynb` pipeline** encountered a connection error on its first cell and was rerun — results are from the second successful execution

---

## 🔮 Possible Improvements

- Refactor into proper Python modules (`.py` files) with a CLI entrypoint
- Add a real agent orchestration framework (LangGraph or CrewAI)
- Improve text extraction quality (handle encoding issues, better table parsing)
- Add domain-specific sector benchmarks per document type
- Add unit normalization for extracted KPI values
- Implement retry logic and error handling for LLM calls
- Add evaluation metrics to measure extraction accuracy against ground truth
- Build a simple Streamlit UI for non-technical users
- Add support for multi-period comparison (Q1 2023 vs Q1 2024 automatically)

---

## 🧰 Tech Stack Summary

```
LLM Backbone    : Groq API — llama-3.1-8b-instant
Framework       : LangChain (RAG + prompt templates + chains)
Embeddings      : HuggingFace sentence-transformers (all-MiniLM-L6-v2)
Vector Store    : ChromaDB (local, persistent)
PDF Parsing     : Docling
Data            : pandas, numpy
Reporting       : ReportLab (PDF), plain HTML
Interface       : Jupyter Notebooks
```

---

## 👩‍💻 Author

**Syrine Maalel**  
Personal experimental project — learning Multi-Agent AI by doing.

---

## 📄 License

This project is shared for educational and experimental purposes.
