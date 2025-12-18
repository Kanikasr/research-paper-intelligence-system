from indexing.embeddings import EmbeddingModel
from indexing.faiss_store import FAISSVectorStore


class SemanticSearchEngine:
    """
    End-to-end semantic search engine:
    chunks → embeddings → FAISS → results
    """

    def __init__(self, embedding_dim: int = 384):
        self.embedder = EmbeddingModel()
        self.vector_store = FAISSVectorStore(embedding_dim)

    def index_chunks(self, chunks):
        """
        Index paper chunks into FAISS.
        """
        texts = [chunk["text"] for chunk in chunks]
        embeddings = self.embedder.embed_texts(texts)

        self.vector_store.add_embeddings(embeddings, chunks)

    def search(self, query: str, top_k: int = 5):
        """
        Perform semantic search over indexed chunks.
        """
        query_embedding = self.embedder.embed_query(query)
        return self.vector_store.search(query_embedding, top_k)
