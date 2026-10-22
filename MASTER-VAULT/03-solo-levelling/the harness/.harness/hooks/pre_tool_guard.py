#!/usr/bin/env python3
"""Deterministic Pre-Tool Security & Secret Guard (CAP-20, CAP-24, CAP-26, CAP-37).

Rejects destructive commands, unconfined filesystem operations, and secret leaks
before tool execution begins.
"""
import argparse
import re
import sys

DANGEROUS_COMMAND_PATTERNS = [
    # rm destructive with recursive/force flags on ROOT/HOME/system path
    (re.compile(r"\brm\s+(-[a-z]*[rfRF][a-z]*\s+|--recursive\s+|--force\s+)+[\"']?([/~]|\.\./|/etc(?:/|$)|/usr(?:/|$)|/bin(?:/|$)|/var(?:/|$)|/root(?:/|$))", re.IGNORECASE), "Destructive rm -rf on root/unconfined path"),
    # rm with recursive/force flags on system/home absolute paths (quoted or not)
    (re.compile(r"\brm\s+(-[a-z]*[rfRF][a-z]*\s+|--recursive\s+|--force\s+)+[\"']?/(etc|usr|bin|var|root|home)(\b|/|\"|')", re.IGNORECASE), "Recursive rm on system/home path"),
    # bare recursive-force-quoted root
    (re.compile(r"\brm\s+-[a-z]*[rfRF][a-z]*\s+[\"'][/~]", re.IGNORECASE), "Recursive rm on quoted root/home path"),
    # rm -rf -- / (option terminator before path)
    (re.compile(r"\brm\s+(-[a-z]*[rfRF][a-z]*\s+)*--\s+[\"']?/(?:$|etc|usr|bin|var|root|home)", re.IGNORECASE), "Recursive rm -- terminator on root/system path"),
    (re.compile(r"\bmkfs(\.\w+)?\b", re.IGNORECASE), "Filesystem format command (mkfs)"),
    # dd — option order independent, quoted devices, NVMe
    (re.compile(r"\bdd\b(?=.*\b(?:if=|of=))(?=.*(?:of=[\"']*/dev/|of=.*nvme))", re.IGNORECASE), "Raw block device overwrite (dd)"),
    (re.compile(r"\bdd\b.*\bof=[\"']*/dev/", re.IGNORECASE), "Raw block device write target (dd)"),
    (re.compile(r":\(\)\s*\{\s*:\s*\|\s*:\s*&\s*\}\s*;"), "Fork bomb pattern"),
    (re.compile(r"\bchmod\s+(-[a-z]*[rR][a-z]*\s+)?777\s+([/~]|\.\.)", re.IGNORECASE), "Insecure unconfined permissions (chmod -R 777)"),
    (re.compile(r">\s*([\"']*)/dev/sd[a-z]"), "Direct disk device write"),
    # curl/wget pipe to ANY shell/python — with sudo, zsh, python
    (re.compile(r"\b(curl|wget)\b.*\|\s*(sudo\s+)?(?:ba|z)?sh\b", re.IGNORECASE), "Unverified remote script pipe to shell"),
    (re.compile(r"\b(curl|wget)\b.*\|\s*(sudo\s+)?(python3|python|sh|bash|zsh|fish|tcsh|ksh)\b", re.IGNORECASE), "Unverified remote script pipe to interpreter"),
    (re.compile(r"\b(curl|wget)\b.*\|\s*(sudo\s+)?python3?\b", re.IGNORECASE), "Unverified remote script pipe to python"),
    # force push to main/master — both arg orders, -f, --force, --force-with-lease, refspec +branch
    (re.compile(r"\bgit\s+push\b.*(?:--force-with-lease|--force|-[fF])\b", re.IGNORECASE), "Force push (any destination)"),
    (re.compile(r"\bgit\s+push\b.*(\+?main|\+?master)\b.*(--force|-f\b|--force-with-lease)?", re.IGNORECASE), "Force push to protected main/master branch"),
    (re.compile(r"\bgit\s+push\b.*(main|master)[^a-z0-9].*(\+[a-z]|HEAD:[a-z])", re.IGNORECASE), "Force push via refspec to main/master"),
    (re.compile(r"\b(shutdown|reboot|poweroff|init\s+0)\b", re.IGNORECASE), "System shutdown / reboot invocation"),
]

SECRET_PATTERNS = [
    (re.compile(r"AKIA[0-9A-Z]{16}"), "AWS Access Key ID"),
    (re.compile(r"ASIA[0-9A-Z]{16}"), "AWS Temporary (STS) Access Key"),
    (re.compile(r"ghp_[a-zA-Z0-9]{36}"), "GitHub Personal Access Token"),
    (re.compile(r"github_pat_[a-zA-Z0-9]{22}_[a-zA-Z0-9]{59}"), "GitHub Fine-Grained Token"),
    (re.compile(r"glpat-[a-zA-Z0-9\-_]{20,24}"), "GitLab Personal Access Token"),
    (re.compile(r"-----BEGIN\s+(?:RSA\s+|EC\s+|DSA\s+|OPENSSH\s+)?PRIVATE\s+KEY-----"), "Private Key Header"),
    (re.compile(r"ey[A-Za-z0-9_-]{10,}\.ey[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}"), "JSON Web Token (JWT)"),
    # key=value with or without quotes
    (re.compile(r"\b(api[_-]?key|secret|password|token|passwd)\s*[:=]\s*[\"']?[A-Za-z0-9_+\-]{16,}[\"']?", re.IGNORECASE), "Hardcoded API Key / Secret Assignment"),
]

def evaluate_command(cmd: str):
    for pattern, description in DANGEROUS_COMMAND_PATTERNS:
        if pattern.search(cmd):
            return False, f"[SECURITY REJECTION: DESTRUCTIVE COMMAND] {description} in '{cmd.strip()}'"
    
    for pattern, description in SECRET_PATTERNS:
        if pattern.search(cmd):
            return False, f"[SECURITY REJECTION: SECRET EXPOSURE] Detected {description} in command line"
            
    return True, "ok"

def evaluate_content(content: str):
    for pattern, description in SECRET_PATTERNS:
        if pattern.search(content):
            return False, f"[SECURITY REJECTION: SECRET LEAK] Detected {description} in file modification content"
    return True, "ok"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pre-tool execution guard")
    parser.add_argument("--command", help="Command string to evaluate")
    parser.add_argument("--content", help="File content string to evaluate")
    args, unknown = parser.parse_known_args()

    input_text = ""
    if args.command:
        input_text = args.command
        ok, reason = evaluate_command(input_text)
    elif args.content:
        input_text = args.content
        ok, reason = evaluate_content(input_text)
    elif not sys.stdin.isatty():
        input_text = sys.stdin.read()
        ok, reason = evaluate_command(input_text)
    elif unknown:
        input_text = " ".join(unknown)
        ok, reason = evaluate_command(input_text)
    else:
        sys.exit(0)

    if not ok:
        print(f"Error: {reason}", file=sys.stderr)
        # Exit code 2 indicates tool execution rejection (Claude Code / Antigravity convention)
        sys.exit(2)

    sys.exit(0)
