import os
import datetime

BASE_DIR = "projects/mini-project-03"
INPUT_DIR = os.path.join(BASE_DIR, "inputs")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

PROMPT_MAP = {
    "1": "prompts/summary.txt",
    "2": "prompts/translate.txt",
    "3": "prompts/extract.txt"
}

def load_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def save_output(name, content):
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{name}_{ts}.md"
    path = os.path.join(OUTPUT_DIR, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write("# AI 输出结果\n\n")
        f.write(content)

    return path

def simulate_ai(prompt):
    return "【AI结果】\n" + prompt[:200]

def main():
    print("请选择功能：")
    print("1. 总结")
    print("2. 翻译")
    print("3. 提炼要点")

    choice = input("输入编号：")

    if choice not in PROMPT_MAP:
        print("无效选择")
        return

    prompt_file = PROMPT_MAP[choice]

    template = load_file(prompt_file)

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    files = os.listdir(INPUT_DIR)

    for file in files:
        if file.endswith(".txt"):
            input_path = os.path.join(INPUT_DIR, file)
            content = load_file(input_path)

            prompt = template.replace("{content}", content)

            result = simulate_ai(prompt)

            name = os.path.splitext(file)[0]
            out_path = save_output(name, result)

            print("已生成:", out_path)

if __name__ == "__main__":
    main()