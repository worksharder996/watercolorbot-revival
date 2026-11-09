# Repository inventory and preservation status

Research date: 2026-11-08.

## Preserved as forks in `worksharder996`

| Upstream | Preserved fork | Role | License status observed |
|---|---|---|---|
| `evil-mad/wcb-ink` | `worksharder996/wcb-ink` | Inkscape WaterColorBot extension | GPL-2.0-or-later in source headers; no root license |
| `evil-mad/robopaint` | `worksharder996/robopaint` | Original Electron painting application | MIT stated in metadata; no root license |
| `evil-mad/robopaint-rt` | `worksharder996/robopaint-rt` | Processing real-time painter | no clear root license found |
| `evil-mad/WaterColorBlocks` | `worksharder996/WaterColorBlocks` | Scratch/Snap/BeetleBlocks examples | MIT |
| `evil-mad/plotink` | `worksharder996/plotink` | Shared EBB/plotter Python routines | MIT |
| `evil-mad/robopaint-mode-print` | `worksharder996/robopaint-mode-print` | automatic painting mode | MIT |
| `evil-mad/robopaint-mode-edit` | `worksharder996/robopaint-mode-edit` | SVG import/edit mode | MIT |
| `evil-mad/robopaint-mode-remote` | `worksharder996/robopaint-mode-remote` | remote SVG print API/mode | MIT |
| `techninja/cncserver` | `worksharder996/cncserver` | REST/Socket.IO EBB bridge | MIT stated in metadata; no root license |
| `evil-mad/EggBot` | `worksharder996/EggBot` | EBB firmware, releases, and protocol source | GPL-3.0 |
| `jrheard/madison_wcb` | `worksharder996/madison_wcb` | community Python WaterColorBot library | MIT |
| `jmpinit/ebb-control` | `worksharder996/ebb-control` | JavaScript EBB wrapper | MIT |

These are GitHub forks, so their upstream relationships and history are preserved.

## Important linked repositories

| Repository | Role | Observed license |
|---|---|---|
| `sparkfun/EiBotBoard` | EBB board design source including v2.4 branch | no root license detected |
| `techninja/etch-a-bits` | physical/manual controller example via CNCServer | inspect before reuse |
| `beardicus/awesome-plotters` | curated plotter project list | inspect before reuse |
| `evil-mad/axidraw` | related modernized plotter software lineage | GPL-2.0 |
| `evil-mad/ink_extensions` | current Inkscape extension dependencies | GPL-2.0 |
| `techninja/robopaint-mode-manual` | historical advanced/manual mode | MIT reported by metadata |
| `techninja/robopaint-mode-spiral` | historical spiral/raster mode | no detected license |
| `techninja/robopaint-mode-stipple` | historical Voronoi/stipple mode | inspect before reuse |

GitHub anti-abuse throttling stopped the first preservation pass after nine core forks. A later verified pass added EggBot, `madison_wcb`, and `ebb-control`. The remaining repositories are recorded here and can be reviewed for preservation without losing the research archive.

## Source scans

- `sources/repository-license-scan.tsv` records GitHub API license results and root license-like files.
- `sources/fork-manifest.tsv` records the successfully created forks.

## Preservation policy

A fork is not a declaration that all contents may be relicensed. Keep upstream notices and history. Reuse code only under its actual repository/file license; repositories without a clear license need explicit review or permission.
