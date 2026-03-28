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

## Key Options

### -testmodule

Specify the Python test module to run.

### -top

Specify the DUT top-level module name.

### -sim

Select the simulator to use.

### -seed

Specify a random seed. Default: random.

### -repeat

Repeat the test case a specified number of times.

### -wave

Enable waveform dumping.

### -cov

Enable coverage collection.

### -parameters

Pass parameters to the DUT in `NAME=VALUE` format.

## Example

```terminal
python3 run_cocotb -testmodule=test_uart -top=uart_top -sim=vcs
```
