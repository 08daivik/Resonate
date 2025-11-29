---

# **Resonate AI**

A simple Audio + Document RAG system that allows you to upload **audio (MP3/WAV/MP4 etc.)**, **PDF**, and **PPTX** files, extract the text, and then **ask questions** or **generate summaries** using a RAG (Retrieval-Augmented Generation) pipeline.

---

## 🚀 **Features**

* Upload audio or documents
* Speech-to-text transcription using AssemblyAI
* PDF/PPT text extraction
* Text chunking + embeddings (Gemini)
* FAISS vector search for retrieval
* Ask questions about uploaded content
* Auto summary generation
* Modern UI (HTML/CSS/JS)

---

## 📁 **Project Structure**

```
Resonate-AI/
│
├── backend/
│   ├── main.py          # FastAPI app
│   ├── processor.py     # Audio/PDF/PPT extraction
│   ├── embeddings.py    # Chunking + embeddings
│   ├── rag.py           # FAISS vector DB
│   ├── utils.py         # Gemini helper
│
├── ui/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│
├── requirements.txt
└── README.md
```

---

## 🔧 **How to Run the Project**

### **1️⃣ Install Python packages**

```
pip install -r requirements.txt
```

---

### **2️⃣ Start the FastAPI Backend**

Run this inside the project folder:

```
uvicorn backend.main:app --reload
```

Backend runs on:

```
http://127.0.0.1:8000
```

---

### **3️⃣ Start the Frontend**

If using Live Server / Node / Vite:

```
cd ui
```

Run using either:

* VS Code Live Server
* `npx live-server`
* OR simply open `index.html` in your browser

UI will run on:

```
http://localhost:5500/
```

(or your live-server port)

---

## 🔑 **API Keys Required**

Create a `.env` file or put them directly in `main.py`:

```
ASSEMBLYAI_KEY=your_key_here
GEMINI_KEY=your_key_here
```

---

## 📝 **Supported File Types**

* Audio: `.mp3`, `.wav`, `.m4a`, `.flac`, `.aac`, `.ogg`, `.wma`, `.webm`, `.mp4`, `.mka`
* Documents: `.pdf`, `.pptx`

---

## ✔️ **You're Ready to Go**

Upload a file → ask questions → generate summaries.

---


Just tell me!
