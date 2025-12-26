class SemanticSearchEngine:
    def __init__(self):
        from src.indexing.faiss_store import FAISSStore
        self.index, self.metadata = FAISSStore.load()

    def search(self, query, top_k=5):
        from src.indexing.embeddings import embed_text
        import numpy as np

        query_embedding = embed_text([query])
        query_embedding = np.array(query_embedding).astype("float32")

        # Get more candidates than needed
        distances, indices = self.index.search(query_embedding, top_k * 5)

        results = []
        for idx in indices[0]:
            if idx < len(self.metadata):
                results.append(self.metadata[idx])

        # 🔑 SECTION-AWARE FILTERING
        query_lower = query.lower()

        if "problem" in query_lower or "solve" in query_lower:
            preferred_sections = ["abstract", "introduction"]
        else:
            preferred_sections = None

        if preferred_sections:
            preferred = [r for r in results if r["section"] in preferred_sections]
            others = [r for r in results if r["section"] not in preferred_sections]
            results = preferred + others

        return results[:top_k]
class SemanticSearchEngine:
    def __init__(self):
        from src.indexing.faiss_store import FAISSStore
        self.index, self.metadata = FAISSStore.load()

    def search(self, query, top_k=5):
        from src.indexing.embeddings import embed_text
        import numpy as np

        query_embedding = embed_text([query])
        query_embedding = np.array(query_embedding).astype("float32")

        # Get more candidates than needed
        distances, indices = self.index.search(query_embedding, top_k * 5)

        results = []
        for idx in indices[0]:
            if idx < len(self.metadata):
                results.append(self.metadata[idx])

        # 🔑 SECTION-AWARE FILTERING
        query_lower = query.lower()

        if "problem" in query_lower or "solve" in query_lower:
            preferred_sections = ["abstract", "introduction"]
        else:
            preferred_sections = None

        if preferred_sections:
            preferred = [r for r in results if r["section"] in preferred_sections]
            others = [r for r in results if r["section"] not in preferred_sections]
            results = preferred + others

        return results[:top_k]
