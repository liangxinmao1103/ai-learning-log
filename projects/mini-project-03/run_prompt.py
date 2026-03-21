import os
import datetime

BASE_DIR = "projects/mini-project-03"
INPUT_DIR = os.path.join(BASE_DIR, "inputs")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
PROMPT_FILE = "prompts/summary.txt"

print(">>> 正在运行 mini-project-03 <<<")

def load_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def save_output(name, content):
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{name}_{ts}.md"
    path = os.path.join(OUTPUT_DIR, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write("# AI 总结\n\n")
        f.write(content)

    return path

def simulate_ai(prompt):
    return "【AI总结】\n" + prompt[:200]

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    template = load_file(PROMPT_FILE)

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