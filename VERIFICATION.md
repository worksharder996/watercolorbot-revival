# Archive verification

Verified on 2026-11-08 after cloning the public repository.

## Results

- All 26 files listed across the two JSON download manifests exist.
- Every listed byte count and SHA-256 digest matches.
- All nine preserved ZIP archives pass full member-integrity checks.
- `git fsck --full --strict` reports no repository-integrity errors.
- All twelve entries in `sources/fork-manifest.tsv` are GitHub forks whose parent matches the recorded upstream repository.

Run the repeatable local check with:

```bash
python3 scripts/verify_archive.py
```

The script checks the JSON-manifested downloads and ZIP contents. GitHub fork-parent relationships require live API access and were verified separately with the GitHub API.
