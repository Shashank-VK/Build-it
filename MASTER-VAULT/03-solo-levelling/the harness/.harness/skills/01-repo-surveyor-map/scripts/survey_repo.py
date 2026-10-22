#!/usr/bin/env python3
"""Deterministic Repo Surveyor & Architectural Mapping Tool (CAP-18 & CAP-08)."""
import argparse
import json
import os
import sys
from typing import Dict, List

EXCLUDED_DIRS = {
    '.git', '.github', 'node_modules', '__pycache__', '.pytest_cache',
    '.venv', 'venv', 'target', 'dist', 'build', '.next', '.turbo', '.coverage',
    '.gemini', '.idea', '.vscode'
}

MANIFEST_MAP = {
    'package.json': 'JavaScript / TypeScript (Node.js / npm)',
    'pnpm-workspace.yaml': 'TypeScript / JavaScript Monorepo (pnpm)',
    'pyproject.toml': 'Python (Modern PEP 518 / Poetry / Flit / Rye)',
    'requirements.txt': 'Python (pip)',
    'Cargo.toml': 'Rust (Cargo)',
    'go.mod': 'Go (Go Modules)',
    'pom.xml': 'Java (Maven)',
    'build.gradle': 'Java / Kotlin (Gradle)',
    'Dockerfile': 'Containerized Infrastructure',
    'Taskfile.yml': 'Taskfile Automation Runner',
    'Makefile': 'Make Automation Runner',
    'AGENTS.md': 'AI Development Harness Root'
}

def detect_manifests(root_dir: str) -> Dict[str, str]:
    detected = {}
    for filename, description in MANIFEST_MAP.items():
        filepath = os.path.join(root_dir, filename)
        if os.path.exists(filepath):
            detected[filename] = description
    return detected

def build_bounded_tree(root_dir: str, max_depth: int = 3) -> List[str]:
    lines = []
    def _traverse(current_dir: str, depth: int):
        if depth > max_depth:
            return
        try:
            entries = sorted(os.listdir(current_dir))
        except PermissionError:
            return
        
        dirs = []
        files = []
        for e in entries:
            if e in EXCLUDED_DIRS or e.startswith('.'):
                continue
            full = os.path.join(current_dir, e)
            if os.path.isdir(full):
                dirs.append(e)
            else:
                files.append(e)

        for d in dirs:
            indent = '  ' * depth
            lines.append(f'{indent}- 📁 {d}/')
            _traverse(os.path.join(current_dir, d), depth + 1)
        for f in files:
            indent = '  ' * depth
            lines.append(f'{indent}- 📄 {f}')

    _traverse(root_dir, 0)
    return lines

def scan_entrypoints(root_dir: str) -> List[str]:
    common_entrypoints = [
        'src/index.ts', 'src/main.ts', 'src/main.py', 'app.py', 'main.py',
        'server.js', 'src/server.ts', 'src/App.tsx', 'src/app/layout.tsx',
        'src/main.rs', 'cmd/main.go', 'bin/run', 'cli.py', 'Taskfile.yml', 'AGENTS.md'
    ]
    found = []
    for ep in common_entrypoints:
        if os.path.exists(os.path.join(root_dir, ep)):
            found.append(ep)
    return found

def generate_report(root_dir: str) -> str:
    manifests = detect_manifests(root_dir)
    tree_lines = build_bounded_tree(root_dir, max_depth=2)
    entrypoints = scan_entrypoints(root_dir)
    
    report = []
    report.append(f'# Repository Architectural Map: {os.path.basename(os.path.abspath(root_dir))}')
    report.append('')
    report.append('## 1. Detected Manifests & Stack')
    if manifests:
        for m, desc in manifests.items():
            report.append(f'- **{m}**: {desc}')
    else:
        report.append('- *No standard root manifests detected.*')
    report.append('')
    report.append('## 2. Bounded Directory Structure (Max Depth 2)')
    report.append('```text')
    report.extend(tree_lines[:40])
    if len(tree_lines) > 40:
        report.append(f'... [{len(tree_lines) - 40} additional items truncated]')
    report.append('```')
    report.append('')
    report.append('## 3. Identified Entrypoints & Control Surfaces')
    if entrypoints:
        for ep in entrypoints:
            report.append(f'- `[ENTRYPOINT]` `{ep}`')
    else:
        report.append('- *No standard entrypoints detected.*')
    report.append('')
    report.append('## 4. Architectural Invariants & Boundary Summary')
    report.append('- **Class-0 Read Inspection**: Complete with zero workspace mutations.')
    report.append(f'- **Total Manifests Found**: {len(manifests)}')
    return "\n".join(report)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Deterministic Repo Surveyor')
    parser.add_argument('--root', default='.', help='Root directory to survey')
    parser.add_argument('--json', action='store_true', help='Output in JSON format')
    args = parser.parse_args()

    if args.json:
        out = {
            'manifests': detect_manifests(args.root),
            'entrypoints': scan_entrypoints(args.root),
            'tree': build_bounded_tree(args.root, max_depth=2)
        }
        print(json.dumps(out, indent=2))
    else:
        print(generate_report(args.root))
