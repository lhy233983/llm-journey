"""命令行多轮聊天：流式输出 + 错误处理。"""
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ["SILICONFLOW_API_KEY"],
    base_url="https://api.siliconflow.cn/v1",
    timeout=30,
    max_retries=1,
)
MODEL = os.environ.get("MODEL", "Qwen/Qwen2.5-7B-Instruct")

SYSTEM = {
    "role": "system",
    "content": "你是一个耐心的编程助教，回答简洁，多用例子，不说废话。",
}

messages = [SYSTEM]

print("输入问题开始聊天；clear 清空历史；exit 退出。")

while True:
    user_input = input("\n你：").strip()

    if user_input == "":
        continue
    if user_input == "exit":
        break
    if user_input == "clear":
        messages = [SYSTEM]
        print("（历史已清空）")
        continue

    messages.append({"role": "user", "content": user_input})

    print("\nAI：", end="")
    answer = ""
    try:
        stream = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            stream=True,
        )
        for chunk in stream:
            if not chunk.choices:
                continue
            delta = chunk.choices[0].delta.content
            if delta:
                answer += delta
                print(delta, end="", flush=True)
    except Exception as e:
        print(f"\n[出错了] {e}")
        messages.pop()
        continue

    print()
    messages.append({"role": "assistant", "content": answer})

print("再见。")