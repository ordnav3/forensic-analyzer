#!/usr/bin/env python3
# main.py
import argparse
from modules.file_reader import walk_directory
from modules.metadata_extractor import extract_metadata
from modules.keyword_scanner import scan_keywords
from modules.report_generator import generate_report
import os

DEFAULT_KEYWORDS = ["senha", "login", "confidencial", "senha123", "transfer", "fraude", "DELETE"]

def analyze(path, keywords, output_dir):
    entries = []
    for filepath in walk_directory(path):
        meta = extract_metadata(filepath)
        hits = scan_keywords(filepath, keywords)
        meta['keywords'] = hits
        entries.append(meta)
    os.makedirs(output_dir, exist_ok=True)
    report_path = os.path.join(output_dir, "relatorio_forense.html")
    generate_report(entries, report_path, path)
    print(f"Relatório gerado: {report_path}")

def parse_args():
    parser = argparse.ArgumentParser(description="Forensic Analyzer - triagem inicial")
    parser.add_argument("path", help="Caminho da pasta a ser analisada")
    parser.add_argument("--keywords", nargs="*", default=DEFAULT_KEYWORDS, help="Lista de palavras-chave")
    parser.add_argument("--output", default="output", help="Pasta de saída")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    analyze(args.path, args.keywords, args.output)
