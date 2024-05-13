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
import asyncio
import with_ai_agents

with_ai_agents.platform = "<Your platform, example: 'dashscope' or 'gpt'>"
with_ai_agents.api_key = "<Your platform api_key, example: 'sk-xxxxxxxx'>"

text = """
https://arxiv.org/abs/2405.05818
The main theme of this article revolves around 
whether it delves into concrete solutions pertaining to vector search.
"""
res = asyncio.run(with_ai_agents.handler.ask_central_brain(text))
print(res)
```
4. Run. `python main.py`


## Usage


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



## Environment (Or called config)
|      配置项       | 必填 |  默认值  |                             说明                             |
| :---------------: | :--: | :------: | :----------------------------------------------------------: |
|   WITH_AI_AGENTS__API_KEY    |  是  | 空字符串 |                         你的大模型 API Key                          |
| WITH_AI_AGENTS_PLATFORM |  是  | 空字符串 | 你的 AI 模型平台，支持 ChatGPT 系列，ChatGLM 系列，Llama 系列，百川，通义千问 |
| WITH_AI_AGENTS__TAVILY_API_KEY |  否  | 空字符串 | 搜索引擎的 Key，不填使用百度搜索，获取地址：[Tavily AI](https://app.tavily.com/sign-in) |
|  WITH_AI_AGENTS__MODEL_NAME   |  否  | 空字符串 |        你的 AI 模型名称，不填将根据平台使用默认模型        |
