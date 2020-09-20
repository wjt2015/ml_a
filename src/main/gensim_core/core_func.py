
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

def word_statistic(text_corpora):
    docs=[doc for doc in text_corpora]
    print("docs={}".format(docs))
    gensim.models.word2vec.Word2Vec


luosifu_desc="富兰克林·德拉诺·罗斯福（英语：Franklin Delano Roosevelt，1882年1月30日—1945年4月12日），简称为FDR，华人将其称为“小罗斯福”，是美国第32任总统，美国历史上首位连任四届（病逝于第四届任期中）的总统在1930年代经济大萧条期间，罗斯福 [1]  推行新政以提供失业救济与复苏经济，并成立众多机构来改革经济和银行体系，从经济危机的深渊中挽救了美国，他所发起的一些计划仍继续在国家的商贸中扮演重要角色。除此之外，在其任内设立的一些制度仍然保留至今。罗斯福曾促成了政党重组，他与其妻埃莉诺·罗斯福是美国现代自由主义的典范。罗斯福是第二次世界大战期间同盟国阵营的重要领导人之一。1941年珍珠港事件发生后，罗斯福力主对日本宣战，并引进了价格管制和配给。罗斯福以租借法案使美国转变为“民主国家的兵工厂”，使美国成为同盟国主要的军火供应商和融资者，也使得美国国内产业大幅扩张，实现充分就业。二战后期同盟国逐渐扭转形势后，罗斯福对塑造战后世界秩序发挥了关键作用，其影响力在雅尔塔会议及联合国的成立中尤其明显。后来，在美国协助下，盟军击败德国、意大利和日本。1945年4月12日，罗斯福在佐治亚州的温泉因突发脑溢血去世。罗斯福是美国迄今为止在任时间最长的美国总统，曾多次被评为美国最佳总统 [2]  ，被美国权威期刊《大西洋月刊》评为影响美国的100位人物第4名。"


