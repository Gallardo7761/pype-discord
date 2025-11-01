import json

def read(file: str) -> str:
    with open(file, "r") as f:
        return f.read()
    
def read_json(file: str) -> dict:
    with open(file, "r") as f:
        return json.load(f)

def write(file: str, content: str) -> None:
    with open(file, "w") as f:
        f.write(content)

def write_json(file: str, content: dict) -> None:
    with open(file, "w") as f:
        json.dump(content, f, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)