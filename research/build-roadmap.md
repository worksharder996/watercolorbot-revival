# Build roadmap

## Goal

Produce a safe, serviceable prototype of an XY watercolor robot without depending on obsolete desktop software or unavailable custom parts.

## Phase 0 — freeze requirements

Decide and document:

- maximum paper size (the original WaterColorBot was oriented around small watercolor sheets; the modern Bantam machine advertises up to 9 × 12 inches)
- number and location of paint pans and rinse-water wells
- acceptable paint-zone contamination and splash containment
- accuracy, speed, noise, and cost targets
- whether the machine must be portable or classroom-safe
- macOS/Windows/Linux support targets

Exit criterion: a one-page product requirement and a bounding-box drawing.

## Phase 1 — clean-sheet mechanical model

1. Import the v2 SVG and SolidWorks material as reference geometry.
2. Re-model the frame, winches, carriage, brush holder, and cable routing in a currently supported CAD tool.
3. Replace the original flexure/flex-PCB brush mechanism if it cannot be sourced economically.
4. Design a removable, washable paint/water tray and paper registration system.
5. Produce an assembly drawing, tolerances, and an annotated BOM.

Key mechanical risks:

- cable stretch, creep, winding-radius variation, and uneven tension
- racking of the carriage
- brush pressure consistency
- water near electronics
- repeatable pan/water positions
- paint drying between strokes

Exit criterion: interference-checked CAD, costed BOM, and fabricated-motion mockup.

## Phase 2 — controller bench

Recommended first bench:

- one EBB v2.7 or compatible board
- two known-compatible bipolar stepper motors
- one brush-lift RC servo
- current-limited 6–24 V supply selected for the motors/controller
- emergency power cutoff
- USB data isolation/physical separation from the wet zone

Tests:

1. Enumerate the EBB as USB serial.
2. Query firmware version.
3. Exercise each motor independently at low current.
4. Verify mixed-axis motion and emergency stop.
5. Exercise servo positions repeatedly.
6. Run a dry coordinate-grid test before mounting a brush.

Do not place water or paint on the machine during controller bring-up.

## Phase 3 — first software path

Start with `wcb-ink` and its compatible `plotink` revision because this is the most direct preserved WaterColorBot workflow. Pin exact Inkscape, Python, and extension versions in a reproducible environment.

In parallel, prototype a small controller service around one of these routes:

- CNCServer default branch (Node >=16, SerialPort 10.5 era)
- a minimal direct serial client implementing only required EBB commands
- a modern Python client using proven EBB command patterns from `wcb-ink`

Do not start by porting the old Electron RoboPaint application; its native dependencies make it a higher-risk path.

Exit criterion: repeatable dry plotting of a calibration SVG and an automated hardware self-test.

## Phase 4 — painting behavior

Implement primitives rather than trying to reproduce RoboPaint wholesale:

- move to rinse well
- rinse/stir sequence
- wipe/blot sequence
- move to paint pan and load brush
- controlled brush-down stroke
- refresh paint after configurable path length/time
- park and safe-stop

Then add:

- palette mapping
- SVG path ordering
- wet-on-wet versus dry-layer timing
- cleaning cycles
- recovery after USB disconnect or interrupted job

Exit criterion: a repeatable multi-color test chart with no manual intervention.

## Phase 5 — safety and durability

- isolate electronics beneath covers and away from spill paths
- add drip management and replaceable absorbent barriers
- validate motor/driver temperatures at worst-case duty cycle
- provide strain relief for power, USB, motor, and servo cables
- add home/reference behavior or a deterministic manual registration procedure
- document cleaning and storage
- test material compatibility with water and pigments

Exit criterion: a documented prototype that can run a full painting cycle repeatedly and be cleaned safely.

## Phase 6 — productization decision

Before selling or distributing kits:

- choose a non-infringing product name
- complete electrical/mechanical safety review
- perform license-by-license compliance review
- publish required modified design/source material and attribution
- establish support, replacement parts, and warranty boundaries
- compare cost/performance with the Bantam Tools commercial WaterColorBot

## First prototype recommendation

Use original v2 mechanics as a reference, but do not attempt a literal clone of every custom part. Build a modern CAD/BOM package around available linear/cable components, EBB-compatible motion, and a simple direct-control software layer. Preserve RoboPaint’s workflow ideas while replacing its legacy runtime.
