from src.trends.trend_analyzer import TrendAnalyzer

ta = TrendAnalyzer()

ta.add_paper(2014, [("attention", 3), ("translation", 2)])
ta.add_paper(2014, [("attention", 1), ("model", 2)])
ta.add_paper(2023, [("llm", 3), ("retrieval", 2)])

print("Detected trends:")
print(ta.get_trends())
