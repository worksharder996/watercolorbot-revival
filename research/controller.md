# EiBotBoard controller ecosystem

Research date: 2026-11-08.

## Why EBB matters

The EiBotBoard (EBB) was originally designed for EggBot and became the shared controller for EggBot, WaterColorBot, and early AxiDraw machines. It presents as a USB serial device and drives two bipolar stepper motors plus RC servo outputs.

Canonical documentation:

- <https://www.schmalzhaus.com/EBB/>
- <https://evil-mad.github.io/EggBot/ebb.html>
- <https://github.com/evil-mad/EggBot>

## Hardware

The documented classic board uses a PIC18F46J50 USB microcontroller and two Allegro stepper drivers. The page describes:

- 6–24 V DC motor supply
- two microstepping bipolar stepper channels
- adjustable motor current
- USB CDC/virtual serial operation
- USB HID bootloader
- RC servo/general I/O headers
- reset and programming controls

Historical EBB design archives preserved here:

- v2.1, v2.2, v2.3
- v2.5, v2.6, v2.7

The archives include combinations of Eagle schematic/board files, Gerbers, BOMs, assembly documents, PDFs, and change notes. EBB v2.4 is represented upstream by the SparkFun GitHub branch and separate PDFs rather than a complete official ZIP.

## Firmware

Current source and release history are maintained in `evil-mad/EggBot`. A historical prebuilt 2.5.4 archive is preserved under `controller/ebb-firmware/`.

The current command documentation covers firmware 3.0+ and links to legacy 2.x documentation. Firmware 3.x retains broad compatibility but introduces a future response-syntax mode and deprecates several old commands.

## Protocol

The protocol is human-readable ASCII over serial. Important command families include:

- `V` — version query
- `EM` — enable motors/microstep mode
- `SM` — timed stepper move
- `XM` — mixed-axis geometry move
- `LM`, `LT`, `L3`, `T3`, `TD` — lower-level motion primitives
- `SP`, `S2`, `TP` — pen/servo control
- `QS`, `QG`, `QE` — position/status queries
- `ES` — emergency stop
- `HM` — home/absolute move on supported firmware/configurations

The board does **not** natively consume G-code. Host software decomposes curves into timed line segments and sends EBB commands.

## Modern use considerations

- Old Windows INF/.NET instructions apply mainly to historical systems; current platforms should be tested against current firmware and USB serial behavior.
- Preserve compatibility with both 2.x and 3.x firmware if existing machines are a target.
- New host software should use current command documentation and avoid commands marked deprecated in firmware 3.x.
- Bench-test motion with motors unloaded and current limited.
- Add application-level timeout, disconnect recovery, buffer/status checks, and a physical power cutoff.

## Alternatives

A modern replacement could use another two-axis motion controller plus servo, but that creates a new protocol/software integration task. Starting with a genuine EBB or compatible board reduces uncertainty because the archived WaterColorBot software already understands its behavior.

## Preservation files

- `controller/ebb-hardware/*.zip`
- `controller/ebb-firmware/EBF_v254.zip`
- `docs/controller/EBB_main.html`
- `docs/controller/EBB_commands_current.html`
- `docs/controller/EBB_commands_legacy.html`
- `docs/controller/EBB_release_notes.html`
- `sources/controller-download-manifest.json`
