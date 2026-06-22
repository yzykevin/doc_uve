# JasperGold Formal Verification

> Executed via `jg_run` (or `python3 jg_run`) in the project root folder.

UVE provides a dedicated entry point for JasperGold formal verification, separate from the simulation flow.

## Environment Setup

### -env_setup

Print the environment variable setup commands for JasperGold. Source the output to configure your shell.

### -env_unset

Print the commands to unset JasperGold environment variables.

## Project Configuration

### -json

Specify the project JSON config file. Default: `jg.json`.

### -name

Specify the verification task name (e.g., `my_module_fpv`).

### -top

Specify the DUT top module name.

### -lib

Specify the design library name. Default: `work`.

### -gen_jg_proj

Generate a template JSON config file with the given name.

## Design Files

### -fl

Specify the design filelist (`.f` file).

### -sva_fl

Specify the SVA / property filelist.

### -inc

Specify include directories (space-separated, repeatable).

## Formal Apps

Multiple apps can be combined in a single run.

| Option | Description |
|--------|-------------|
| `-fpv` | Formal Property Verification (default) |
| `-conn` | Connectivity Check |
| `-csr` | CSR Check |
| `-xprop` | X-propagation Check |
| `-lpv` | Low Power Verification |
| `-cdc` | Clock Domain Crossing Verification |
| `-sec` | Sequential Equivalence Checking |
| `-superlint` | Superlint (formal lint + overflow checks) |
| `-cov_app` | Coverage App (formal coverage measurement) |
| `-spv` | Security Path Verification |

## Environment Constraints

### -clock

Specify the primary clock signal.

### -reset

Specify the reset signal. Use `~` prefix for active-low (e.g., `-reset=~rst_n`).

### -assume

Specify assumption expressions. Can be repeated for multiple assumptions.

## Proof Options

### -gui

Open JasperGold in interactive GUI mode.

### -dry_run

Print the generated commands without executing.

### -regen_tcl

Force regeneration of the TCL script even if one already exists under `verif/`.

### -check

Run the result checker automatically after each formal app completes.

### -check_only

Skip the JasperGold run and only check results from a previous run. Requires `-name` and the relevant app flag(s).

### -max_jobs

Maximum number of parallel proof jobs. Default: `50`.

### -bbox_mul

Blackbox multipliers wider than N bits. Default: `0` (disabled).

### -cov

Enable coverage collection during the formal run.

## Run Directory

### -run_dir

Specify where run directories are created. Default: `work/formal` if a `work/` folder exists, otherwise `jasper_run`.

## Formal Regression

### -fl_formal

Run all formal tests listed in a formal testlist file.

Example: `-fl_formal=verif/formal/adder/formal_adder`

### -suite

Restrict the regression to only the named SUITE within the testlist.

### -gen_formal_testlist

Generate a formal testlist template for the given module name.
