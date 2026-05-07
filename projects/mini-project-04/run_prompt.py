import os
import datetime
import argparse

BASE_DIR = "projects/mini-project-03"
INPUT_DIR = os.path.join(BASE_DIR, "inputs")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

PROMPT_MAP = {
    "summary": "prompts/summary.txt",
    "translate": "prompts/translate.txt",
    "extract": "prompts/extract.txt"
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
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", required=True, help="summary / translate / extract")
    parser.add_argument("--file", help="指定单个文件（可选）")

    args = parser.parse_args()

    if args.mode not in PROMPT_MAP:
        print("无效 mode")
        return

    prompt_file = PROMPT_MAP[args.mode]
    template = load_file(prompt_file)

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # 单文件 or 批量
    if args.file:
        files = [args.file]
    else:
        files = os.listdir(INPUT_DIR)

    for file in files:
        if not file.endswith(".txt"):
            continue

        input_path = os.path.join(INPUT_DIR, file)
        content = load_file(input_path)

        prompt = template.replace("{content}", content)
        result = simulate_ai(prompt)

        name = os.path.splitext(file)[0]
        out_path = save_output(name, result)

        print("已生成:", out_path)

if __name__ == "__main__":
    main()
