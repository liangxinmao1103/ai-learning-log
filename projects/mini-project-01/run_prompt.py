# run_prompt.py

# 1️⃣ 让用户输入文件名
filename = input("请输入要处理的文件名（例如 input.txt）： ")

# 2️⃣ 读取原始内容
with open(filename, "r", encoding="utf-8") as f:
    original_text = f.read()

# 3️⃣ 读取 Prompt 模板
with open("prompt_template.txt", "r", encoding="utf-8") as f:
    template = f.read()

# 4️⃣ 替换占位符
prompt = template.replace("{content}", original_text)

# 5️⃣ 模拟 AI 输出（以后会替换成真实 API）
ai_output = "这是自动化生成的测试结果。"

# 6️⃣ 输出文件名自动生成
output_file = "output_" + filename.replace(".txt", ".md")

with open(output_file, "w", encoding="utf-8") as f:
    f.write("# AI 输出结果\n\n")
    f.write(ai_output)

print("处理完成，生成文件：", output_file)