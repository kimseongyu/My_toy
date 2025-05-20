import os


# 세미콜론 변환
def replace_semicolon_in_file(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    # ; → ; 변환
    new_content = content.replace(";", ";")
    with open(file_path, "w", encoding="utf-8", errors="ignore") as f:
        f.write(new_content)


# 폴더 내 파일 탐색 및 처리
for root, dirs, files in os.walk("."):
    for file in files:
        if not file.endswith((".c", ".cpp")):
            continue 
        file_path = os.path.join(root, file)
        replace_semicolon_in_file(file_path)
        print(f"Updated: {file_path}")

