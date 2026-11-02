"""命令行多轮聊天：演示上下文是怎么保留的。"""
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ["SILICONFLOW_API_KEY"],
    base_url="https://api.siliconflow.cn/v1",
)
MODEL = os.environ.get("MODEL", "Qwen/Qwen2.5-7B-Instruct")

messages = []

print("输入问题开始聊天；clear 清空历史；exit 退出。")

while True:
    user_input = input("\n你：").strip()

    if user_input == "":
        continue
    if user_input == "exit":
        break
    if user_input == "clear":
        messages = []
        print("（历史已清空）")
        continue

    messages.append({"role": "user", "content": user_input})

    resp = client.chat.completions.create(model=MODEL, messages=messages)
    answer = resp.choices[0].message.content

    messages.append({"role": "assistant", "content": answer})
    print(f"\nAI：{answer}")

print("再见。")
