#!/usr/bin/env python3
"""Verify preserved downloads against the repository manifests."""

from __future__ import annotations

import hashlib
import json
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFESTS = (
    ROOT / "sources" / "download-manifest.json",
    ROOT / "sources" / "controller-download-manifest.json",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    errors: list[str] = []
    checked = 0

    for manifest_path in MANIFESTS:
        rows = json.loads(manifest_path.read_text(encoding="utf-8"))
        for row in rows:
            relative = Path(row["path"])
            path = ROOT / relative
            checked += 1
            if not path.is_file():
                errors.append(f"missing: {relative}")
                continue
            if path.stat().st_size != row["bytes"]:
                errors.append(
                    f"size mismatch: {relative}: "
                    f"{path.stat().st_size} != {row['bytes']}"
                )
            actual_hash = sha256(path)
            if actual_hash != row["sha256"]:
                errors.append(
                    f"hash mismatch: {relative}: "
                    f"{actual_hash} != {row['sha256']}"
                )
            if path.suffix.lower() == ".zip":
                try:
                    with zipfile.ZipFile(path) as archive:
                        corrupt = archive.testzip()
                    if corrupt:
                        errors.append(f"corrupt ZIP member: {relative}: {corrupt}")
                except zipfile.BadZipFile:
                    errors.append(f"invalid ZIP: {relative}")

    if errors:
        print(f"FAILED: {len(errors)} error(s) across {checked} manifest files")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"OK: verified {checked} manifest files and all ZIP archives")
    return 0


if __name__ == "__main__":
    sys.exit(main())
