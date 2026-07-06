# coding: utf-8

"""
Talks markdown generator for academicpages.

Input:
  markdown_generator/talks.tsv

Required columns:
  title, type, url_slug, venue, date, location, talk_url, description

Output:
  _talks/YYYY-MM-DD-url-slug.md
"""

from pathlib import Path
import re
import json
import pandas as pd


# Paths
BASE_DIR = Path(__file__).resolve().parent
TSV_FILE = BASE_DIR / "talks.tsv"
OUTPUT_DIR = BASE_DIR.parent / "_talks"

# 如果你的 _talks 文件全部由 talks.tsv 生成，建议设为 True
# 这样可以删除旧的错误 md，避免 Jekyll 继续读取旧文件
CLEAN_OUTPUT_DIR = True


def yaml_quote(value):
    """Return a safe quoted YAML string."""
    value = "" if pd.isna(value) else str(value).strip()
    return json.dumps(value, ensure_ascii=False)


def clean_text(value):
    """Clean normal text fields."""
    if pd.isna(value):
        return ""
    return str(value).strip()


def normalize_date(value):
    """
    Convert dates such as:
      2021-04-21
      4/21/2021
      04/21/2021
    into:
      2021-04-21
    """
    value = clean_text(value)

    if not value:
        raise ValueError("Empty date field")

    parsed = pd.to_datetime(value, errors="raise", dayfirst=False)
    return parsed.strftime("%Y-%m-%d")


def slugify(value):
    """
    Convert url_slug into a clean URL slug.
    Example:
      soft-xray-population-CLAP Workshop
    becomes:
      soft-xray-population-clap-workshop
    """
    value = clean_text(value).lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value)
    value = value.strip("-")
    return value


def make_talk_markdown(item):
    title = clean_text(item.get("title"))
    talk_type = clean_text(item.get("type")) or "Talk"
    venue = clean_text(item.get("venue"))
    location = clean_text(item.get("location"))
    talk_url = clean_text(item.get("talk_url"))
    description = clean_text(item.get("description"))

    date = normalize_date(item.get("date"))
    slug = slugify(item.get("url_slug"))

    if not title:
        raise ValueError("Missing title")
    if not slug:
        raise ValueError(f"Missing url_slug for talk: {title}")

    filename = f"{date}-{slug}.md"
    permalink = f"/talks/{date}-{slug}"

    lines = [
        "---",
        f"title: {yaml_quote(title)}",
        "collection: talks",
        f"type: {yaml_quote(talk_type)}",
        f"permalink: {permalink}",
    ]

    if venue:
        lines.append(f"venue: {yaml_quote(venue)}")

    lines.append(f"date: {date}")

    if location:
        lines.append(f"location: {yaml_quote(location)}")

    lines.append("---")
    lines.append("")

    if talk_url:
        lines.append(f"[More information here]({talk_url})")
        lines.append("")

    if description:
        lines.append(description)
        lines.append("")

    md = "\n".join(lines)
    return filename, md


def main():
    if not TSV_FILE.exists():
        raise FileNotFoundError(f"Cannot find {TSV_FILE}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if CLEAN_OUTPUT_DIR:
        for old_file in OUTPUT_DIR.glob("*.md"):
            old_file.unlink()

    talks = pd.read_csv(TSV_FILE, sep="\t", header=0, dtype=str, keep_default_na=False)

    required_columns = [
        "title",
        "type",
        "url_slug",
        "venue",
        "date",
        "location",
        "talk_url",
        "description",
    ]

    missing = [col for col in required_columns if col not in talks.columns]
    if missing:
        raise ValueError(f"Missing columns in talks.tsv: {missing}")

    for idx, item in talks.iterrows():
        filename, md = make_talk_markdown(item)
        output_file = OUTPUT_DIR / filename

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(md)

        print(f"Generated: {output_file.relative_to(BASE_DIR.parent)}")


if __name__ == "__main__":
    main()