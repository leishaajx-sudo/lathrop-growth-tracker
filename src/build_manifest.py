"""Build data/manifest.csv from data/pdf_links.txt and the PDFs in data/raw."""
import csv
import datetime
import hashlib
import re
from pathlib import Path

MONTHS = {n: i for i, n in enumerate(
    ["january", "february", "march", "april", "may", "june", "july",
     "august", "september", "october", "november", "december"], start=1)}


def month_of(name):
    n = name.lower()
    m = re.search(r"(20\d\d)[-_](\d\d)", n)
    if m:
        return f"{m.group(1)}-{m.group(2)}", "YYYY-MM in file name"
    m = re.search(r"(20\d\d)_([a-z]+)_", n)
    if m and m.group(2) in MONTHS:
        return f"{m.group(1)}-{MONTHS[m.group(2)]:02d}", "YYYY_monthname in file name"
    m = re.search(r"_(\d{1,2})\.(\d\d)\.pdf$", n)
    if m:
        return f"20{m.group(2)}-{int(m.group(1)):02d}", "M.YY in file name"
    raise ValueError(f"cannot map a month for {name}")


def kind_of(name):
    n = name.lower()
    if "completed" in n:
        return "finaled"
    if "issued" in n:
        return "issued"
    raise ValueError(f"cannot tell report type for {name}")


def main():
    urls = {Path(u).name: u for u in Path("data/pdf_links.txt").read_text().split()}
    rows = []
    for name, url in urls.items():
        f = Path("data/raw") / name
        if not f.exists():
            raise SystemExit(f"missing file: {f}")
        month, rule = month_of(name)
        rows.append([
            kind_of(name), month, name, url,
            datetime.date.fromtimestamp(f.stat().st_mtime).isoformat(),
            hashlib.sha256(f.read_bytes()).hexdigest(),
            f"month mapped by: {rule}",
        ])
    rows.sort(key=lambda r: (r[1], r[0]))
    with open("data/manifest.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["report_type", "report_month", "file_name", "url",
                    "download_date", "sha256", "notes"])
        w.writerows(rows)
    months = sorted({r[1] for r in rows})
    print(f"{len(rows)} files, {len(months)} months: {months[0]} to {months[-1]}")


if __name__ == "__main__":
    main()
