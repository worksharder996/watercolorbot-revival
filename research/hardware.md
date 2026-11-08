# Original hardware and documentation

Research date: 2026-11-08.

## Official reference designs

Canonical page: <https://wiki.evilmadscientist.com/WaterColorBot_Reference_Design>

The official page provides two downloadable designs:

- **WaterColorBot 1.0** — original ZIP, preserved as `hardware/reference-designs/wcb_refdesign_v1.zip`
  - seven Inkscape SVG design/sketch files
  - CSV bill of materials
  - design notes and license text
- **WaterColorBot 2.0 revision 1** — preserved as `hardware/reference-designs/WCBv2_r1.zip`
  - updated wooden-part SVGs
  - SolidWorks parts for carriage and winches
  - manufacturing PDFs
  - flex-PCB source and Gerbers
  - CSV bill of materials

Both archives are also extracted under `hardware/reference-designs/v1/` and `v2/`.

## License and marks

The official page states that the hardware reference design is dual-licensed under either CC BY-SA 3.0 US or TAPR OHL. Both downloaded archives contain `copying.txt`.

The page also states that “WaterColorBot,” “Evil Mad Scientist,” and “Evil Mad Scientist Laboratories” are trademarks of Evil Mad Science LLC. A derivative machine needs its own name and manufacturer identity.

## Preserved quick-start manuals

- WaterColorBot 1.0: `hardware/guides/WCB_QuickStart_1_0_B_Linear.pdf`
- WaterColorBot 1.5: `hardware/guides/WCB_QuickStart_1_5_C_Linear.pdf`
- WaterColorBot 2.0: `hardware/guides/WCB_QuickStart_2A_Linear.pdf`

The main wiki and topic pages are snapshotted under `docs/wiki-snapshots/`, including software, paper, paint, writing implements, and troubleshooting.

## Mechanical concept

The design is an XY cable-driven plotter carrying a brush. Two stepper-driven winches coordinate carriage motion. A servo lifts/lowers the brush. Fixed locations hold watercolor pans and rinse water; software inserts wash, re-ink, and painting moves.

## What needs redesign

The archive is sufficient as a reference, but a literal production clone is not the best first target:

- SolidWorks source is old and incomplete as a modern parametric assembly.
- Original custom flexure/flex-PCB and carriage parts may be difficult or costly to reproduce.
- Legacy BOM supplier part numbers need current substitutions.
- The design lacks modern enclosure, spill isolation, homing, and serviceability features expected in a new product.
- Cable/winch geometry and calibration should be revalidated rather than assumed.

## Recommended hardware baseline

- Preserve the original work-envelope and pan/water concept initially.
- Remodel every fabricated part in a current CAD tool.
- Use commonly available bipolar steppers, bearings, shafts, cable, and fasteners where possible.
- Keep the electronics and USB/power entry physically separated from all wet zones.
- Make the palette/water tray removable and washable.
- Add a deterministic homing or registration approach.
- Validate brush pressure and cable tension over the entire work area.

## Archived integrity

`sources/download-manifest.json` records URL, redirected URL, byte count, retrieval timestamp, media type, and SHA-256 digest for the official archives, manuals, and wiki pages.
