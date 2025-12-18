from indexing.embeddings import EmbeddingModel

if __name__ == "__main__":
    model = EmbeddingModel()

    texts = [
        "Transformer models are based on attention",
        "Recurrent neural networks use recurrence",
        "Pizza is my favorite food"
    ]

    embeddings = model.embed_texts(texts)

    print("Embedding vector length:", len(embeddings[0]))
