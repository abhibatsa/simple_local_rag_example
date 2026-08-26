# Simple Local RAG Pipeline

A lightweight, 100% private, and local Retrieval-Augmented Generation (RAG) pipeline 
built using Python, LangChain, ChromaDB, and Ollama. 

This project runs fully offline on consumer hardware, 
making it ideal for systems with resource constraints like an 8GB M1 Mac.

⭐ **If you found this starter template helpful, please consider giving it a star! It helps others discover the project.**

---

## 🛠️ What is a RAG Pipeline?

**Retrieval-Augmented Generation (RAG)** is an architectural pattern that optimizes the output of a Large Language Model (LLM). 
Instead of relying strictly on what the model learned during its initial training, 
a RAG pipeline queries an external authoritative knowledge base (like a database, PDFs, or private company files) 
to find relevant facts matching a user's prompt. 
It then passes those facts directly into the LLM as context to generate an accurate, updated answer.

![Simple RAG Pipeline Diagram](/assets/rag-pipeline.png)


### The 2 Core Phases of RAG:
1. **Data Ingestion (The Retrieval):** Documents are broken down into chunks,
   converted into mathematical vector representations (embeddings), and stored inside a Vector Database.
   When a user asks a question, the database acts like a search engine to retrieve the closest matching document text chunks.
3. **Synthesis (The Generation):** The retrieved chunks are glued together with the user's original question
   into a specialized prompt template and handed over to the LLM to generate a natural response.

---

## 💡 Why Build a RAG Pipeline & What Problem It Solves

### 1. Eliminates AI Hallucinations
Standard LLMs confidently invent false information when they do not know an answer. 
RAG solves this by binding the LLM's workspace strictly to the data provided in its prompt context.

### 2. Connects Private & Dynamic Data
Commercial foundation models do not know your private business files, personal notes, or real-time data changes. 
RAG securely bridges your local data to an AI without needing to spend thousands of dollars retraining or fine-tuning models.

### 3. Absolute Privacy & Zero Cost
Because this pipeline uses Ollama to host models locally, your private documents never leave your physical computer. 
No cloud APIs, no data tracking, and no subscriptions.

---

## 🚀 Getting Started

### Prerequisites

1. **Install Ollama**  
   Download and install the desktop app from [Ollama's Official Website](https://ollama.com).

2. **Pull the Low-Resource Models**  
   Open your terminal and download the required lightweight models optimized for 8GB systems:
   ```bash
   ollama pull llama3.2:1b
   ollama pull nomic-embed-text
   ```

### Installation & Environment Setup

Follow these steps to clone the project, isolate dependencies inside a Python virtual environment (`venv`), and install packages.

1. **Clone the repository**
   ```bash
   git clone https://github.com
   cd YOUR_REPO_NAME
   ```

2. **Create a Python virtual environment**  
   This keeps project dependencies isolated from your global system environment:
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**  
   * **macOS / Linux:**
     ```bash
     source venv/bin/activate
     ```
   * **Windows (Command Prompt):**
     ```cmd
     venv\Scripts\activate.bat
     ```
   * **Windows (PowerShell):**
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   *(Once activated, you will see `(venv)` prepended to your terminal prompt).*

4. **Install required packages**  
   Ensure you install the modern, non-deprecated standalone integration libraries:
   ```bash
   pip install --upgrade pip
   pip install langchain-ollama langchain-chroma
   ```

### Running the Project

Make sure the Ollama application is active and running in your Mac system background, 
then launch the interactive script:

```bash
python3 rag_pipeline.py
```

### Example Usage:
* **Input:** `Who authorized Project Quantum-X?`
* **Output:** `Project Quantum-X was authorized by Director Sarah Jenkins in 2024.`

---

## 🔒 Keeping it Clean (`.gitignore`)

To ensure you don't accidentally push your local database cache or environment dependencies to GitHub, 
create a file named `.gitignore` in your root folder and add the following lines:

```text
# Python virtual environment
venv/
.venv/
__pycache__/
*.pyc

# Local Vector Database storage files
.chroma/
chroma_db/
```

---

## 🚀 What's Ahead? (Future Roadmaps to Build & Fork)

This repository is built as a minimal foundation. If you want to expand your knowledge, fork this repo and try implementing these next steps:

* [ ] **Persistent Storage:** Modify ChromaDB settings to save the vector files to your local disk instead of resetting the memory database every time the script exits.
* [ ] **PDF Document Loader:** Replace the hardcoded list with a text document or PDF file parsing pipeline using `PyPDFLoader` or `DirectoryLoader`.
* [ ] **Text Chunk Splitter:** Add `RecursiveCharacterTextSplitter` to handle massive user documents by cutting long files into clean overlapping text windows.
* [ ] **Add a Graphical Interface:** Wrap this python script with a lightweight, browser-based web application layout using `Streamlit` or `Gradio`.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information. Anyone is free to use, modify, and distribute this codebase.
