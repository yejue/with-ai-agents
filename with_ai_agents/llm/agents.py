import re
import subprocess

from .utils import prompts, retrievers
from .llms import LLM_TYPE


class BaseType:
    """Agents 基类"""

    def get_agent_context(self, llm: LLM_TYPE, question: str):
        raise NotImplemented


class Type1(BaseType):
    """提取页面内容"""

    @staticmethod
    def extract_url_without_llm(question: str):
        """不使用 LLM 提取 URL 链接"""
        # 正则匹配 http 或 https 开头的 url
        # url_pattern = r'https?://[-\w.]+(?:[-\w/]|\.(?!\.))+'
        url_pattern = r'https?://[-\w.]+(?:[-\w/]|[-\w/?.&=%+])+'
        # 匹配第一个 URL
        match = re.search(url_pattern, question)
        return match.group(0) if match else None

    @staticmethod
    def extreact_url_with_llm(llm: LLM_TYPE, question: str):
        """大模型提取 URL"""
        prompt = prompts.get_type1_prompt(question=question)
        url = llm.ask_model(question=prompt)
        url = url.strip()
        return url

    @staticmethod
    def summarize_weblink_content(llm: LLM_TYPE, question: str):
        # 从问题中提取 URL
        url = Type1.extract_url_without_llm(question=question)
        if not url:
            return f"\"{url}\" 的大致内容是：内容提取失败"

        # 提取页面内容
        url_content = retrievers.get_url_content(url)
        url_content = url_content[:3000]
        result = f"\"{url}\" 的大致内容是：{url_content}"
        return result

    def get_agent_context(self, llm: LLM_TYPE, question: str):
        url = self.summarize_weblink_content(llm=llm, question=question)
        return url


class Type2(BaseType):
    """联网查询"""

    @staticmethod
    def get_search_result(llm: LLM_TYPE, question: str):
        prompt = prompts.get_type2_prompt(question=question)
        llm_res = llm.ask_model(question=prompt)
        search_result = retrievers.search_baidu(query=llm_res)
        result = f"\"{llm_res}\" 在搜索引擎的搜索结果是：{search_result}"
        return result

    def get_agent_context(self, llm: LLM_TYPE, question: str):
        return self.get_search_result(llm=llm, question=question)


class Type4(BaseType):
    """命令执行"""

    @staticmethod
    def command_execute(cmd):
        """命令执行"""
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout, result.stderr

    @staticmethod
    def get_command_result(llm: LLM_TYPE, question: str):
        prompt = prompts.get_type4_prompt(question)
        llm_res = llm.ask_model(question=prompt)

        llm_res = llm_res.strip()
        cmd_res = Type4.command_execute(llm_res)
        data = f"命令 {llm_res} 在当前服务器的执行结果是：{cmd_res}"
        return data

    def get_agent_context(self, llm: LLM_TYPE, question: str):
        return self.get_command_result(llm=llm, question=question)


class Type5(BaseType):
    """你是谁"""

    @staticmethod
    def get_who_you_are(**kwargs):
        prompt = kwargs.get("prompt", prompts.get_kurisu_prompt())
        text = f"关于你的信息：{prompt}"
        return text

    def get_agent_context(self, *args, **kwargs):
        return self.get_who_you_are(**kwargs)


class Type6(BaseType):
    """功能列表"""

    @staticmethod
    def get_ai_abilities():

        text = '''
        当前助手有的功能：
            - 总结网页内容。例子：提取这个页面的内容，www.baidu.com/
            - 天气预报。例子：今天北京的天气怎样
            - 命令执行。例子：执行这条语句，ls -la
            - 聊天。例子：最近有什么新闻？帮我写一个打印 hello world 的代码    
        '''

        return text

    def get_agent_context(self, *args, **kwargs):
        return self.get_ai_abilities()


class Type8(BaseType):
    """百科搜索能力"""

    def get_agent_context(self, llm: LLM_TYPE, question: str):
        prompt = prompts.get_type8_prompt(question=question)
        query = llm.ask_model(question=prompt)
        res = retrievers.search_baidu_wiki(query)
        res = res[:3000]
        return res


type1 = Type1()
type2 = Type2()
type4 = Type4()
type5 = Type5()
type6 = Type6()
type8 = Type8()
