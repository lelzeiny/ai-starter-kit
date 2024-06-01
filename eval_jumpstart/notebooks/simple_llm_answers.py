from typing import Dict, Any
from langchain.llms.base import BaseLLM
from langchain.prompts import PromptTemplate


class SimpleLLMAnswers:
    """Simple LLM answer generation without a vector DB"""

    def __init__(self, llm: BaseLLM):
        self.llm = llm
        self.prompt = PromptTemplate(
            template="Question: {question}\nAnswer:", input_variables=["question"]
        )

    def generate(self, query: str) -> Dict:
        """Generate an answer for the given query"""
        response = self.llm(self.prompt.format(question=query))
        print(response)
        return {"answer": response}
