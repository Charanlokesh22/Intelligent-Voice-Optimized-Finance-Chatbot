# prompts.py
from langchain.prompts import PromptTemplate

finance_prompt_template = """
You are a helpful financial assistant. Use the retrieved financial knowledge to answer the user's question accurately.
Knowledge: {context}

User question: {question}

Answer:
"""

def get_finance_prompt():
    return PromptTemplate(
        input_variables=["context", "question"],
        template=finance_prompt_template
    )
