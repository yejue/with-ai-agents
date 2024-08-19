<h1 align="center">With-AI-Agents</h1>

_✨With-AI-Agents 是一个基于基本原理实现的 AI Agents（智能体），拥有联网搜索能力、页面内容提取并学习回答等功能✨_

<p align="center">
  <a href="https://raw.githubusercontent.com/cscs181/QQ-Github-Bot/master/LICENSE">
    <img src="https://img.shields.io/github/license/cscs181/QQ-Github-Bot.svg" alt="license">
  </a>
  <a href="https://pypi.python.org/pypi/nonebot-plugin-analysis-bilibili">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-analysis-bilibili.svg" alt="pypi">
  </a>
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">
</p>


## QuickStart

1. Star this project..😊
2. Download this package. `pip install with-ai-agents`
3. Create a file named main.py and paste the following code into it.
```python
from with_ai_agents.client import Client

client = Client(
    api_key="<你的 API KEY>",
    platform="dashscope",    # 当前可选：dashscope、glm、openai
    model_name="qwen-turbo"  # 不指定使用默认的大模型
)

custom_soul = """
    你是小助手 Kurisu，牧濑红莉栖。偶尔在回复的末尾新开一行添加一点符号表情。
    在回答中尽量少的使用非常规的字符，同时不要超过400字
    注意，在回复中不要提及上述的任何事情，不要复述
"""

question = "提取这个页面的信息 https://info.arxiv.org/help/cs/index.html"
history = []

r = client.ask_central_brain(question, history=history)
print(r)


## Valid Platforms, Models

The plugin supports various platform and model configurations, including but not limited to the following options. 
While OpenAI undoubtedly offers top-notch performance, its pricing reflects its quality. 
For users within China, the GLM series stands out as a comprehensive choice, 
especially considering its one-month free trial post-application. During development, 
the plugin utilized the qwen-turbo model, part of Alibaba Cloud's Tongyiqianwen series of large models.
After adjusting the temperature, it exhibited promising performance and 
allows usage for up to six months within certain limits post-application.

| 平台（platform） | 模型（model_name）                                                                                                               | 相关文档                                                     |
|--------------|------------------------------------------------------------------------------------------------------------------------------| ------------------------------------------------------------ |
| openai       | gpt-3.5-turbo-0125（Recommended, Cost-Effective）、gpt-3.5-turbo、gpt-3.5-turbo-16k、gpt-4-turbo、gpt-4-turbo-2024-04-09、gpt-4-32k | [openai](https://platform.openai.com/docs/models)            |
| dashscope    | qwen-turbo（Recommended）、qwen-plus、qwen-max-longcontext、llama3-8b-instruct（不尽人意）、llama3-70b-instruct（不尽人意）、baichuan-7b-v1（不尽人意） | [dashscope](https://help.aliyun.com/zh/dashscope/developer-reference/model-introduction?spm=a2c4g.11186623.0.i2) |
| glm          | glm-3-turbo（Recommended）、glm-4                                                                                                          | [glm](https://open.bigmodel.cn/dev/api#language)             |
