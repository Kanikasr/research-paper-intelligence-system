# Research Paper Management & Analysis Intelligence System

## Project Overview
This project implements an AI-powered research intelligence system that ingests academic research papers and enables semantic discovery, question answering, citation analysis, and trend analysis across long-form technical documents.

The system is designed to help researchers efficiently explore, organize, and retrieve relevant information from research papers using embeddings, vector similarity search, and Retrieval-Augmented Generation (RAG).

This project mirrors real-world research assistant platforms used by universities, research labs, and R&D organizations.

---

## System Architecture
The implemented system follows the pipeline below:

PDF Ingestion  
→ Section-Level Parsing  
→ Metadata Extraction  
→ Intelligent Chunking  
→ Text Embeddings  
→ FAISS Vector Store  
→ Semantic Search  
→ RAG Question Answering  
→ Citation Analysis  
→ Research Trend Analysis  
→ Streamlit UI  

---

## Features Implemented

### Part I: Paper Ingestion & Representation
- Programmatic PDF loading and raw text extraction
- Section-level parsing (Abstract, Model, References, etc.)
- Metadata extraction (title, authors, publication year)
- Unified internal schema for structured research paper representation

### Part II: Knowledge Indexing & Semantic Search
- Section-aware and token-length-based text chunking
- Sentence-transformer-based dense embeddings
- FAISS-backed vector database for similarity search
- Natural language semantic search across indexed paper sections

### Part III: RAG-Based Question Answering
- Context retrieval using FAISS
- Prompt-grounded answer generation using open-source LLMs
- Answers constrained strictly to retrieved paper context

### Part IV: Citation Analysis
- Reference section parsing
- Heuristic citation extraction
- Citation graph construction

### Part V: Research Trend Analysis
- Keyword aggregation by publication year
- Frequency-based trend identification across papers

### Part VI: Streamlit Research Assistant UI
- Interactive question answering interface
- Display of retrieved context chunks
- Citation and trend visualization panels

---

## Tech Stack
- Python 3.11
- PyPDF
- Sentence-Transformers
- FAISS
- LangChain
- HuggingFace Transformers
- Streamlit
- Git & GitHub

---

## Setup Instructions

### Clone the repository
```bash
git clone https://github.com/Kanikasr/research-paper-intelligence-system.git

cd research-paper-intelligence-system

```
---

### Create virtual environment and install dependencies
```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate

pip install -r requirements.txt

```

---

## Data
This system expects users to provide their own PDFs in `data/raw_papers/`.
Due to copyright restrictions, papers are not included in the repository.



### Run ingestion pipeline
python -m src.ingestion.run_ingestion

### Run Streamlit application
```bash
streamlit run src/app.py
```
Open in browser:
http://localhost:8501

### Running Semantic Search
python src/search/test_semantic_search.py

## Example Query & Output

**Question:**  
What problem does the Transformer model solve?

**Retrieved Sections:**  
- *Attention Is All You Need* — Abstract, Model  
- *BERT: Pre-training of Deep Bidirectional Transformers* — Abstract  

**RAG Answer:**  
> The Transformer model addresses the limitations of recurrent and convolutional sequence models by eliminating sequential computation and using attention mechanisms to model global dependencies, enabling efficient parallel processing of sequences.

**Citation Extraction (Example):**  
- Layer Normalization. arXiv:1607.06450

**Research Trend Analysis (Keyword Frequency):**  
- **2014:** attention, transformer, translation  
- **2018:** pretraining, bidirectional, language model  

---

## Known Limitations
- Citation extraction is heuristic-based and may miss references due to PDF formatting
- Trend analysis improves as more papers are added
- Open-source LLMs are used; answer quality depends on context length limits
- Focus is on research intelligence workflows rather than production deployment

---

## Project Status
**Completed**
- PDF ingestion and structured representation
- Semantic indexing and similarity search
- RAG-based question answering
- Citation extraction and graph construction
- Research trend analysis
- Streamlit-based research assistant UI


## Future Enhancements

  - Advanced citation graph visualization
  - Cross-paper comparative analysis
  - Multi-document summarization
  - External metadata enrichment (arXiv / Semantic Scholar APIs)

