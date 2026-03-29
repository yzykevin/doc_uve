# Register Generator

The register generator (`reggen`) is integrated in `uve_tools`. It takes a register description file and generates all register-related artifacts needed for both hardware and verification teams.

## Supported Input Formats

- YAML / JSON / TOML
- XLSX (Excel)
- SystemRDL
- IP-XACT

## Supported Output Types

- **UVM RAL Model** — SystemVerilog UVM register abstraction layer for testbench integration
- **SystemVerilog RTL** — synthesizable register block RTL with configurable bus interface
- **C Header** — portable C header file for embedded software / firmware access
- **Markdown Documentation** — auto-generated register reference documentation

## Supported Bus Protocols

Bus protocol and bus/address width are configurable. Supported protocols: APB, AXI4-Lite, Avalon, Wishbone.

## Format Conversion

Register description files can be converted between YAML, JSON, TOML, and XLSX formats without regenerating outputs. Config files can also be converted between formats.

## Templates

Starter templates are available in YAML, JSON, and TOML to help bootstrap a new register description file.

## Bit Field Access Types

The generator supports a comprehensive set of bit field access types: rw, ro, wo, rwtrg, rotrg, rof, rohw, wrc, wrs, rowo, rowotrg, wc, woc, ws, wos, w0c, w1c, w0s, w1s, w0t, w1t, rc, rs, w0crs, w1crs, wcrs, w0src, w1src, wsrc, rwc, rws, rwe, rwl, rwhw, w0trg, w1trg, row0trg, row1trg, wotrg, wo1, w1, counter, custom, reserved.

## Extensibility

The generator supports a plugin system for loading custom output generators.