# run_prompt.py
import os
import datetime
import json

def load_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def save_output(folder, basename, content):
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = f"{basename}_{ts}.md"
    out_path = os.path.join(folder, fname)
    with open(out_path, "w", encoding="utf-8") as fo:
        fo.write("# AI 输出结果\n\n")
        fo.write(content)
    return out_path

def call_ai_simulation(prompt_text):
    # 模拟模式：把 prompt 的关键信息摘出作为示例输出
    summary = "（模拟）自动化生成的摘要：\n"
    lines = prompt_text.strip().splitlines()
    sample = " ".join(lines[:3])
    return summary + sample[:300]

def call_openai_api(prompt_text):
    # 可选真实调用（需要安装 openai 并设置 OPENAI_API_KEY）
    try:
        import openai
    except ImportError:
        raise RuntimeError("openai 库未安装。pip install openai")
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("未设置 OPENAI_API_KEY 环境变量")
    openai.api_key = key
    # 这里示范使用 ChatCompletion（可能随官方变化，请以官方文档为准）
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user", "content": prompt_text}],
        max_tokens=300,
        temperature=0.2,
    )
    return resp.choices[0].message.content.strip()

def main():
    # 1) 选择输入文件
    inp = input("要处理的文本文件（相对路径，例如 projects/mini-project-01/input.txt）： ").strip()
    if not inp:
        print("未输入文件名，退出")
        return
    if not os.path.exists(inp):
        print("文件不存在：", inp)
        return

    # 2) 选择 prompt 模板文件
    tmpl = input("prompt 模板文件（例如 prompts/prompt_template.txt，回车使用默认 prompt_template.txt）: ").strip()
    if not tmpl:
        tmpl = "prompt_template.txt"
    if not os.path.exists(tmpl):
        print("模板文件不存在，使用内置默认模板")
        template_text = "背景：\n下面是一段内容。\n目标：请生成一段不超过100字的摘要。\n原始内容：\n{content}"
    else:
        template_text = load_file(tmpl)

    # 3) 读取并替换
    original_text = load_file(inp)
    prompt_text = template_text.replace("{content}", original_text)

    # 4) 决定使用真实 API 还是模拟
    if os.getenv("OPENAI_API_KEY"):
        try:
            ai_output = call_openai_api(prompt_text)
        except Exception as e:
            print("调用 API 出错，回退到模拟模式：", e)
            ai_output = call_ai_simulation(prompt_text)
    else:
        ai_output = call_ai_simulation(prompt_text)

    # 5) 保存输出（自动命名）
    out_folder = os.path.join("projects", "mini-project-01", "outputs")
    os.makedirs(out_folder, exist_ok=True)
    base = os.path.splitext(os.path.basename(inp))[0]
    out_path = save_output(out_folder, base, ai_output)
    print("处理完成，生成文件：", out_path)

if __name__ == "__main__":
    main()