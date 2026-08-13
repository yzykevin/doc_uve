# UVE: Universal Verification Environment

UVE is a hardware verification environment and engineering toolchain for IP, subsystem, SoC, and chiplet development. It combines reusable verification packages, project-aware automation, simulator and formal-tool flows, register and testbench generation, reporting, and architecture-level modeling in one environment.

## Verification environment

UVE provides a common project foundation for:

- IP and block-level verification;
- subsystem and SoC integration verification;
- reusable UVM environments and verification components;
- SystemVerilog, Python, cocotb, and SVUnit based tests;
- simulation, regression, coverage, debug, and result analysis; and
- early architecture and behavior-model exploration.

The environment is designed to support both day-to-day verification work and the long-term reuse of project assets across multiple designs.

## Complete verification flow

UVE connects project setup, design and testbench composition, pre-compilation, simulation, regression, coverage, result collection, debug, and reporting into one repeatable flow. The same project context can be used to prepare a run, select tests, execute on local or scheduled resources, collect logs and artifacts, and review results through terminal, report-server, or editor-based views.

The flow is intended to scale from focused IP verification to subsystem and SoC projects. It supports modular project components, reusable examples, configurable tool adapters, and the ability to add or replace flow stages as project needs evolve.

## UVE toolchain

The UVE toolchain brings the main verification activities under a consistent set of project-oriented tools.

### Project preparation and management

- project initialization and environment preparation;
- shell environment setup and cleanup;
- project configuration and flow selection;
- design and test file-list management;
- repository and submodule maintenance;
- generated-file and workspace cleanup;
- project consistency checks; and
- shared-library and tool-version management.

### Simulation flows

The simulation flow supports the major stages of a hardware verification run:

- source and file-list preparation;
- compilation and elaboration;
- test execution;
- random seed and repeat control;
- waveform generation and GUI/debug modes;
- functional and code-coverage collection;
- configurable DUT and testbench composition; and
- reusable flow configuration for different projects.

### Supported simulator families

Depending on the project and installed licenses, UVE supports integrations with:

- Synopsys VCS;
- Cadence Xcelium;
- Icarus Verilog;
- Verilator; and
- other project-configured open-source simulators.

The toolchain keeps simulator-specific details behind project flow configuration while preserving common concepts for compilation, execution, results, and debugging.

### Python and cocotb verification

UVE also supports Python-driven verification with cocotb and pyuvm-oriented environments. The flow covers test-module selection, top-level selection, simulator integration, seed handling, pre-compilation, regression execution, and result collection for supported simulators. This allows teams to use Python verification alongside SystemVerilog and UVM environments.

### SVUnit and unit-level verification

The SVUnit flow provides unit-test discovery, test scaffolding, execution, cleanup, and workspace organization for focused SystemVerilog verification. It complements broader UVM and regression flows by making small, fast tests easy to maintain.

### Regression and coverage

Regression capabilities include:

- testlist-driven execution;
- parallel case scheduling;
- VCS and Xcelium regression variants;
- failed-test collection and rerun;
- waveform-enabled debug reruns;
- pass/fail summaries;
- result-check analysis;
- HTML reporting;
- log and case navigation; and
- disk-space-conscious cleanup of completed results.

Coverage support includes common line, condition, toggle, FSM, branch, assertion, and functional-coverage workflows where supported by the selected simulator and project configuration.

### Formal, static, and mutation-oriented flows

UVE provides project entry points for formal and related analysis workflows, including JasperGold-based applications such as:

- formal property verification;
- connectivity and structural checks;
- security-oriented analysis;
- sequential-equivalence analysis; and
- lint and quality-oriented checks.

The environment also includes support for Certitude-oriented mutation and fault-analysis workflows, including generated filelists, simulator scripts, and result cleanup.

### Pre-compilation and result collection

Common pre-compilation assets, generated filelists, compiled libraries, testbench artifacts, and tool-specific run products can be managed as part of the project flow. Verification and tool self-checks can be exercised through automated tests, with pytest-based collection and presentation of simulation, regression, and utility results.

### SoC integration and automatic connectivity

UVE supports SoC-level environment assembly through reusable design and verification components, configurable interfaces, project metadata, and automatic connectivity assistance. This helps teams compose environments at different scales, connect common blocks and wrappers, and move from individual IP validation toward integrated subsystem and SoC verification.

### Job scheduling and reporting

Verification jobs can be connected to managed compute resources through scheduler-aware flows. UVE includes integration patterns for Slurm and LSF, together with local execution for smaller tasks. Report services provide searchable summaries of tests, logs, results, coverage information, and project status.

## `uve_ip`: Reusable Design IP library

UVE includes a growing library of reusable design IP and integration examples. The library is intended to provide consistent starting points for common SoC functions and to make those functions available to both design and verification flows.

Current design-IP areas include:

- always-on and low-power timer functions;
- general-purpose timers and watchdog functions;
- UART, SPI, I2C, GPIO, mailbox, and interrupt-control peripherals;
- clock, reset, power-management, and pin-multiplexing support;
- debug control, debug status, debug locks, JTAG, and debug-bus access;
- error management and firewall/access-control functions;
- PMU and SoC information services;
- AXI/APB bridge and peripheral integration functions;
- NoC management and system-control functions;
- boot-ROM and startup support;
- DSP and selected AI/NPU-oriented blocks; and
- SoC-level integration examples and reference assemblies.

The design-IP library is developed with verification, register descriptions, documentation, and integration support in mind so that a block can be evaluated as part of a complete project rather than as an isolated source tree.

### Design IP catalog

The current self-developed Design IP catalog includes:

| IP | Overview |
|---|---|
| `uve_uart` | UART peripheral and verification-ready integration support. |
| `uve_spi_host` | SPI host peripheral. |
| `uve_i2c` | I2C controller peripheral. |
| `uve_gpio` | General-purpose I/O peripheral. |
| `uve_mailbox` | Mailbox and message-passing support. |
| `uve_intc` | Interrupt-control and interrupt-routing support. |
| `uve_aon_timer` | Always-on timer function. |
| `uve_timer` | General-purpose timer function. |
| `uve_clk_mgr` | Clock-management support. |
| `uve_reset_mgr` | Reset-management support. |
| `uve_pmu` | Power-management support. |
| `uve_pinmux` | Pin-multiplexing support. |
| `uve_boot_rom` | Boot-ROM and startup support. |
| `uve_soc_info` | SoC information and identification support. |
| `uve_axi_apb_bridge` | AXI/APB bridge and integration support. |
| `uve_noc_mgmt` | NoC management and system-control support. |
| `uve_firewall` | Access-control and firewall support. |
| `uve_errmgr` | Error-management support. |
| `uve_debug_ctrl` | Debug-control support. |
| `uve_debug_status` | Debug-status and observability support. |
| `uve_debug_lock` | Debug-access lock and protection support. |
| `uve_debug_bus_gate` | Debug-bus access-gating support. |
| `uve_jtag_tap` | JTAG tap and debug connectivity support. |
| `uve_dsp` | DSP-oriented processing support. |
| `fly_npu` | AI/NPU-oriented processing support under active development. |

The catalog is extended as new reusable blocks and integration examples mature.

### Protocol IP and configurable wrappers

The IP direction includes reusable protocol-oriented building blocks and configurable wrappers for interfaces such as AXI4-Lite and APB. Wrapper configuration allows the same integration concept to be adapted to different project contexts without requiring every project to rebuild the surrounding infrastructure.

## `uve_pkg`: Reusable verification package library

The UVE verification package library provides reusable SystemVerilog/UVM infrastructure for common verification concerns, including:

- base and common utilities;
- environment and phase management;
- clock, reset, synchronization, and pin-level support;
- interrupt handling;
- DMA and memory-oriented verification;
- error injection;
- performance measurement and reporting;
- object pools and reusable transactions;
- register-model utilities;
- protocol-oriented register support for AHB, APB, AXI, AXI-Stream, I2C, OCP, SPI, and UART; and
- verification reports and shared helper services.

The `uve_pkg` library provides the general-purpose verification foundation. It is complemented by a separate protocol package family described below.

### `uve_pkg` package catalog

The current reusable package set includes:

| Package | Overview |
|---|---|
| `uve_base_pkg` | Base verification services and common foundations. |
| `uve_common_pkg` | Shared verification utilities and common types. |
| `uve_utils_pkg` | General-purpose verification helpers. |
| `uve_env_pkg` | Reusable environment-level support. |
| `uve_phase_pkg` | Verification phase and lifecycle support. |
| `uve_clk_pkg` | Clock-related verification support. |
| `uve_reset_pkg` | Reset-related verification support. |
| `uve_sync_pkg` | Synchronization-related verification support. |
| `uve_pins_pkg` | Pin-level verification support. |
| `uve_interrupt_pkg` | Interrupt verification services. |
| `uve_dma_pkg` | DMA-oriented verification support. |
| `uve_memory_pkg` | Memory-oriented verification support. |
| `uve_error_injection_pkg` | Error-injection and negative-testing support. |
| `uve_performance_pkg` | Performance measurement and analysis support. |
| `uve_report_pkg` | Verification result and report support. |
| `uve_obj_pool_pkg` | Reusable object and transaction-pool support. |
| `uve_reg_utils_pkg` | Register-model utilities. |
| `uve_reg_ahb_pkg` | AHB register verification support. |
| `uve_reg_apb_pkg` | APB register verification support. |
| `uve_reg_axi_pkg` | AXI register verification support. |
| `uve_reg_axis_pkg` | AXI-Stream register verification support. |
| `uve_reg_i2c_pkg` | I2C register verification support. |
| `uve_reg_ocp_pkg` | OCP register verification support. |
| `uve_reg_spi_pkg` | SPI register verification support. |
| `uve_reg_uart_pkg` | UART register verification support. |
The package catalog is designed for composition: teams can start with common services, add protocol packages, and extend the environment with project-specific verification components.

## `uve_protocol_pkg`: Reusable protocol verification package library

The `uve_protocol_pkg` family provides reusable verification components for common interfaces and protocols. It is separated from the general `uve_pkg` foundation so protocol-specific agents and services can be adopted independently.

| Package | Overview |
|---|---|
| `uve_protocol_pkg` | Protocol-focused reusable verification package family. |
| `uve_i2c_pkg` | Reusable I2C verification components. |
| `uve_spi_pkg` | Reusable SPI verification components. |
| `uve_uart_pkg` | Reusable UART verification components. |

### Verification IP and VIP direction

UVE is developing a reusable verification-component and VIP library for common protocols and interface behaviors. The goal is to provide configurable agents, monitors, drivers, scoreboards, sequences, protocol checks, and reusable verification services that can be composed across projects.

## UVE behavioral model library

UVE includes a behavioral model library for simulation-oriented verification and system behavior studies. The models provide reusable representations of common processing, interconnect, memory, peripheral, security, and connectivity behavior for use alongside verification environments.

Model and component areas include:

- RISC-V CPU and processor wrappers;
- interconnect, crossbar, arbitration, and NoC models;
- memory and memory-controller models, including DDR and HBM-oriented studies;
- chiplet and die-to-die connectivity models;
- PCIe, Ethernet, CXL, and other high-speed connectivity abstractions;
- UART, SPI, I2C, GPIO, timer, watchdog, RTC, and interrupt peripherals;
- clock and power-management behavior;
- security, root-of-trust, secure-boot, and access-filter modeling;
- telemetry and transaction-observation components; and
- AI accelerator and NPU-oriented architecture exploration.

The behavioral model library supports simulation, integration experiments, software-visible behavior checks, and reusable system-level verification scenarios.

### Behavioral model catalog

The architecture and behavioral model platform currently includes the following model families:

| Model family | Overview |
|---|---|
| CPU behavior models | Processor and CPU-wrapper behavior for simulation and integration studies. |
| Interconnect behavior models | Crossbar, arbitration, and system-interconnect behavior. |
| Memory behavior models | DDR/HBM-oriented memory behavior. |
| Peripheral behavior models | UART, SPI, I2C, GPIO, timer, watchdog, RTC, and interrupt behavior. |
| Connectivity behavior models | PCIe, Ethernet, CXL, and related connectivity behavior. |
| Security behavior models | Root-of-trust, secure-boot, and access-control behavior. |
| Telemetry behavior models | Passive observation and transaction-telemetry behavior. |
| AI behavior models | AI accelerator and NPU-oriented behavior. |

## `uve_arch`: Architecture exploration and performance platform

`uve_arch` is based on SystemC and Accellera ecosystem technologies and supports architecture exploration, system design studies, integration validation, and performance analysis before detailed RTL implementation. Its model families cover:

| Architecture model family | Overview |
|---|---|
| CPU architecture models | RISC-V processor and CPU-wrapper architecture studies. |
| Interconnect and NoC models | Crossbar, arbitration, NoC, and topology studies. |
| Memory-system models | DDR/HBM and memory-controller performance studies. |
| Chiplet and die-to-die models | Chiplet connectivity and system-integration studies. |
| High-speed fabric models | PCIe, Ethernet, and CXL architecture studies. |
| Peripheral-system models | UART, SPI, I2C, GPIO, timer, watchdog, RTC, and interrupt integration. |
| Clock, power, and security models | Clock/power sequencing, root-of-trust, secure-boot, and access-control studies. |
| AI/NPU architecture models | AI accelerator and NPU system exploration. |

The architecture flow is being extended toward complete system studies, software-visible behavior, Linux boot, and architecture-to-RTL validation.

## Register and testbench generation

UVE provides generators that turn structured descriptions into consistent project artifacts.

### Register generation

The register generator supports common structured inputs such as YAML, JSON, TOML, and spreadsheet-based descriptions, with conversion support for additional industry formats where configured. It can produce:

- UVM register-abstraction models;
- SystemVerilog register RTL;
- C headers for software access;
- Markdown register documentation; and
- converted or normalized register descriptions.

It supports common bus-oriented configurations, address and data-width settings, arrays, aliases, indirect registers, and a broad set of field access behaviors.

### Testbench and UVM generation

Generation utilities assist with creating:

- DUT and HVL top-level scaffolding;
- testbench includes and filelists;
- testlist templates;
- base tests;
- UVM agent, environment, register, and sequence-library templates; and
- format-conversion templates for project configuration.

These generators provide repeatable starting points while leaving the project team in control of the final verification architecture and implementation.

Generation is designed to be composable: projects can combine generated configuration, testbench, register, coverage, Jasper, report, and statistical-analysis artifacts with hand-written project content.

## Project information and analysis

UVE provides tools for turning project metadata into useful engineering views and reports.

Capabilities include:

- package and component discovery;
- UVM class, sequence, interface, define, and parameter inspection;
- README and documentation rendering;
- testlist and test-status analysis;
- design and register summaries;
- filelist and configuration inspection;
- tool and environment information;
- consistency checks across related descriptions; and
- local report-server views for browsing project information.

## UVE VS Code extension

The UVE VS Code extension brings project exploration and review into the editor. It provides:

- a project overview and navigation hub;
- design, sub-project, filelist, and documentation views;
- toolchain and environment inspection;
- test status and regression views;
- package classes, sequences, interfaces, defines, parameters, and consistency views;
- register and design-analysis views;
- project configuration editing and refresh;
- local and remote development support; and
- an integrated UVE User Guide for the complete project operation reference.

## Continuous integration and project automation

UVE includes project automation capabilities for:

- source-control and code-review workflows;
- continuous integration execution;
- automated lint, test, and packaging checks;
- reproducible tool and environment setup;
- artifact and report generation; and
- validation of project-level changes.

These capabilities support both individual development and repeatable team-level verification.

The CI/CD environment is built around Forgejo and Woodpecker workflows and is intended to support multi-project collaboration, automated validation, packaging, artifact publication, and repeatable engineering checks.

## Ongoing development

UVE is under continuous development.
