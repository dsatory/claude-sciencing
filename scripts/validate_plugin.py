#!/usr/bin/env python3

import argparse
import json
import re
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_JSON = ROOT / ".claude-plugin" / "plugin.json"
MARKETPLACE_JSON = ROOT / ".claude-plugin" / "marketplace.json"
README = ROOT / "README.md"
CLAUDE_MD = ROOT / "CLAUDE.md"
RUNTIME_PATH_PREFIXES = ("references/", "literature/", ".claude/", "~/.claude/")
RUNTIME_PATH_NAMES = {"download_log.md"}


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def load_json(path):
    with path.open() as fh:
        return json.load(fh)


def find_command_refs(text):
    return set(re.findall(r"(?<![A-Za-z0-9_./-])/(sci-[a-z0-9-]+|pubmed-setup)\b(?!/)", text))


def find_path_refs(text):
    refs = set()
    for match in re.findall(r"`([^`\n]+\.(?:md|json|py))`", text):
        if (
            match.startswith(("http://", "https://", "~/"))
            or " " in match
            or "path/to/" in match
            or "wc -w" in match
            or "compliance_checklist_" in match
            or match in RUNTIME_PATH_NAMES
            or match.startswith(RUNTIME_PATH_PREFIXES)
        ):
            continue
        refs.add(match)
    return refs


def repo_relative_exists(source, ref):
    candidates = [
        (source.parent / ref).resolve(),
        (ROOT / ref).resolve(),
    ]
    return any(candidate.exists() for candidate in candidates)


def check_endpoint(url):
    opener = urllib.request.build_opener(NoRedirect())
    request = urllib.request.Request(
        url,
        method="HEAD",
        headers={"Accept": "application/json, text/event-stream"},
    )
    try:
        with opener.open(request, timeout=10) as response:
            return ("ok", response.getcode(), url)
    except urllib.error.HTTPError as exc:
        if exc.code in {200, 204, 401, 405, 406}:
            return ("ok", exc.code, url)
        if exc.code in {301, 302, 307, 308}:
            return ("warn", exc.code, exc.headers.get("Location", ""))
        return ("error", exc.code, str(exc))
    except Exception as exc:  # pragma: no cover
        return ("error", None, str(exc))


def main():
    parser = argparse.ArgumentParser(description="Validate claude-sciencing repo metadata.")
    parser.add_argument(
        "--check-endpoints",
        action="store_true",
        help="Probe MCP endpoints declared in .claude-plugin/plugin.json",
    )
    args = parser.parse_args()

    errors = []
    warnings = []

    plugin = load_json(PLUGIN_JSON)
    marketplace = load_json(MARKETPLACE_JSON)
    readme_text = README.read_text()

    plugin_version = plugin["version"]
    marketplace_version = marketplace["plugins"][0]["version"]
    if plugin_version != marketplace_version:
        errors.append(
            f"Version mismatch: plugin.json={plugin_version} marketplace.json={marketplace_version}"
        )

    headline_match = re.search(r"^# Claude Sciencing v([0-9.]+)$", readme_text, re.MULTILINE)
    if not headline_match:
        errors.append("README version headline not found")
    elif headline_match.group(1) != plugin_version:
        errors.append(
            f"README version mismatch: README={headline_match.group(1)} plugin.json={plugin_version}"
        )

    install_url = "git clone https://github.com/dsatory/claude-sciencing.git"
    if install_url not in readme_text:
        errors.append("README install URL is not the canonical GitHub clone URL")

    if not CLAUDE_MD.exists():
        errors.append("CLAUDE.md is missing")

    commands = {path.stem for path in (ROOT / "commands").glob("*.md")}
    markdown_files = list(ROOT.rglob("*.md"))

    for path in markdown_files:
        text = path.read_text()
        for ref in sorted(find_command_refs(text)):
            if ref.startswith("sci-") and ref not in commands:
                errors.append(f"{path.relative_to(ROOT)} references missing command /{ref}")
            if ref == "pubmed-setup" and ref not in commands:
                errors.append(f"{path.relative_to(ROOT)} references missing command /{ref}")

        for ref in sorted(find_path_refs(text)):
            if not repo_relative_exists(path, ref):
                errors.append(f"{path.relative_to(ROOT)} references missing file `{ref}`")

    banned_global = {
        "AskUserQuestion": "Replace AskUserQuestion with plain user-prompt instructions",
        "`library.bib`": "Use references/library.bib",
        "`library.md`": "Use references/library.md",
    }
    for needle, message in banned_global.items():
        for path in markdown_files:
            text = path.read_text()
            if needle in text and path.name != "CLAUDE.md":
                errors.append(f"{path.relative_to(ROOT)} contains `{needle}`: {message}")

    if "tracked changes" in readme_text:
        errors.append("README.md contains `tracked changes`: Avoid claiming tracked changes support")

    if args.check_endpoints:
        for name, server in plugin.get("mcpServers", {}).items():
            status, code, detail = check_endpoint(server["url"])
            if status == "error":
                errors.append(f"MCP endpoint {name} failed ({code}): {detail}")
            elif status == "warn":
                warnings.append(f"MCP endpoint {name} redirected ({code}) to {detail}")

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
