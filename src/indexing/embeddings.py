from sentence_transformers import SentenceTransformer
from typing import List


class EmbeddingModel:
    """
    Wrapper around a sentence-transformer embedding model.
    """

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        """
        Convert list of texts into embeddings.
        """
        return self.model.encode(texts, convert_to_numpy=True).tolist()

    def embed_query(self, query: str) -> List[float]:
        """
        Convert a search query into an embedding.
        """
        return self.model.encode(query, convert_to_numpy=True).tolist()
