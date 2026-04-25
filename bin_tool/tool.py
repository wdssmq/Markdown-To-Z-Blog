"""Temporary tool: collect file/alias info from markdown posts."""

from __future__ import annotations

import json
import os


def _get_md_list(dir_path: str) -> list[str]:
    """Collect markdown files under _posts and include nested doc.md."""
    md_list: list[str] = []
    for name in os.listdir(dir_path):
        if name in {".gitkeep", "1970-01-01-empty.md"}:
            continue
        cur_path = os.path.join(dir_path, name)
        if os.path.isfile(cur_path) and os.path.splitext(name)[1] == ".md":
            md_list.append(cur_path)
            continue
        doc_file = os.path.join(cur_path, "doc.md")
        if os.path.isdir(cur_path) and os.path.isfile(doc_file):
            md_list.append(doc_file)
    return md_list


def _project_root() -> str:
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _resolve_file_name(md_file_path: str) -> str:
    """Return file name without extension; for doc.md use directory name."""
    stem = os.path.splitext(os.path.basename(md_file_path))[0]
    if stem == "doc":
        return os.path.basename(os.path.dirname(md_file_path))
    return stem


def _extract_alias(md_file_path: str) -> str:
    """Extract alias from YAML front matter; return empty string when absent."""
    with open(md_file_path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    if not lines or lines[0].strip() != "---":
        return ""

    for i in range(1, len(lines)):
        line = lines[i].strip()
        if line == "---":
            break
        if not line.startswith("alias:"):
            continue
        value = line.split(":", 1)[1].strip()
        if (value.startswith('"') and value.endswith('"')) or (
            value.startswith("'") and value.endswith("'")
        ):
            value = value[1:-1]
        return value

    return ""


def main() -> None:
    root = _project_root()

    posts_dir = os.path.join(root, "_posts")
    output_file = os.path.join(root, "bin_tool", "post_aliases.json")

    result = []
    for md_file in sorted(_get_md_list(posts_dir)):
        file_name = _resolve_file_name(md_file)
        alias = _extract_alias(md_file)

        if "-new-post" in file_name:
            continue
        if alias == "":
            continue

        result.append(
            {
                "file": file_name,
                "alias": alias,
            }
        )

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"Done. {len(result)} items written to: {output_file}")


if __name__ == "__main__":
    main()
