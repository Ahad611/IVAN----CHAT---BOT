def read_file(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"Read error: {e}"
