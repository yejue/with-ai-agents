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

# 你的 history 应该类似于这样
# history = [
#    {"role": "user", "content": "内容"},
#    {"role": "assistant", "content": "内容"},
# ]

history = []

r = client.ask_central_brain(question, history=history)
print(r)
```

### History

#### 0.2.0
此版本为同步特性更新，主要同步内容如下：
 - GLM、OpenAI 类抽象
 - 百度百科搜索能力
 - 自定义 AI 人格
 - 新增了模型 API URL 的配置项
 - 联网搜索优化
 - 页面内容提取


### Valid Platforms, Models
可以支持以下三种平台的所有模型，实际上，凡是和下面三种平台一致的 history 输入格式都可以使用。可以通过 Client 的 `api_url` 参数来更改实际提供服务的接口地址。

| 平台（platform） | 模型（model_name）                                                                                                               | 相关文档                                                     |
|--------------|------------------------------------------------------------------------------------------------------------------------------| ------------------------------------------------------------ |
| openai       | gpt 全系列 | [openai](https://platform.openai.com/docs/models)            |
| dashscope    | 通意千问系列| [dashscope](https://help.aliyun.com/zh/dashscope/developer-reference/model-introduction?spm=a2c4g.11186623.0.i2) |
| glm          | 智普清言系列  | [glm](https://open.bigmodel.cn/dev/api#language)             |
