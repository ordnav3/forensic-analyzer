# modules/report_generator.py
import html
from datetime import datetime

def generate_report(entries, out_path, analyzed_root):
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("<html><head><meta charset='utf-8'><title>Relatório Forense</title></head><body>")
        f.write(f"<h1>Relatório Forense - Triagem Inicial</h1>")
        f.write(f"<p>Raiz analisada: {html.escape(analyzed_root)}</p>")
        f.write(f"<p>Data do relatório: {datetime.now().isoformat()}</p>")
        f.write("<table border='1' cellpadding='5' cellspacing='0'>")
        f.write("<tr><th>Arquivo</th><th>Tamanho (bytes)</th><th>Modificado</th><th>Mime</th><th>SHA256</th><th>Palavras-chave</th></tr>")
        for e in entries:
            path = html.escape(e.get("path",""))
            size = e.get("size_bytes","-")
            mod = e.get("modified","-")
            mime = e.get("mime","-")
            sha = e.get("sha256","-")
            kws = ", ".join(e.get("keywords", [])) or "-"
            f.write(f"<tr><td>{path}</td><td>{size}</td><td>{mod}</td><td>{mime}</td><td style='font-family:monospace'>{sha}</td><td>{html.escape(kws)}</td></tr>")
        f.write("</table></body></html>")