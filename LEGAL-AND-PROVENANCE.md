# Licensing, trademarks, and provenance

This is a research and preservation repository, not legal advice. Imported files keep their original notices and licenses. No umbrella license is asserted over third-party material.

## Original WaterColorBot hardware

The official reference-design page states that the WaterColorBot hardware reference design is dual-licensed under either:

- Creative Commons Attribution-ShareAlike 3.0 United States (CC BY-SA 3.0 US), or
- TAPR Open Hardware License (TAPR OHL).

Both original design archives include `copying.txt`; those notices are preserved with the extracted files. Attribution and applicable share-alike/source-documentation obligations must be followed when distributing modified designs.

Source: <https://wiki.evilmadscientist.com/WaterColorBot_Reference_Design>

## Trademarks

The same official page states that these are trademarks of Evil Mad Science LLC:

- WaterColorBot
- Evil Mad Scientist
- Evil Mad Scientist Laboratories

A derivative machine should use a new name and clearly identify its actual manufacturer. Open hardware licensing does not grant trademark rights.

## Software licenses

License status must be assessed repository by repository:

- `wcb-ink`: Python file headers state GPL-2.0-or-later; no root license file is currently detected by GitHub.
- `robopaint`: historical source headers include MIT-style notices and GPL-2.0 notices in different areas; dependency licenses also apply. Review before reuse.
- `robopaint-rt`: source headers state GPL-2.0-or-later; no root license file is currently detected by GitHub.
- `WaterColorBlocks`: MIT license file.
- `plotink`: MIT license file.
- `robopaint-mode-print`, `robopaint-mode-edit`, `robopaint-mode-remote`: MIT license files.
- `EggBot`: GPL-3.0 repository license.
- `madison_wcb`: MIT license file.
- `ebb-control`: MIT license file.
- `cncserver`: no repository-level license file detected during this survey; some individual files or dependencies may contain notices. Do not assume permission beyond GitHub-hosted forking without a fuller legal review.
- `sparkfun/EiBotBoard`: no root license file detected during this survey. Inspect file-level notices and upstream documentation before manufacturing or redistributing modified board files.

The API-derived scan is preserved in `sources/repository-license-scan.tsv`.

## EiBotBoard materials

The official EBB page describes the board as open-source hardware and software, but downloaded historical archives do not uniformly present a simple root license file. Current firmware is hosted in `evil-mad/EggBot` under that repository's GPL-3.0 license. Hardware redistribution should retain all embedded notices and be reviewed against the original EBB documentation and file-level metadata.

## Commercial successor

The current Bantam Tools WaterColorBot is a separate commercial product. Nothing in this archive claims that its designs, software, product photography, branding, or other materials are open source.

## Retrieval and verification

- `sources/download-manifest.json` — original WaterColorBot files and wiki snapshots
- `sources/controller-download-manifest.json` — EBB hardware, firmware, and documentation
- `sources/repository-license-scan.tsv` — GitHub repository license scan
- `sources/fork-manifest.tsv` — preserved GitHub forks

Each download manifest records SHA-256 hashes. Original URLs remain the preferred attribution targets.
