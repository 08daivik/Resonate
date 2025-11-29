from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

# -------------------------------
# CHUNKING
# -------------------------------
def chunk_text(text: str, max_len: int = 500):
    sentences = text.split(".")
    chunks = []
    current = ""

    for sent in sentences:
        sent = sent.strip()
        if not sent:
            continue

        if len(current) + len(sent) < max_len:
            current += sent + ". "
        else:
            chunks.append(current.strip())
            current = sent + ". "

    if current:
        chunks.append(current.strip())

    return chunks


# -------------------------------
# EMBEDDING GENERATION
# -------------------------------
def get_embeddings(text_list):
    return model.encode(text_list)
