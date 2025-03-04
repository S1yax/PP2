import os, string, re

def list_items(path):
    items = os.listdir(path)
    return {
        "folders": [f for f in items if os.path.isdir(os.path.join(path, f))],
        "files": [f for f in items if os.path.isfile(os.path.join(path, f))],
        "all": items
    }

def extract_numbers(text):
    return re.findall(r"\+7705\d{7}", text)

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as file:
        file.write(f"This is file {letter}.txt")