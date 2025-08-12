# app.py
import os
import openai
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from config import OPENAI_API_KEY
from prompts import get_finance_prompt
from retrieval import SimpleRetriever
from voice_handler.py import VoiceHandler

def main():
    # Setup OpenAI API key
    openai.api_key = OPENAI_API_KEY

    # Initialize components
    retriever = SimpleRetriever()
    prompt_template = get_finance_prompt()
    llm = OpenAI(temperature=0)
    chain = LLMChain(llm=llm, prompt=prompt_template)
    voice = VoiceHandler()

    voice.speak("Hello! I am your finance assistant. Ask me any finance-related question.")

    while True:
        user_question = voice.listen()
        if not user_question:
            continue
        if user_question.lower() in ["exit", "quit", "stop"]:
            voice.speak("Goodbye!")
            break

        # Retrieve knowledge context
        context = retriever.retrieve(user_question)

        # Generate answer
        answer = chain.run(context=context, question=user_question)

        # Speak answer
        voice.speak(answer)

if __name__ == "__main__":
    main()
