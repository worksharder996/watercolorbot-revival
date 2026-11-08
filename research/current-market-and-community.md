# Current market, successors, and community

Research date: 2026-11-08.

## Original project status

The Evil Mad Scientist WaterColorBot kit is discontinued, but its core wiki, reference-design downloads, manuals, and source repositories remain online.

The surviving ecosystem is unusually complete for a discontinued educational robot:

- full mechanical reference archives for v1 and v2
- BOMs and manufacturing files
- user and troubleshooting documentation
- EBB hardware, firmware, and command documentation
- Inkscape, desktop, real-time, API, Scratch, and Snap software references

## Current commercial WaterColorBot

Bantam Tools currently sells a reimagined **Bantam Tools WaterColorBot**.

Verified public product/search information at the research date:

- Product page: <https://bantamtools.com/products/bantam-tools-watercolorbot>
- Listed price: USD $699 domestic / $799 international
- Advertised paper capability: up to 9 × 12 inch watercolor paper
- Uses real brushes and watercolors
- Bantam Tools sells compatible palettes and related art-machine accessories

This is the likely commercial version referenced in the original request.

Bantam Tools’ retrospective identifies Evil Mad Scientist founders Lenore Edman and Windell Oskay as Bantam Tools’ COO and CTO and describes WaterColorBot as part of the lineage that led from EggBot to AxiDraw and NextDraw:

<https://content.bantamtools.com/blog/a-look-back-part-2>

The current commercial product is a useful benchmark for feature, size, usability, and price. This archive does not claim that the Bantam design or software is open source.

## Related commercial/open ecosystem

### AxiDraw / NextDraw

AxiDraw originated from the same EBB and software family. Current NextDraw hardware/software may provide useful motion-control and usability benchmarks, but it is a pen plotter rather than a drop-in watercolor system.

### EiBotBoard availability

EBB v2.7 boards continue to appear through robotics/electronics distributors. Availability and pricing should be checked at purchasing time. A genuine EBB is the lowest-risk controller for proving the archived software path.

## Community software and examples

Relevant community repositories found during the survey:

- `jrheard/madison_wcb` — MIT-licensed Python WaterColorBot control library
- `jmpinit/ebb-control` — MIT-licensed JavaScript EBB wrapper
- `techninja/etch-a-bits` — LittleBits/Etch-a-Sketch-style WaterColorBot controller through CNCServer
- `beardicus/awesome-plotters` — curated plotter ecosystem list
- `spaelectronics/eggpaint-kids` — historical RoboPaint RT derivative
- Techninja and community RoboPaint mode experiments for spiral, stipple, manual, comic, crosshatch, and templates

Most WaterColorBot-specific community projects are historical rather than maintained. They remain valuable as interaction and protocol examples.

## Community/documentation venues

Historical links include:

- WaterColorBot Google user group (`wcb-discuss`)
- WaterColorBot developer group (`wcb-developer`)
- Evil Mad Scientist forum
- Thingiverse `watercolorbot` tag
- Plotter community resources such as Plotter People and `awesome-plotters`

Activity and archive availability vary; treat these as research sources rather than support channels.

## Comparable DIY directions

A broad search finds many generic XY pen plotters and CNC/GRBL drawing machines, but fewer systems designed for autonomous watercolor handling. The differentiated work is not basic XY motion; it is:

- reliable brush lifting and pressure
- repeatable rinsing and paint loading
- palette/water layout calibration
- paint refresh policy
- wet-media timing
- spill isolation and cleaning
- interruption recovery

A GRBL-style plotter can replace the motion system, but doing so does not automatically provide WaterColorBot’s painting workflow.

## Strategic conclusion

There is room for a modern open implementation if it emphasizes:

- current CAD and commodity parts
- reproducible software installation
- safe local API boundaries
- modern OS support
- washable/removable wet components
- calibration and self-test
- open file formats and documented painting primitives

The commercial Bantam machine sets an important price/usability benchmark. A new open build should compete on modifiability, educational value, repairability, and experimentation rather than merely cloning the discontinued frame.
