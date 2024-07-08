import importlib
from ragflow.graph.component.begin import Begin, BeginParam
from ragflow.graph.component.generate import Generate, GenerateParam
from ragflow.graph.component.retrieval import Retrieval, RetrievalParam
from ragflow.graph.component.answer import Answer, AnswerParam
from ragflow.graph.component.categorize import Categorize, CategorizeParam
from ragflow.graph.component.switch import Switch, SwitchParam
from ragflow.graph.component.relevant import Relevant, RelevantParam
from ragflow.graph.component.message import Message, MessageParam
from ragflow.graph.component.rewrite import RewriteQuestion, RewriteQuestionParam
from ragflow.graph.component.keyword import KeywordExtract, KeywordExtractParam
from ragflow.graph.component.baidu import Baidu, BaiduParam
from ragflow.graph.component.duckduckgosearch import DuckDuckGoSearch, DuckDuckGoSearchParam


def component_class(class_name):
    m = importlib.import_module("graph.component")
    c = getattr(m, class_name)
    return c
