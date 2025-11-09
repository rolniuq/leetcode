import sys
import random
import subprocess
import os

DIR_PATH = "~/Workplace/leetcode/scripts/"

LIST_FILE = os.path.expanduser(DIR_PATH + "leetcode-75.txt")
SOLVED_FILE = os.path.expanduser(DIR_PATH + "solved-75.txt")
LANG = "python"
EDITOR_CMD = "nv"
MODE = "next"

with open(LIST_FILE, "r") as f:
    all_ids = [line.strip() for line in f if line.strip()]

solved_set = set()
if os.path.exists(SOLVED_FILE):
    with open(SOLVED_FILE, "r") as f:
        solved_set = {line.strip() for line in f if line.strip()}

pending_ids = [id_ for id_ in all_ids if id_ not in solved_set]

if not pending_ids:
    print("🎉 Hoàn thành 75 bài rồi! Nghỉ ngơi đi.")
    sys.exit(0)

if MODE == "next":
    today_id = pending_ids[0]
elif MODE == "random":
    today_id = random.choice(pending_ids)
else:
    print("MODE sai: dùng 'next' hoặc 'random'")
    sys.exit(1)

print(f"📚 Bài hôm nay: {today_id} (Còn {len(pending_ids)} bài nữa)")

try:
    subprocess.run(["leetcode", "show", today_id, "-g", f"-l{LANG}"], check=True)
    print(f"✅ Generated: {today_id}.{LANG}")

    file_path = f"{today_id}.{LANG}"
    if os.path.exists(file_path):
        subprocess.run([EDITOR_CMD, file_path])

    choice = input("Solved chưa? (y/n): ")
    if choice.lower() == "y":
        with open(SOLVED_FILE, "a") as f:
            f.write(today_id + "\n")
        print("📝 Đã mark solved!")

except subprocess.CalledProcessError:
    print("❌ Lỗi CLI: Kiểm tra login và cài đặt.")
except FileNotFoundError:
    print("❌ Chưa cài leetcode CLI hoặc editor.")
