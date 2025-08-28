from openai import OpenAI
import os
from dotenv import load_dotenv

# 加载.env文件中的环境变量
load_dotenv()

def call_llm(messages):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key == "your_actual_api_key_here":
        raise ValueError("请在.env文件中设置有效的OPENAI_API_KEY")
    
    # 获取BASE_URL和MODEL，如果没有设置则使用默认值
    base_url = os.getenv("BASE_URL", "https://api.openai.com/v1")
    model = os.getenv("MODEL", "gpt-4o")
    
    client = OpenAI(
        api_key=api_key,
        base_url=base_url
    )
    
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    # Test the LLM call
    messages = [{"role": "user", "content": "In a few words, what's the meaning of life?"}]
    response = call_llm(messages)
    print(f"Prompt: {messages[0]['content']}")
    print(f"Response: {response}")

