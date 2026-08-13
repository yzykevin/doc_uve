# UVE: Universal Verification Environment

UVE is a private-project verification environment for hardware and semiconductor development. It brings commonly used verification activities into one coherent workspace, helping teams prepare projects, run simulations, execute regressions, inspect results, and manage reusable verification assets.

This public page is intentionally a product overview. It does not describe private source code, internal architecture, repository topology, implementation techniques, credentials, or confidential project information.

## What UVE provides

- **Project-oriented verification**: a consistent starting point for IP, subsystem, and larger hardware verification activities.
- **Simulation workflows**: support for common SystemVerilog/UVM and Python-based verification workflows across supported commercial and open-source simulators.
- **Regression management**: repeatable test selection, execution, result collection, rerun support, and summary reporting.
- **Formal and static verification support**: organized entry points for formal, connectivity, and related analysis workflows where the required tools are available.
- **Reusable verification assets**: shared libraries, packages, testbench helpers, interfaces, utilities, and verification components.
- **Testbench assistance**: project-aware helpers for creating or maintaining testbench-related files and verification metadata.
- **Register and documentation generation**: tools that transform structured register descriptions into commonly used hardware, verification, software, and documentation artifacts.
- **Project information and reports**: browsable summaries of verification assets, documentation, interfaces, parameters, test information, and consistency results.
- **Job and resource integration**: support for connecting verification work with local or managed compute resources and job schedulers.
- **Developer tooling**: command-line tools, local report services, repository helpers, and editor integration.
- **Architecture-level modeling**: a separate UVE capability for early exploration of hardware and system architecture before detailed RTL implementation.
- **Continuous integration support**: deployment and automation building blocks for repeatable project checks and verification tasks.

## UVE tools and companion products

The UVE project family includes several complementary tools. Their exact implementation and project-specific configuration are not part of this public overview.

### UVE command-line tools

The command-line toolset provides a unified way to discover project information, prepare environments, launch supported verification tasks, manage regressions, collect reports, and maintain project links and generated assets.

### UVE information browser

The information browser presents verification-package and project metadata in a searchable local web interface. It can help developers review classes, sequences, interfaces, parameters, defines, documentation, and consistency information without manually searching every source file.

### UVE register generator

The register generator accepts structured register descriptions and can produce selected hardware, verification, software-header, and documentation outputs. It is intended to reduce repetitive register-map work and keep related artifacts aligned.

### UVE VS Code extension

The UVE VS Code extension brings project browsing and review into the editor. It provides a project overview, documentation and file-list navigation, test and tool information, package-oriented inspection, refresh support, and project-path configuration. It is designed for local and remote development sessions and does not require a separate browser service for its main views.

### UVE architecture platform

The architecture platform supports early software-based exploration of SoC and chiplet systems. It helps teams reason about system structure, connectivity, address spaces, performance questions, and architecture-to-implementation handoff before detailed RTL work begins. This page intentionally omits proprietary component details and internal modeling methods.

### UVE project guidance

The project-guidance companion provides maintainers and developers with project-aware orientation, conventions, troubleshooting guidance, and verification-flow references. It complements general verification knowledge rather than replacing it.

### UVE CI and validation support

UVE includes reusable patterns for self-hosted source control, continuous integration, automated checks, packaging, and project-level validation. Deployment-specific settings and infrastructure details are intentionally not documented here.

## Intended users

UVE is intended for:

- hardware and semiconductor verification engineers;
- RTL, IP, subsystem, SoC, and chiplet development teams;
- engineers who combine SystemVerilog, UVM, Python, cocotb, simulation, and formal analysis;
- teams that need reusable verification infrastructure rather than isolated scripts; and
- developers who want project context available from the command line, browser, or editor.

## Public documentation boundary

This site describes capabilities at a high level only. Private implementation details, internal project organization, confidential product information, source code, credentials, service addresses, proprietary algorithms, private benchmarks, and project-specific verification data are intentionally excluded.
