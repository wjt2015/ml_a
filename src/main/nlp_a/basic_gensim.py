
import gensim


text_corpus = [
    "Human machine interface for lab abc computer applications",
    "A survey of user opinion of computer system response time",
    "The EPS user interface management system",
    "System and human system engineering testing of EPS",
    "Relation of user perceived response time to error measurement",
    "The generation of random binary unordered trees",
    "The intersection graph of paths in trees",
    "Graph minors IV Widths of trees and well quasi ordering",
    "Graph minors A survey",
]


stop_words=set("for a an of the and to in out".split(" "))
"""
统计词汇;
"""
def word_count():
    texts=[[word for word in document.lower().split()] for document in text_corpus]

    print("texts={}".format(texts))


