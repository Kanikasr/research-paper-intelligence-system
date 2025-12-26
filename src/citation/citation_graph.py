class CitationGraph:
    def __init__(self):
        # paper_id -> list of cited paper titles
        self.graph = {}

    def add_paper(self, paper_id, citations):
        self.graph[paper_id] = citations

    def get_citations(self, paper_id):
        return self.graph.get(paper_id, [])

    def get_full_graph(self):
        return self.graph
