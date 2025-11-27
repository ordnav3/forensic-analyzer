import os
import hashlib
from datetime import datetime
import mimetypes

def file_hash_sha256(path, block_size=65536):
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(block_size), b""):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return None

def extract_metadata(path):
    try:
        st = os.stat(path)
        mime, _ = mimetypes.guess_type(path)
        return {
            "path": path,
            "size_bytes": st.st_size,
            "created": datetime.fromtimestamp(st.st_ctime).isoformat(),
            "modified": datetime.fromtimestamp(st.st_mtime).isoformat(),
            "mode": oct(st.st_mode),
            "mime": mime or "unknown",
            "sha256": file_hash_sha256(path)
        }
    except Exception as e:
        return {"path": path, "error": str(e)}
