# Research Paper Management & Analysis Intelligence System

## Project Overview
This project implements an AI-powered research intelligence backend that ingests academic research papers and enables semantic discovery across long-form technical documents. The system is designed to help researchers efficiently explore, organize, and retrieve relevant information from research papers using modern embedding models and vector similarity search.

The project reflects real-world research assistant platforms used by universities, research labs, and R&D organizations.

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

---

## Features Implemented (Part I & Part II)

### Part I: Paper Ingestion & Representation
- Programmatic PDF loading and raw text extraction
- Section-level parsing (Abstract, Model, References, etc.)
- Metadata extraction including title, authors, and publication year
- Unified internal schema for structured research paper representation

### Part II: Knowledge Indexing & Semantic Search
- Section-aware and token-length-based text chunking
- Sentence-transformer-based dense embeddings
- FAISS-backed vector database for efficient similarity search
- Natural language semantic search across indexed paper sections

---

## Tech Stack
- Python 3.11
- PyPDF for PDF text extraction
- Sentence-Transformers for embeddings
- FAISS for vector similarity search
- LangChain (foundation-ready for future extensions)
- Git and GitHub for version control

---

## Setup Instructions

### Clone the repository
```bash
git clone https://github.com/<your-username>/research-paper-intelligence-system.git
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

### Add research papers
## Place research paper PDFs inside:
data/raw_papers/


### Running Semantic Search
python src/search/test_semantic_search.py

## Example query:
attention mechanism in transformers

## Project Status and Future Work

### Completed
- Research paper ingestion and structured representation
- Semantic indexing and similarity-based search

### Planned Enhancements
- LLM-based paper summarization
- Retrieval-Augmented Generation (RAG) question answering
- Cross-paper comparison and analysis
- Citation graph construction
- Research trend and topic analysis
- Streamlit-based researcher-facing user interface

---
