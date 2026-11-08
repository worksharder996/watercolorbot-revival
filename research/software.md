# Software inventory

Research date: 2026-11-08.

## Executive assessment

- **Best preserved original path:** `evil-mad/wcb-ink` with maintained `plotink`. This is the shortest route from a modern Inkscape workflow to EBB motion.
- **Original RoboPaint is legacy:** Electron 1.6.10, old native SerialPort dependencies, and a 2017 application stack make a current build a porting project rather than a normal rebuild.
- **RoboPaint RT is historical:** Processing/Java source with last meaningful application work in 2014 and binaries aimed at OS versions of that period.
- **CNCServer is the strongest API base:** default branch 2.9.1 supports Node >=16 and SerialPort 10.5; unreleased branches explore Node 20/24 and a Rust renderer.
- **WaterColorBlocks is educational reference material:** Scratch 2/Snap 4-era examples need a modern bridge and security model.
- No maintained drop-in RoboPaint replacement was found.

## wcb-ink

Upstream: <https://github.com/evil-mad/wcb-ink>

- Python Inkscape extensions for WaterColorBot.
- File headers declare GPL-2.0-or-later; no root license file is detected by GitHub.
- Default branch source identifies as version 1.6.1 and uses the Inkscape 1.x extension schema.
- Default branch last substantive update: 2023-12-22.
- `V1_axidraw` branch received work in June 2026 targeting AxiDraw 3.9.5/Inkscape integration.
- Dependencies include `plotink`, `ink_extensions`, `ink_extensions_utils`, `lxml`, and PySerial through Plotink.
- Old packaged installers target Inkscape 0.91 and should not be treated as current deployment packages.

Important unresolved behavior includes alternate paper sizes, re-inking/washing pauses, cancellation during plotting, and some hatch behavior.

## plotink

Upstream: <https://github.com/evil-mad/plotink>

- Shared Python routines for EggBot, WaterColorBot, AxiDraw, and similar plotters.
- MIT licensed.
- Active through 2026.
- Current package metadata observed: 1.14.3, Python >=3.6.
- A modernization should consume Plotink as a dependency instead of reviving old copied EBB/serial routines.

## RoboPaint

Upstream: <https://github.com/evil-mad/robopaint>

- Electron desktop GUI for importing/editing SVGs, simulating, and running painting modes.
- README/package metadata state MIT, but no root license file is present.
- Last default-branch code activity: 2017-09-23.
- Latest published application line: 2.1.0.
- Pinned to Electron 1.6.10 and an old native SerialPort stack.
- Bundles CNCServer 2.7.x and separate mode packages.

A responsible modern port would require Electron API migration, dependency replacement, native serial work, packaging/signing/notarization, and security review. It is not a safe starting point for an internet-exposed application.

### Mode repositories

- `evil-mad/robopaint-mode-edit` — MIT
- `evil-mad/robopaint-mode-print` — MIT
- `evil-mad/robopaint-mode-remote` — MIT; documents the high-level print queue API
- Additional historical Techninja modes exist for manual, spiral, stipple, and example workflows.

## RoboPaint RT

Upstream: <https://github.com/evil-mad/robopaint-rt>

- Processing/Java real-time freehand painting application.
- Uses Processing serial and Ani libraries.
- No clear repository-level license was found.
- Last meaningful source work: 2014.
- Historical binaries target Windows through Windows 8, OS X 10.7.3–10.9, and old Linux architectures.

Use this as interaction and protocol reference; expect source migration for a modern runtime.

## CNCServer and APIs

Upstream: <https://github.com/techninja/cncserver>

- Node.js HTTP/Socket.IO bridge to serial EBB machines.
- README/package metadata state MIT, but no root license file is detected.
- Default branch 2.9.1 supports Node >=16 (README recommends 18+) and SerialPort 10.5.
- Local endpoint: `http://localhost:4242`.
- The REST API exposes pen motion/state, tools/colors, motors, buffering, and events.
- A GET-oriented Scratch API exposes coordinate movement, tool/water selection, washing, and parking.
- RoboPaint Remote mode adds `/robopaint/v1/print` queue operations for SVG jobs.

Security warning: the historical local APIs do not provide a modern authentication/origin model. Bind to localhost or a controlled network and add authentication before network exposure.

Experimental branches include Node 20 and a 2026 Node 24/Rust-renderer line. They are development branches, not stable published releases.

## WaterColorBlocks

Upstream: <https://github.com/evil-mad/WaterColorBlocks>

- MIT licensed.
- Contains Scratch 2 `.sb2`, experimental HTTP extension files, Snap XML examples, and a BeetleBlocks example.
- Last commit: 2018-03-20.
- Requires RoboPaint or standalone CNCServer.
- The historical online Scratch path relied on RawGit, which has been discontinued.
- HTTPS editors may block local HTTP calls as mixed content.

A revival should port the teaching concepts to current Scratch/Snap extension mechanisms and a secured local bridge.

## Recommended software sequence

1. Pin and test current `wcb-ink` + compatible `plotink` against one exact Inkscape release.
2. Validate motion against an EBB with the brush removed.
3. Prototype a small, local-only control service using CNCServer 2.9.1 or a minimal direct serial client.
4. Reimplement painting primitives and recovery behavior.
5. Only then decide whether a full RoboPaint-style GUI is worth rebuilding.
