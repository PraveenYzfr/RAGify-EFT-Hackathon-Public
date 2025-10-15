import json
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

def add_jsonl_to_chromadb(jsonl_path, collection_name="RAGify_Collection", persist_directory="chromadb_local"):
    # Initialize ChromaDB client with local persistence
    client = chromadb.PersistentClient(path="./chromadb_data")
    collection = client.get_or_create_collection(collection_name)

    # Initialize embedding model (can be changed)
    embedder = SentenceTransformer('all-MiniLM-L6-v2')

    # Read JSONL and add to ChromaDB with embeddings
    with open(jsonl_path, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            data = json.loads(line)
            text = data.get("contents")
            if text:
                # Chroma will use its default embedding function unless you specify one
                collection.add(
                    documents=[text],                    
                    embeddings=[embedder.encode(text).tolist()],
                    ids=[str(idx)]
                )
    # Persist the data to disk
    #client.persist()
    print(f"Added data from {jsonl_path} to ChromaDB collection '{collection_name}' (local storage: {persist_directory}).")

def generate_reply(user_query):
    
    client = chromadb.PersistentClient(path="./chromadb_data")
    collection = client.get_or_create_collection("RAGify_Collection")

    # Initialize embedding model (can be changed)
    embedder = SentenceTransformer('all-MiniLM-L6-v2')
    query_emb = embedder.encode([user_query]).tolist()
    results = collection.query(query_embeddings=query_emb, n_results=2)
    context = "\n".join(results["documents"][0]) if results["documents"] else ""
    return context