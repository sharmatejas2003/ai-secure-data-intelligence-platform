def parse_text(content: str):
    if not content:
        return []
    return content.splitlines()


# 🔥 NEW
def parse_by_type(input_type, content):
    if input_type == "text":
        return content.splitlines()

    elif input_type == "log":
        return content.splitlines()

    elif input_type == "sql":
        return content.split(";")

    elif input_type == "chat":
        return content.split("\n")

    else:
        return content.splitlines()