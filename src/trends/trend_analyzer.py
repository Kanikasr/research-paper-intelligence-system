from collections import defaultdict, Counter

class TrendAnalyzer:
    def __init__(self):
        # year -> list of keywords
        self.yearly_keywords = defaultdict(list)

    def add_paper(self, year, keywords):
        if not year:
            return
        for keyword, count in keywords:
            self.yearly_keywords[year].extend([keyword] * count)

    def get_trends(self, top_k=10):
        trends = {}
        for year, keywords in self.yearly_keywords.items():
            trends[year] = Counter(keywords).most_common(top_k)
        return trends
