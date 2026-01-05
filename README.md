# ESILV Smart Assistant 🤖🎓

The **ESILV Smart Assistant** is an intelligent multi-agent chatbot designed for the ESILV engineering school.  
It provides reliable answers to questions about programs, admissions, and courses using official ESILV documentation, and supports student registration with role-based access control.

This project was developed as part of the **LLM & Generative AI** course.

---

## 🚀 Features

- Retrieval-Augmented Generation (RAG) using ESILV internal documents
- Multi-agent architecture (retrieval, orchestration, form agents)
- Accurate, document-grounded answers (no hallucinations)
- Student registration and contact collection
- Role-based authentication (admin / student)
- Admin dashboard to visualize registrations
- Local inference using open-source LLMs (Ollama)
- Streamlit-based web interface

---

## 🧠 System Architecture

The system follows a **modular multi-agent architecture**:

- **Retrieval Agent**
  - Answers factual questions using ESILV documents
  - Uses ChromaDB for vector search and Ollama for generation

- **Form Agent**
  - Collects structured user information (name, email, program interest)
  - Stores data locally for demonstration purposes

- **Orchestration Agent**
  - Routes user queries to the appropriate agent based on intent

- **Admin Logic**
  - Restricts access to sensitive data (registrations)
  - Implements role-based access control

---

## 🏗️ High-Level Architecture

```
User
 ↓
Streamlit Interface
 ↓
Orchestration Agent
 ├── Retrieval Agent (RAG + ChromaDB + Ollama)
 ├── Form Agent (Registration)
 └── Admin Access Control
```

---

## 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/esilv-smart-assistant.git
cd esilv-smart-assistant
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Install Ollama and pull the model
```bash
ollama pull tinyllama
```

### 4. Ingest ESILV documents
```bash
python rag/ingest.py
```

### 5. Run the application
```bash
streamlit run app.py
```

---

## 🔐 Demo Credentials

For demonstration purposes, authentication is hardcoded:

### Admin
- Username: `admin`
- Password: `admin123`

### Student
- Username: `student`
- Password: `student123`

Only admins can access the registration dashboard.

---

## 📁 Project Structure

```
esilv-smart-assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── agents/
│   ├── retrieval_agent.py
│   ├── form_agent.py
│   └── orchestrator.py
│
├── rag/
│   └── ingest.py
│
├── data/
│   └── esilv.txt
```

---

## 📚 Technologies Used

- **Python**
- **Streamlit**
- **LangChain**
- **ChromaDB**
- **Ollama (TinyLlama)**
- **Pandas**

All tools are open-source or academic-friendly.

---

## ⚠️ Notes

- The vector database (`rag/db`) is generated locally and not included in the repository.
- Registration data (`contacts.csv`) is excluded for privacy reasons.
- UTF-8 encoding is enforced to ensure correct handling of French characters.

---

## 🎓 Course Context

This project was developed for the **Final Project – LLM and Generative AI** course at ESILV.  
It demonstrates best practices in:
- Retrieval-Augmented Generation
- Multi-agent coordination
- Responsible use of Large Language Models
- Reproducible AI systems

---

## 📌 License

This project is intended for academic use only.
