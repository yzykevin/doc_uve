# Guideline for File Managing

## Creating in design folder

Please do not modify:

- design/fl/dut.f
- design/fl/dut_auto_fl/xxx_filelist.f

These files are automatically generated.

Please arrange the design files using meanful folder.

## Creating in doc folder

Please do not modify:

- doc/test_status.xlsx

These files are automatically generated.

## Creating in test folder

The base test will be extended by different tests for each module can be placed in test folder.

### Creating tests

- Various tests for one module should be place in the folder named as the module.
- The test name should be started with the module name.
- The type should be followed the module name within the test name.
- The test name should use _test.sv as the tail

For example,
xxx/xxx_aaa_sv_test.sv
xxx/xxx_aaa_sv_test.sv
xxx/xxx_bbb_ccc_sv_test.sv

### Creating testlist

> Note: Do not forget to add SUITE line no matter how many tests does a testlist file have

Test list should be created in the name format: testlist_xxx

For example, testlist_xxx

Comment should be include

- Description: (as the head)
- Each section should be seperated by ','
- Each section format: Some Topic-detailed information
- Random-xxx, Owner-xxx should be put to the tail of the comment

The example testlist_xxx can be generated using the option: `-gen_testlist`

### Creating in verif folder

Please do not modify:

- verif/tb/test_include/xxx_test_include.sv
- tb.f

These files are automatically generated.

### Creating pkg/uvc

All the component for a single module should be placed in the folder named with module name in verif/pkg folder

### Creating sequences

The sequences and sequence_library should be placed in the related module folder and in a new created folder named seqs

### Creating common things

Common things of the testbench should be placed in tb folder.

- tb/top
- tb/top_sub
- tb/tb_include
- tb/test_include
- tb/wrappers

Please keep in order and do not cause compile error to interrupt others' work

### Creating in vip folder

Please do not copy files to this folder. All the files here are generated using Synopsys VIP tool if the VIP is from Synopsys.

## Creating in tools folder

IP specified tools should be in a folder named as the module name

### result_check

This is useful for error/warning checking and related with result double check and review using pytest framework.

This will also affect the result report in websites and CI.

The check rule can be modified to be tense or loose according to various project stages.

early stage - loose
late stage - tense

Use this policy to eliminate ignored errors or leakage of checkers to gurantee the success of verification before tape-out.

There are 4 files to manage the check method.

- result_error_check
- result_error_ignore
- result_warning_check
- result_warning_ignore

"//" will be treated as comment and ignored by flow

the rules are:

- items in ignore will be ignored first
- if the text in check hit, but more specific text in ignore, more specific text will be ignored
- warning check will cause fail for the case
- each log will be treated as a single test applied for the whole rules

Please Note:

- user who want to modify this should be very careful and should be better to add and not reduce. Especially in general block.
- user can start the ignore/check with detailed description for the comment and add/modify their own items.
- Note that all the modification will affect the whole project and all the people. The test from other engineer may get fake pass
- The rule files should be reviewed several times in case to cover things should not be.
