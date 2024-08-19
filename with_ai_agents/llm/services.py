import json

from .utils import prompts
from . import agents
from . import llms


class AIService:
    """AI 相关控制类"""

    @staticmethod
    def get_assistant_prompt():
        """获取 AI 默认人格提示词"""
        return prompts.get_kurisu_prompt()

    @staticmethod
    def get_question_class(llm: llms.LLM_TYPE, raw_question: str):
        """获取问题分类"""
        # 将用户提问发送到大模型分类器，获取分类列表
        prompt = prompts.get_classifier_prompt(question=raw_question)
        s = prompts.get_classifier_master_prompt()

        try:
            classifier_res = llm.ask_model(question=prompt, system_prompt=s)
            classifier_res = json.loads(classifier_res)
        except Exception as e:
            return False, str(e)

        return True, classifier_res

    @staticmethod
    def get_assistant_context(
            llm: llms.LLM_TYPE,
            classifier_res: list,
            raw_question: str,
            custom_soul: str = prompts.get_kurisu_prompt()
    ):
        """从 Agents 中获取 AI 的上下文"""
        agent_data = ""

        if len(classifier_res) == 1 and classifier_res[0] == 7:
            assemble_prompt = raw_question
        else:
            for num in classifier_res:
                if int(num) == 1:  # 提取页面内容
                    agent_data += agents.type1.get_agent_context(llm=llm, question=raw_question)
                    agent_data += "\n"
                elif int(num) == 2:  # 联网搜索能力
                    agent_data += agents.type2.get_agent_context(llm=llm, question=raw_question)
                    agent_data += "\n"
                elif int(num) == 3:  # 某地天气
                    pass
                elif int(num) == 4:  # 执行指令
                    pass
                elif int(num) == 5:  # who are you
                    agent_data += agents.type5.get_agent_context(prompt=custom_soul)
                    agent_data += "\n"
                elif int(num) == 6:  # 功能列表
                    agent_data += agents.type6.get_agent_context()
                    agent_data += "\n"
                elif int(num) == 8:  # 百科搜索能力
                    agent_data += agents.type8.get_agent_context(llm=llm, question=raw_question)

            assemble_prompt = prompts.get_assemble_prompt(question=raw_question, agent_data=agent_data)

        return assemble_prompt

    @staticmethod
    def ask_llm_with_agents(
            llm: llms.LLM_TYPE,
            classifier_res: list,
            raw_question,
            custom_soul: str = None,
            history: list = ()
    ):
        """携带 Agents 上下文向 LLM 提问"""
        try:
            # 获取上下文
            assemble_prompt = AIService.get_assistant_context(llm, classifier_res, raw_question)

            # 发送正式提问
            s = custom_soul
            if not s:
                s = AIService.get_assistant_prompt()

            assemble_res = llm.ask_model(
                question=assemble_prompt,
                system_prompt=s,
                message_history=history,
                temperature=0.3
            )
        except Exception as e:
            return False, str(e)

        return True, assemble_res
