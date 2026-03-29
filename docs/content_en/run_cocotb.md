# Cocotb Simulation

`run_cocotb` is the entry point for running Python-based testbenches using the [cocotb](https://www.cocotb.org/) framework.

It supports multiple simulators and both Verilog and VHDL designs.

## Supported Simulators

- Synopsys VCS
- Cadence Xcelium
- Mentor Questa / ModelSim
- Aldec Riviera-PRO / Active-HDL
- Icarus Verilog
- Verilator
- GHDL / NVC

## Capabilities

**Test Control**
- Specify Python test module(s), individual test functions, and top-level module
- Control random seed and repeat count for randomized test campaigns

**Source File Support**
- Supports Verilog and VHDL source file lists or individual file paths
- Supports include directories for Verilog
- Supports VAMS (analog) source files for AMS simulation

**DUT Configuration**
- Pass module parameters directly (NAME=VALUE format)
- Configure HDL time unit and time precision

**Simulation Runtime**
- Pre-compile and post-run argument passthrough for each simulator phase
- Simulator plusargs support
- Configurable build directory and results output file

**Waveform Dumping**
- Enable waveform capture with support for GHW, FST, and VCD formats

**Coverage and Profiling**
- Python code coverage collection
- Call-graph profiling for performance analysis
- cocotb internals coverage for framework-level analysis

**Analog/Mixed-Signal (AMS)**
- AMS simulation support for Xcelium and VCS
- Discipline configuration for mixed-signal designs

**GPI Interface (VHDL)**
- Selectable GPI interface for VHDL designs: VPI, VHPI, or FLI
- Support for extra GPI libraries and custom PyGPI entry points

**X/Z Value Resolution**
- Configurable behavior when X/Z logic values are converted to integers: error, zeros, ones, or random

**Debug Support**
- Pause before simulation start for external debugger attachment
- Drop into Python debugger (pdb) on test exception
- HTTP memory debugging endpoint

## Example

```terminal
python3 run_cocotb -testmodule=test_uart -top=uart_top -sim=vcs
```
