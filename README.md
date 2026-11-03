# llm-journey

2026.11 开始，记录我学大模型应用开发的过程。

## Day 1：环境 + 第一次调用 API

目标：让电脑能写 Python，并成功调用一次大模型。

### 已完成
- [x] 装好 Python
- [x] 装好 VS Code
- [x] 装好 Git
- [x] 注册 GitHub
- [x] 注册硅基流动，拿到 API Key
- [x] 跑通 `hello.py`
- [x] 跑通 `first_call.py`
- [x] 推到 GitHub

## Day 2：多轮对话

- [x] 跑通 `chat_cli.py`
- [x] 验证上下文记忆
- [x] 理解 messages 列表就是「记忆」

学到：模型本身不记事，每次请求都把历史一起发过去。

## Day 3：流式输出与错误处理

- [x] 用 stream=True 实现打字机效果
- [x] try/except 捕获错误，断网不崩
- [x] system 提示词设定人设

学到：flush=True 才会立刻输出；失败的请求要 pop 掉，别污染历史。