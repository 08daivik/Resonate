from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import os

from backend.processor import transcribe_audio, extract_pdf, extract_ppt
from backend.embeddings import chunk_text, get_embeddings
from backend.rag import build_faiss, retrieve
from backend.utils import init_gemini, get_gemini_model


# -------------------------------
# SETUP FASTAPI
# -------------------------------
app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=['http://localhost:5500', 'http://localhost:3000'])
ASSEMBLYAI_KEY = "add here"
GEMINI_KEY = "add here"

init_gemini(GEMINI_KEY)


# -------------------------------
# FILE UPLOAD ENDPOINT
# -------------------------------
@app.post("/upload")
async def upload_file(file: UploadFile):

    os.makedirs("uploads", exist_ok=True)
    path = f"uploads/{file.filename}"

    with open(path, "wb") as f:
        f.write(await file.read())

    # ------------------------------
    # DETECT FILE TYPE
    # ------------------------------
    if file.filename.lower().endswith((
    ".mp3", ".wav", ".m4a", ".flac", ".aac",
    ".ogg", ".wma", ".webm", ".mp4", ".mka"
    )):
        text = transcribe_audio(path, ASSEMBLYAI_KEY)

    elif file.filename.lower().endswith(".pdf"):
        text = extract_pdf(path)

    elif file.filename.lower().endswith(".pptx"):
        text = extract_ppt(path)

    else:
        return {"error": "Unsupported file format"}

    # ------------------------------
    # CHUNK + EMBEDDINGS
    # ------------------------------
    chunks = chunk_text(text)
    vectors = get_embeddings(chunks)

    # ------------------------------
    # BUILD VECTOR DB
    # ------------------------------
    build_faiss(vectors, chunks)

    return {
        "message": "File processed successfully",
        "text_length": len(text),
        "chunks": len(chunks)
    }


# -------------------------------
# Q&A ENDPOINT
# -------------------------------
@app.get("/ask")
async def ask_question(query: str):

    query_vec = get_embeddings([query])[0]
    retrieved_chunks = retrieve(query_vec)

    context = "\n".join(retrieved_chunks)
    model = get_gemini_model()

    prompt = f"""
You are an AI assistant performing RAG.

Use ONLY the context below to answer.

Context:
{context}

Question: {query}

Give a clear answer.
"""

    response = model.generate_content(prompt)

    return {"answer": response.text}


# -------------------------------
# SUMMARY ENDPOINT
# -------------------------------
@app.get("/summary")
async def summarize():
    from backend.rag import stored_chunks   # ⬅ IMPORTANT CHANGE

    if not stored_chunks:
        return {"error": "No data available. Upload a file first."}

    context = "\n".join(stored_chunks)
    model = get_gemini_model()

    prompt = f"""
Summarize the following document/audio:

{context}

Provide a short and clean summary.
"""

    response = model.generate_content(prompt)

    return {"summary": response.text}

