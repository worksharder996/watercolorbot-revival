# Open XY Watercolor Robot — preservation and revival research

This repository preserves source material and records a source-backed path toward building a modern XY watercolor-painting robot inspired by the discontinued Evil Mad Scientist WaterColorBot.

**Research snapshot:** 2026-11-08  
**Status:** research and preservation archive; no new machine design has been validated yet.

## Bottom line

A new build is feasible. The original mechanical reference designs, bills of materials, quick-start manuals, EiBotBoard designs/firmware/protocol documentation, and multiple control-software paths remain available.

The safest practical architecture is:

1. Use the **WaterColorBot 2.0 mechanics** as a dimensional and motion reference, redesigning obsolete or hard-to-source parts in a modern CAD format.
2. Prototype with a genuine **EiBotBoard (EBB)** or compatible two-stepper-plus-servo controller.
3. Use **modernized `wcb-ink` + `plotink`** for the shortest path to first motion.
4. Evaluate the actively modernized default branch of **CNCServer** for a web/API control layer.
5. Treat original **RoboPaint** and **RoboPaint RT** as design references, not as dependable modern applications.

## What is preserved here

- `hardware/reference-designs/`
  - Original WaterColorBot v1.0 and v2.0 download archives.
  - Extracted SVG, SolidWorks, PDF, Gerber/flex-PCB, and BOM files.
- `hardware/guides/`
  - Quick-start guides for WaterColorBot 1.0, 1.5, and 2.0.
- `controller/ebb-hardware/`
  - EiBotBoard design archives for hardware versions 2.1, 2.2, 2.3, 2.5, 2.6, and 2.7.
- `controller/ebb-firmware/`
  - Preserved EBB 2.5.4 firmware binary archive. Current source lives in the EggBot repository.
- `docs/wiki-snapshots/`
  - HTML snapshots of the core WaterColorBot documentation pages.
- `docs/controller/`
  - EBB overview, current and legacy command documentation, and release notes.
- `research/`
  - Hardware, software, controller, market/successor, licensing, and build-roadmap analysis.
- `sources/`
  - Retrieval manifests, checksums, source URLs, repository scans, and fork records.

## GitHub preservation forks

The related source repositories are preserved as forks in the same GitHub account. See [`research/repository-inventory.md`](research/repository-inventory.md) and [`sources/fork-manifest.tsv`](sources/fork-manifest.tsv).

Core upstreams include:

- [`evil-mad/wcb-ink`](https://github.com/evil-mad/wcb-ink) — Inkscape control path
- [`evil-mad/robopaint`](https://github.com/evil-mad/robopaint) — original desktop painting application
- [`evil-mad/robopaint-rt`](https://github.com/evil-mad/robopaint-rt) — real-time Processing application
- [`techninja/cncserver`](https://github.com/techninja/cncserver) — REST/API controller
- [`evil-mad/WaterColorBlocks`](https://github.com/evil-mad/WaterColorBlocks) — Scratch/Snap examples
- [`evil-mad/EggBot`](https://github.com/evil-mad/EggBot) — EBB firmware and protocol sources
- [`sparkfun/EiBotBoard`](https://github.com/sparkfun/EiBotBoard) — controller-board design source

## Modern commercial successor

Bantam Tools now sells a reimagined **Bantam Tools WaterColorBot** (listed at USD $699 domestic / $799 international when researched). Evil Mad Scientist founders Lenore Edman and Windell Oskay are now Bantam Tools’ COO and CTO. This commercial machine is useful as a present-day benchmark, but this repository does not assume its hardware or software is open source.

## Important licensing and trademark note

This repository contains materials from several authors under different licenses. **There is intentionally no repository-wide license covering imported material.** Read [`LEGAL-AND-PROVENANCE.md`](LEGAL-AND-PROVENANCE.md) before modifying or redistributing anything.

The original hardware reference design states that it is dual-licensed under **CC BY-SA 3.0** or the **TAPR Open Hardware License**. “WaterColorBot,” “Evil Mad Scientist,” and “Evil Mad Scientist Laboratories” are stated trademarks of Evil Mad Science LLC. A new product needs its own name and clear manufacturer attribution.

## Recommended next milestone

Before purchasing parts, create a clean-sheet CAD model and a verified BOM for one prototype. Then bench-test the controller, two motors, and brush-lift servo before building the frame. See [`research/build-roadmap.md`](research/build-roadmap.md).

## Preservation integrity

Download manifests include source URL, final URL, byte count, retrieval timestamp, and SHA-256 checksum. The preserved archives are kept alongside extracted copies so later changes can be audited.
