import os

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace


class LLMFactory():
    
    def get_llm():
        llm = HuggingFaceEndpoint(repo_id=os.getenv("HF_MODEL"), task='text-generation')
        return ChatHuggingFace(llm=llm)