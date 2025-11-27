import io
import chardet

def try_read_text(path):
    try:
        with open(path, "rb") as f:
            raw = f.read()
        enc = chardet.detect(raw)['encoding'] or 'utf-8'
        return raw.decode(enc, errors="ignore")
    except Exception:
        return None

def scan_keywords(path, keywords):
    text = try_read_text(path)
    if not text:
        return []
    found = []
    low = text.lower()
    for kw in keywords:
        if kw.lower() in low:
            found.append(kw)
    return found
