# retrieval.py
import json
import os

class SimpleRetriever:
    def __init__(self, data_path='data/financial_faq.json'):
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"{data_path} not found.")
        with open(data_path, 'r') as f:
            self.knowledge_base = json.load(f)

    def retrieve(self, query):
        # Simple keyword match retrieval for demonstration
        query_lower = query.lower()
        relevant_facts = []
        for item in self.knowledge_base:
            if any(word in query_lower for word in item['question'].lower().split()):
                relevant_facts.append(item['answer'])
        if not relevant_facts:
            relevant_facts = ["No relevant information found in knowledge base."]
        return "\n".join(relevant_facts)
