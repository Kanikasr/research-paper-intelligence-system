import faiss
import numpy as np
from typing import List, Dict


class FAISSVectorStore:
    """
    FAISS-based vector store for semantic search.
    """

    def __init__(self, embedding_dim: int):
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.metadata = []

    def add_embeddings(self, embeddings: List[List[float]], metadatas: List[Dict]):
        vectors = np.array(embeddings).astype("float32")
        self.index.add(vectors)
        self.metadata.extend(metadatas)

    def search(self, query_embedding: List[float], top_k: int = 5):
        query_vector = np.array([query_embedding]).astype("float32")
        distances, indices = self.index.search(query_vector, top_k)

        results = []
        for idx in indices[0]:
            results.append(self.metadata[idx])

        return results
