#!/usr/bin/env python3
"""Scan this demo repository for sensitive-looking content.

The script is read-only. It prints findings grouped as:
- HIGH_RISK: likely real secrets or private identifiers that must be removed.
- ALLOWED_PLACEHOLDER: public-safe placeholders such as YOUR_API_KEY_HERE.
- TECH_TERM_FALSE_POSITIVE: technical words that are expected in this demo.
- REVIEW: suspicious keywords that should be checked manually.
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path


PLACEHOLDERS = {
    "YOUR_API_KEY_HERE",
    "YOUR_FEISHU_APP_ID",
    "YOUR_FEISHU_APP_SECRET",
    "YOUR_MODEL_ENDPOINT_HERE",
    "YOUR_DIFY_API_KEY",
    "YOUR_BOT_WEBHOOK_URL",
    "YOUR_WORKSPACE_ID",
    "YOUR_MODEL_PROVIDER_HERE",
    "YOUR_MODEL_NAME_HERE",
    "YOUR_FEISHU_VERIFICATION_TOKEN",
    "YOUR_FEISHU_ENCRYPT_KEY",
}

TECH_TERMS = {
    "API",
    "Token",
    "OpenAI",
    "DASHSCOPE",
    "Feishu",
    "Dify",
    "OpenClaw",
}

SUSPICIOUS_TERMS = [
    "api_key",
    "apikey",
    "secret",
    "token",
    "password",
    "appSecret",
    "Authorization",
    "Bearer",
    "sk-",
    "OPENAI",
    "DASHSCOPE",
    "FEISHU",
    "XIAOMI",
    ".env",
    "API",
    "Token",
    "Feishu",
    "Dify",
    "OpenClaw",
]

TERM_PATTERNS = [
    (
        term,
        re.compile(re.escape(term), re.IGNORECASE)
        if term in {".env", "sk-"}
        else re.compile(rf"(?<![A-Za-z0-9_]){re.escape(term)}(?![A-Za-z0-9_])", re.IGNORECASE),
    )
    for term in SUSPICIOUS_TERMS
]

SAFE_EXPLANATION_PATTERN = re.compile(
    r"(?i)(do not|never|public-safe|placeholder|redact|blur|sanitized|"
    r"must not|must be removed|private environment|not contain|real|"
    r"不包含|不能|不得|必须|打码|脱敏|占位符|真实|公开|安全)"
)

SAFE_CONTEXT_FILES = {
    ".gitignore",
    "safety-notes.md",
    "screenshots/README.md",
}

HIGH_RISK_PATTERNS = [
    ("openai_key", re.compile(r"sk-[A-Za-z0-9_-]{20,}")),
    ("bearer_token", re.compile(r"Bearer\s+[A-Za-z0-9._~+\-/]{20,}=*", re.IGNORECASE)),
    ("private_key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    (
        "assigned_secret",
        re.compile(
            r"(?i)\b(api[_-]?key|apikey|secret|token|password|appSecret|Authorization)\b"
            r"\s*[:=]\s*['\"]?(?!YOUR_|PLACEHOLDER|REDACTED|<)[A-Za-z0-9._~+\-/]{12,}"
        ),
    ),
    ("email", re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")),
    ("cn_phone", re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)")),
    ("ip_addr", re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")),
]

IGNORED_DIRS = {
    ".git",
    "node_modules",
    ".venv",
    "venv",
    "__pycache__",
    "dist",
    "build",
    "volumes",
    "postgres",
    "redis",
    "weaviate",
    "storage",
}

BINARY_SUFFIXES = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".ico",
    ".pdf",
    ".docx",
    ".xlsx",
    ".pptx",
    ".zip",
    ".rar",
    ".7z",
    ".mp4",
    ".mov",
}


def iter_files(root: Path):
    scanner = Path(__file__).resolve()
    for path in root.rglob("*"):
        if path.is_dir():
            continue
        if any(part in IGNORED_DIRS for part in path.parts):
            continue
        if path.resolve() == scanner:
            continue
        if path.suffix.lower() in BINARY_SUFFIXES:
            continue
        yield path


def classify_line(line: str, rel_path: str = ""):
    placeholder_hits = sorted(p for p in PLACEHOLDERS if p in line)
    if placeholder_hits:
        return "ALLOWED_PLACEHOLDER", ", ".join(placeholder_hits)

    high_hits = []
    for label, pattern in HIGH_RISK_PATTERNS:
        if pattern.search(line):
            high_hits.append(label)
    if high_hits:
        return "HIGH_RISK", ", ".join(sorted(set(high_hits)))

    term_hits = [term for term, pattern in TERM_PATTERNS if pattern.search(line)]

    if not term_hits:
        return None, None

    tech_terms_lower = {t.lower() for t in TECH_TERMS}
    if (
        all(t.lower() in tech_terms_lower for t in term_hits)
        or SAFE_EXPLANATION_PATTERN.search(line)
        or rel_path.replace("\\", "/") in SAFE_CONTEXT_FILES
        or "work scope confirmation" in line
    ):
        return "TECH_TERM_FALSE_POSITIVE", ", ".join(sorted(set(term_hits)))

    return "REVIEW", ", ".join(sorted(set(term_hits)))


def scan(root: Path):
    findings = defaultdict(list)
    for path in iter_files(root):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = path.read_text(encoding="utf-8", errors="replace")
        rel = path.relative_to(root)
        for number, line in enumerate(text.splitlines(), start=1):
            category, reason = classify_line(line, str(rel))
            if category:
                findings[category].append((str(rel), number, reason, line.strip()))
    return findings


def print_section(title: str, rows):
    print(f"\n## {title}")
    if not rows:
        print("None")
        return
    grouped = defaultdict(list)
    for rel, number, reason, line in rows:
        grouped[(rel, reason)].append((number, line))
    for (rel, reason), entries in sorted(grouped.items()):
        line_numbers = ", ".join(str(n) for n, _ in entries[:12])
        more = "" if len(entries) <= 12 else f", ... (+{len(entries) - 12} more)"
        print(f"- {rel} | lines {line_numbers}{more} | {reason}")
        for number, line in entries[:3]:
            print(f"  line {number}: {line[:180]}")


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    findings = scan(root)
    print(f"Sensitive scan report for: {root}")
    print_section("HIGH_RISK", findings.get("HIGH_RISK", []))
    print_section("ALLOWED_PLACEHOLDER", findings.get("ALLOWED_PLACEHOLDER", []))
    print_section("TECH_TERM_FALSE_POSITIVE", findings.get("TECH_TERM_FALSE_POSITIVE", []))
    print_section("REVIEW", findings.get("REVIEW", []))
    return 1 if findings.get("HIGH_RISK") else 0


if __name__ == "__main__":
    raise SystemExit(main())
