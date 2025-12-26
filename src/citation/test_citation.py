print(">>> test_citation.py STARTED <<<")

from src.citation.citation_extractor import extract_citations

print(">>> import worked <<<")

sample_references = """
[1] Jimmy Lei Ba, Jamie Ryan Kiros, and Geoffrey E. Hinton.
Layer Normalization. arXiv preprint arXiv:1607.06450, 2016.

[2] Dzmitry Bahdanau et al.
Neural Machine Translation by Jointly Learning to Align and Translate.
ICLR, 2015.
"""

citations = extract_citations(sample_references)

print(">>> Extracted citations <<<")
for c in citations:
    print("-", c)

print(">>> test_citation.py FINISHED <<<")
