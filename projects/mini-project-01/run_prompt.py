# run_prompt.py

# 1️⃣ 读取原始文本
with open("input.txt", "r", encoding="utf-8") as f:
    original_text = f.read()

# 2️⃣ 拼接进 Prompt 模板
prompt = f"""
背景：
下面是一段我的学习内容。

目标：
请生成一段不超过100字的摘要。

约束：
语言简洁，不引入新概念。

原始内容：
{original_text}
"""

# 3️⃣ 假设这是“AI输出”（今天先模拟）
ai_output = "（这里是AI生成的摘要示例）\n这是自动化流程的测试结果。"

# 4️⃣ 保存为 Markdown 文件
with open("output.md", "w", encoding="utf-8") as f:
    f.write("# AI 输出结果\n\n")
    f.write(ai_output)

print("运行完成，已生成 output.md")
