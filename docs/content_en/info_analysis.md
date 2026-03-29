# Info Analysis

## -info_defines

Collect all the defines in design/verif folders, analyze folders/files within specified level layer.
info_defines will be created to store the information for reviewing. This will be git ignored and need to be deleted manually.
Please note: vip folder will be skipped.

review information:

- Found in design
- Found in verif

## -info_git_submodule

Show all the git repository/submodule information.

## -info_uvm

File/structures summary of xVCs according to the specified list in `config/info/uvc.info`.

## -info_all_testlist

Info about all the testlists in the test folder.

## Verification Document Template Generation

UVE supports generating structured verification document templates for both IP-level and SOC-level projects. The generated documents follow a standardized format covering all essential verification planning areas.

**IP-level template** includes:

- Author and contact information
- IP overview and version table
- Configuration registers table
- Verification strategy (approach, UVM components, reference model, coverage strategy)
- Debug notes
- Test scope with feature table and ASIC verification checklist
- Regression and coverage signoff

**SOC-level template** includes:

- Author and contact information
- SOC overview and version table
- Pre-steps checklist (environment, submodule verification)
- Required tools table
- Environment setup (submodule status, library locations, VIP versions)
- Verification strategy (EDA tool support, flow support)
- Verification plan (test case list, SOC testbench, SOC scenarios, IP-level table)
- Regression and coverage targets
- Signoff checklist
- Change log

Generated documents are placed under `doc/IP_Level/` or `doc/SOC_Level/` respectively.
