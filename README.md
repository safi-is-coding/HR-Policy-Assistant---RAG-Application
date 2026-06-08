# 🏢 HR Policy Assistant - RAG Application

An intelligent HR Policy Assistant built using **LangChain**, **Mistral AI**, **ChromaDB**, and **Streamlit** that enables employees to query organizational HR policies using natural language.

The application leverages **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from HR policy documents and generate accurate, context-aware responses grounded in company documentation.

---

## 🚀 Features

* 📄 Multi-PDF HR policy ingestion
* 🔍 Semantic search using vector embeddings
* 🤖 AI-powered question answering with Mistral AI
* 🗂 ChromaDB vector database for efficient retrieval
* 💬 Interactive chat interface using Streamlit
* 📚 Context-aware responses based on uploaded policies
* ⚡ Fast retrieval using Maximum Marginal Relevance (MMR)
* 🔒 Reduces hallucinations by grounding answers in documents

---

## 🏗 Architecture

```text
HR Policy PDFs
       │
       ▼
Document Loader
       │
       ▼
Text Chunking
       │
       ▼
Mistral Embeddings
       │
       ▼
ChromaDB Vector Store
       │
       ▼
Retriever (MMR)
       │
       ▼
Mistral LLM
       │
       ▼
Streamlit Chat Interface
```

---

## 🛠 Tech Stack

### Frontend

* Streamlit

### Backend

* Python
* LangChain

### LLM

* Mistral AI

### Vector Database

* ChromaDB

### Embeddings

* Mistral Embeddings

### Document Processing

* PyPDFLoader
* RecursiveCharacterTextSplitter

---

## 📂 Project Structure

```text
HR-RAG/
│
├── data/
│
├── vector_db/
│
├── ingest.py
├── rag_chain.py
├── app.py
├── .env
├── pyproject.toml
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/hr-rag.git
cd hr-rag
```

### Create Virtual Environment

Using UV:

```bash
uv venv
```

Activate Environment:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
uv sync
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
MISTRAL_API_KEY=your_api_key_here
```

---

## 📥 Add HR Policy Documents

Place all HR policy PDF files inside the `data/` directory.

Example:

```text
data/
├── Employee_Handbook.pdf
├── Leave_Policy.pdf
├── Insurance_Policy.pdf
├── Travel_Policy.pdf
└── Work_From_Home_Policy.pdf
```

---

## 🗄 Create Vector Database

Run the ingestion pipeline:

```bash
python ingest.py
```

This process:

1. Loads PDF documents
2. Splits documents into chunks
3. Generates embeddings
4. Stores embeddings in ChromaDB

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```
---

## 🔄 RAG Workflow

### Document Processing

* Load PDFs
* Extract text
* Split into chunks

### Embedding Generation

* Convert chunks into vector embeddings using Mistral Embeddings

### Vector Storage

* Store embeddings in ChromaDB

### Retrieval

* Retrieve top relevant chunks using MMR retrieval

### Generation

* Pass retrieved context to Mistral LLM
* Generate grounded responses

---

## 📊 Current Limitations

* No source citation display
* No conversational memory
* No user authentication
* No document upload interface
* Single organization knowledge base

---

## 🚀 Future Enhancements

* Source citations with page numbers
* Conversational memory
* Hybrid Search (BM25 + Vector Search)
* Reranking
* Role-Based Access Control
* HR Admin Dashboard
* PDF Upload Interface
* Feedback Collection System
* Docker Deployment
* Cloud Deployment (AWS / Azure / GCP)

---

## 🎯 Learning Outcomes

This project demonstrates:

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Semantic Search
* Prompt Engineering
* LLM Integration
* Document Intelligence
* Streamlit Application Development

---

## 👨‍💻 Author

**Mohammad Safi Maz**


GitHub: https://github.com/safi-is-coding
LinkedIn: Add your LinkedIn profile link

---
