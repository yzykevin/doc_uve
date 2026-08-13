# UVE_INFO: Project information and analysis

UVE_INFO provides project-aware information discovery, analysis, and reporting services.

## Information discovery

- `-info_all`: combined project information view;
- `-info_defines`: discover and summarize compile-time defines;
- `-info_git_submodule`: inspect repository and submodule information;
- `-info_uvm`: inspect UVM package structure and reusable components;
- `-info_all_testlist`: collect testlists across the project; and
- test-status and project-metadata analysis.

## Analysis and reporting

UVE_INFO supports package, class, sequence, interface, define, parameter, register, filelist, test, configuration, and consistency analysis. Results can be consumed through local report views, the VS Code extension, and project automation checks.

## Result and self-check integration

Information analysis is integrated with tool self-tests, pytest-based checks, regression result collection, report generation, and consistency review so that project status can be inspected as part of the same verification environment.
