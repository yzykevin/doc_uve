# 2.6 Regression and coverage

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

## Formal, static, and mutation-oriented flows

UVE provides project entry points for formal and related analysis workflows, including JasperGold-based applications such as:

- formal property verification;
- connectivity and structural checks;
- security-oriented analysis;
- sequential-equivalence analysis; and
- lint and quality-oriented checks.

The environment also includes support for Certitude-oriented mutation and fault-analysis workflows, including generated filelists, simulator scripts, and result cleanup.

## Pre-compilation and result collection

Common pre-compilation assets, generated filelists, compiled libraries, testbench artifacts, and tool-specific run products can be managed as part of the project flow. Verification and tool self-checks can be exercised through automated tests, with pytest-based collection and presentation of simulation, regression, and utility results.

## SoC integration and automatic connectivity

UVE supports SoC-level environment assembly through reusable design and verification components, configurable interfaces, project metadata, and automatic connectivity assistance. This helps teams compose environments at different scales, connect common blocks and wrappers, and move from individual IP validation toward integrated subsystem and SoC verification.

## Job scheduling and reporting

Verification jobs can be connected to managed compute resources through scheduler-aware flows. UVE includes integration patterns for Slurm and LSF, together with local execution for smaller tasks. Report services provide searchable summaries of tests, logs, results, coverage information, and project status.
