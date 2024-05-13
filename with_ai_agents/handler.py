from .llm import central_brain
from .llm.services import ChatService


async def ask_central_brain(question: str):
    """向 Agents 提问"""
    res = await central_brain.ask_central_brain(raw_question=question)
    return res


async def ask_simple_llm(question: str):
    """向一般 LLM 提问"""
    res = await central_brain.ask_simple_llm(raw_question=question)
    return res
