import faiss
import pickle
import numpy as np
from pathlib import Path

INDEX_PATH = Path("data/faiss.index")
META_PATH = Path("data/metadata.pkl")


class FAISSStore:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.metadata = []

    def add(self, embeddings, metadata):
        self.index.add(embeddings)
        self.metadata.extend(metadata)

    def save(self):
        faiss.write_index(self.index, str(INDEX_PATH))
        with open(META_PATH, "wb") as f:
            pickle.dump(self.metadata, f)

    @staticmethod
    def load():
        index = faiss.read_index(str(INDEX_PATH))
        with open(META_PATH, "rb") as f:
            metadata = pickle.load(f)
        return index, metadata

    def search(self, query_embedding, top_k=5):
        distances, indices = self.index.search(query_embedding, top_k)
        results = []
        for idx in indices[0]:
            if idx < len(self.metadata):
                results.append(self.metadata[idx])
        return results
