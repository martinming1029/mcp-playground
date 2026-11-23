def read_file(path):
    f = open(path, "r", encoding="utf-8")
    content = f.read()
    f.close()
    return content


def write_file(path, content):
    f = open(path, "w", encoding="utf-8")
    f.write(content)
    f.close()
