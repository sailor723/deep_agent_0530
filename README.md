# 从零构建 Deep Agents

这个仓库是一个用于学习的 LangGraph / LangChain 教程项目，目标是帮助你从零理解并实现更复杂的智能体模式。

它更偏向训练与演示用途，主要学习内容放在 `notebooks/` 中，同时在 `src/` 下提供了一套简洁的参考实现。

## 项目概览

这个仓库重点围绕三种实用的智能体模式展开：

1. 使用 TODO 列表进行任务规划
2. 使用内存中的虚拟文件系统进行上下文卸载
3. 使用子智能体委托实现上下文隔离

整体内容采用循序渐进的方式组织，方便你从基础模型调用一路学习到更完整的研究型智能体构建过程。

## 环境要求

- Python 3.11 及以上
- 使用 [uv](https://docs.astral.sh/uv/) 进行依赖管理

## 安装 uv

如果你的本机还没有安装 `uv`，可以先使用以下任一方式安装：

```bash
# macOS / Linux 官方安装脚本
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```bash
# macOS 也可以使用 Homebrew
brew install uv
```

Windows 用户建议优先使用 PowerShell 官方安装方式：

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

如果你使用的是 Windows `cmd`，也可以直接执行下面的命令调用 PowerShell 安装：

```bat
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

如果你使用 Windows 包管理器，也可以参考 `uv` 官方安装文档中的 `winget` 方式。

如果你更习惯 Linux 命令行，也可以在 Windows 上使用 WSL。

WSL 快速安装与打开方式：

```powershell
# 以管理员身份打开 PowerShell 后执行
wsl --install
```

安装完成并重启后，可以用以下任一方式打开 WSL：

```powershell
wsl
```

```powershell
ubuntu
```

进入 WSL 后，可以按 Linux 方式安装 `uv`：

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

安装完成后，可以用下面的命令确认是否安装成功：

```bash
uv --version
```

`uv` 官方文档：

- 安装说明: <https://docs.astral.sh/uv/getting-started/installation/>
- 使用说明: <https://docs.astral.sh/uv/>

## 快速开始

1. 克隆仓库：

```bash
git clone git@github.com:sailor723/deep_agent_0530.git
cd deep_agent_0530
```

如果团队成员本机没有安装 Git，也可以通过微信或其他聊天工具直接分享项目压缩包：

```text
deep_agent_0530.zip
```

推荐分享方式：

1. 在项目根目录将仓库压缩为 `deep_agent_0530.zip`
2. 通过微信发送压缩包给团队成员
3. 团队成员下载后解压到本地目录
4. 进入项目目录后继续执行下面的安装步骤

注意事项：

- 建议不要把 `.venv`、`.git`、`__pycache__`、`node_modules` 等本地缓存或版本控制目录打进压缩包
- 通过微信分享时，优先发送压缩包，不要直接逐个发送源码文件
- 团队成员收到后，目录名保持为 `deep_agent_0530` 即可
- `.env` 中的私密 API Key 不建议直接放进分享包，建议让每位同学自己配置

2. 安装依赖：

```bash
uv sync
```

如果你在中国大陆网络环境下安装较慢，可以临时使用 PyPI 镜像加速 `uv sync`。

推荐镜像：

- 清华镜像: `https://pypi.tuna.tsinghua.edu.cn/simple`
- 阿里云镜像: `https://mirrors.aliyun.com/pypi/simple`

临时使用示例：

```bash
UV_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple uv sync
```

如果你使用的是 Windows PowerShell：

```powershell
$env:UV_INDEX_URL="https://pypi.tuna.tsinghua.edu.cn/simple"
uv sync
```

如果你使用的是 Windows CMD：

```bat
set UV_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple
uv sync
```

说明：

- 这里建议只对 Python 包下载使用镜像
- GitHub 仓库地址、API 平台地址、登录页面、密钥管理页面仍建议使用官方地址
- 如果镜像源异常，可直接去掉 `UV_INDEX_URL` 后重试官方源

常用 `uv` 用法示例：

```bash
# 安装并同步当前项目依赖
uv sync

# 在项目环境中运行 Python 脚本
uv run python check_model.py

# 启动 Jupyter Notebook
uv run jupyter notebook

# 启动 JupyterLab
uv run jupyter lab
```

3. 创建本地环境变量文件：

```bash
cp example.env .env
```

4. 在 `.env` 中填写你需要的 API Key。

如果要运行网页搜索相关笔记本或研究工具，至少需要：

```env
TAVILY_API_KEY=your_tavily_api_key_here
```

获取 Tavily API Key：

- 平台主页: <https://app.tavily.com/>
- 快速开始文档: <https://docs.tavily.com/documentation/quickstart>

根据你实际运行的笔记本或脚本不同，可能还需要填写一个或多个模型提供方的密钥，例如：

```env
DEEPSEEK_API_KEY=your_deepseek_api_key_here
MINIMAX_API_KEY=your_minimax_api_key_here
```

获取模型 API Key：

- DeepSeek 平台: <https://platform.deepseek.com/>
- DeepSeek 文档: <https://api-docs.deepseek.com/quick_start>
- MiniMax 平台: <https://platform.minimax.io/login>
- MiniMax 文档: <https://platform.minimax.io/docs/guides/quickstart-preparation>

仓库中的部分本地实验脚本还默认依赖兼容 Ollama 的本地接口。

5. 启动 Jupyter：

```bash
# 打开 Jupyter Notebook
uv run jupyter notebook

# 打开 JupyterLab
uv run jupyter lab
```

## 学习路径

项目中的笔记本分为两个模块。

### 模块一：LLM 与智能体基础

这一部分用于介绍后续智能体示例中会用到的核心构件。

| 笔记本 | 内容 |
| --- | --- |
| `1.1_foundational_models.ipynb` | 模型初始化与基础聊天模型调用 |
| `1.1_prompting.ipynb` | Prompt 基础与提示词设计 |
| `1.2_tools.ipynb` | 工具定义与工具调用 |
| `1.2_web_search.ipynb` | 网页搜索能力接入 |
| `1.3_memory.ipynb` | Memory 与状态管理 |
| `1.4_multimodal_messages.ipynb` | 多模态消息处理模式 |
| `1.5_personal_chef.ipynb` | 一个简单的端到端助手示例 |

### 模块二：深度智能体模式

这一部分聚焦于更复杂智能体中常见的高阶模式。

| 笔记本 | 内容 |
| --- | --- |
| `2.0_create_agent.ipynb` | 使用 `create_agent` 构建基础 agent 循环 |
| `2.1_todo.ipynb` | 使用 TODO 进行规划与进度跟踪 |
| `2.2_files.ipynb` | 使用虚拟文件工具进行上下文卸载 |
| `2.3_subagents.ipynb` | 通过子智能体委托实现上下文隔离 |
| `2.4_full_agent.ipynb` | 将这些模式组合成更完整的 agent |

## 源码包说明

可复用的 Python 代码位于 `src/deep_agents_from_scratch/`。

| 文件 | 作用 |
| --- | --- |
| `state.py` | 定义 `DeepAgentState`、TODO 结构以及文件状态合并逻辑 |
| `todo_tools.py` | 读写任务列表的工具 |
| `file_tools.py` | 虚拟文件的列出、读取与写入工具 |
| `task_tool.py` | 带上下文隔离的子智能体委托工具 |
| `research_tools.py` | Tavily 搜索、网页读取与结果摘要工具 |
| `prompts.py` | 共享提示词与工具描述模板 |

## 项目结构

```text
deep_agent_0530/
├── notebooks/
│   ├── module-1/
│   │   ├── resources/
│   │   ├── 1.1_foundational_models.ipynb
│   │   ├── 1.1_prompting.ipynb
│   │   ├── 1.2_tools.ipynb
│   │   ├── 1.2_web_search.ipynb
│   │   ├── 1.3_memory.ipynb
│   │   ├── 1.4_multimodal_messages.ipynb
│   │   ├── 1.5_personal_chef.ipynb
│   │   └── langgraph.json
│   └── module-2/
│       ├── resources/
│       ├── 2.0_create_agent.ipynb
│       ├── 2.1_todo.ipynb
│       ├── 2.2_files.ipynb
│       ├── 2.3_subagents.ipynb
│       ├── 2.4_full_agent.ipynb
│       └── utils.py
├── src/
│   └── deep_agents_from_scratch/
│       ├── __init__.py
│       ├── file_tools.py
│       ├── prompts.py
│       ├── research_tools.py
│       ├── state.py
│       ├── task_tool.py
│       └── todo_tools.py
├── example.env
├── pyproject.toml
└── README.md
```

## 说明

- 这是一个学习型仓库，推荐优先从笔记本开始阅读和运行。
- 项目实现有意保持轻量，目标是帮助理解模式，而不是提供完整的生产级框架。
- 当前仓库中没有正式配置自动化测试套件。
- 一些辅助脚本仅用于环境检查或本地实验。

## 推荐学习方式

1. 按顺序完成模块一
2. 再按顺序完成模块二
3. 每看完一个笔记本，再对照阅读 `src/` 中对应源码
4. 完成环境配置后，再尝试运行辅助脚本
