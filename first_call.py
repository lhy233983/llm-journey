"""第一次调用大模型 API。

运行前：把 .env 里的 SILICONFLOW_API_KEY 换成你自己的 key。
"""
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ["SILICONFLOW_API_KEY"],
    base_url="https://api.siliconflow.cn/v1",
)

resp = client.chat.completions.create(
    model=os.environ.get("MODEL", "Qwen/Qwen2.5-7B-Instruct"),
    messages=[{"role": "user", "content": "用一句话解释什么是 RAG"}],
)

print(resp.choices[0].message.content)

