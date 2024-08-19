from pydantic import Field
from .llm import llms
from .llm.services import AIService


class Client:

    def __init__(
            self, api_key: str = None,
            api_url: str = None,
            platform: str = "dashscope",
            model_name: str = "qwen-turbo"
    ):
        self.api_key: str = api_key
        self.api_url: str = api_url
        self.platform: str = platform
        self.model_name: str = model_name

    def _get_llm(self):
        platform_map = {
            "dashscope": llms.DashscopeModel,
            "glm": llms.GLMModel,
            "openai": llms.OpenAIModel,
        }

        platform = platform_map.get(self.platform, None)
        if not platform:
            return None

        llm = platform(api_key=self.api_key)

        if self.model_name:
            llm.model = self.model_name

        if self.api_url:
            llm.api_url = self.api_url

        return llm

    def ask_central_brain(self, raw_question: str, history: list = (), custom_soul: str = None):
        llm = self._get_llm()
        if not llm:
            return "WITH_AI_AGENTS 大模型获取失败，请检查配置。配置文档参考：https://github.com/yejue/nonebot-plugin-with-ai-agents"

        # 获取分类信息
        status, classifier_res = AIService.get_question_class(llm=llm, raw_question=raw_question)
        if not status:
            return f"分类失败, {classifier_res}"

        # 获取最终回答
        status, assemble_res = AIService.ask_llm_with_agents(
            llm=llm,
            classifier_res=classifier_res,
            raw_question=raw_question,
            history=history,
            custom_soul=custom_soul
        )

        if not status:
            return f"最终结果获取失败，{assemble_res}"

        return assemble_res

    def ask_simple_brain(self, raw_question: str, history: list = (), custom_soul: str = None):
        llm = self._get_llm()
        res = llm.ask_model(
            question=raw_question,
            system_prompt=custom_soul,
            message_history=history,
            temperature=0.3
        )
        return res
