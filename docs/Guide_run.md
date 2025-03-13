# The Guide of run

- [The Guide of run](#the-guide-of-run)
  - [Author](#author)
  - [General Options for single simulation](#general-options-for-single-simulation)
    - [-h/--help](#-h--help)
    - [-env\_setup](#-env_setup)
    - [-env\_unset](#-env_unset)
  - [Running single simulation](#running-single-simulation)
    - [-check](#-check)
    - [-tool](#-tool)
    - [-list](#-list)
    - [-auto\_dut](#-auto_dut)
    - [-auto\_tb](#-auto_tb)
    - [-manual\_dut](#-manual_dut)
    - [-manual\_tb](#-manual_tb)
    - [-run\_folder](#-run_folder)
    - [-name](#-name)
    - [-s\_run](#-s_run)
    - [-s\_com](#-s_com)
    - [-s\_dut](#-s_dut)
    - [-s\_tb](#-s_tb)
    - [-s\_sim](#-s_sim)
    - [-s\_part\_comp](#-s_part_comp)
    - [-base\_dut](#-base_dut)
    - [-base\_tb](#-base_tb)
    - [-c\_run](#-c_run)
    - [-c\_com](#-c_com)
    - [-c\_dut](#-c_dut)
    - [-c\_tb](#-c_tb)
    - [-c\_sim](#-c_sim)
    - [-dump\_scope](#-dump_scope)
    - [-prerun](#-prerun)
    - [-postrun](#-postrun)
    - [-define](#-define)
    - [-tpa](#-tpa)
    - [-vpa](#-vpa)
    - [-seed](#-seed)
    - [-repeat](#-repeat)
    - [-wave](#-wave)
    - [-cov](#-cov)
    - [-svlib](#-svlib)
  - [Running Regression](#running-regression)
    - [Display in terminal](#display-in-terminal)
    - [General Options for regression](#general-options-for-regression)
      - [-s\_regress2](#-s_regress2)
      - [-s\_regress3](#-s_regress3)
      - [-c\_regress1](#-c_regress1)
      - [-c\_regress3](#-c_regress3)
      - [-reg\_num](#-reg_num)
      - [-suite](#-suite)
      - [-rm\_pass](#-rm_pass)
      - [-rerun](#-rerun)
    - [rerun\_for options](#rerun_for-options)
      - [-s\_rerun2\_for](#-s_rerun2_for)
      - [-s\_rerun3\_for](#-s_rerun3_for)
      - [-c\_rerun1\_for](#-c_rerun1_for)
      - [-c\_rerun3\_for](#-c_rerun3_for)
  - [Job Scheduler](#job-scheduler)
    - [-job](#-job)
    - [-lsf\_q](#-lsf_q)
    - [-slurm\_q](#-slurm_q)
    - [-slurm\_mem](#-slurm_mem)
  - [JSON for projects](#json-for-projects)
    - [-json](#-json)
    - [-json\_extra](#-json_extra)
  - [Other Options](#other-options)
    - [-report](#-report)
    - [-clean](#-clean)
    - [-debug](#-debug)
    - [-git\_update](#-git_update)
    - [-gen\_test\_status](#-gen_test_status)
    - [-check\_git\_clean](#-check_git_clean)
    - [-info\_defines](#-info_defines)
    - [-info\_git\_submodule](#-info_git_submodule)
    - [-info\_uvm](#-info_uvm)
    - [-info\_all\_testlist](#-info_all_testlist)
  - [Examples](#examples)
    - [Setup Environment](#setup-environment)
    - [Generate Filelist](#generate-filelist)
    - [Run Simulation with Synopsys Tool](#run-simulation-with-synopsys-tool)
    - [Run Regression with Cadence Tool](#run-regression-with-cadence-tool)
    - [Clean Root Folder](#clean-root-folder)
  - [Contributing](#contributing)
  - [License](#license)

## Author

Zhenyu Yan (Kevin)  
Contact: <yzykevin@gmail.com>

## General Options for single simulation

The run should be used in the root folder of the cloned repo!

### -h/--help

Show help message, descriptions of the options.

### -env_setup

Automatically setup the needed environment variables according to your shell type.

Supported shells:

- bash
- tcsh

### -env_unset

Unset all environment variables related to uve_tools.

## Running single simulation

To run a single test, the test folder will be created in the run folder using the test name and seed combination. There is a slight difference between the 2-step and 3-step flow.

### -check

check the testlist before simulation/regression, help to found errors in very early stage.

eg. -check=./verif/test/ap_if/testlist_ap_if

### -tool

Select the tool to use: Synopsys VCS (`snps`) or Cadence XRUN (`cdns`). Default is `snps`.

### -list

Automatically generate filelist.f in rtl folder, which will be used for testbench.

The filelist.f will include all .v file with the absolute path of the cloned repo. Please make sure the rtl file folder clean and does not contain unused files.

To use this, the following is needed:

1. make the xxx folder, put all design files into the xxx folder
2. add the xxx name to design/dut_auto_filelist/dut_auto_filelist
3. python3 run -auto_dut=xxx
4. xxx_filelist.f will be generated in design/dut_auto_filelist/

eg. -list

The xxx_filelist.f will be generated into design/dut_auto_filelist, which will include all existed file path.

The list can be found and managed in design/dut_auto_filelist/dut_auto_filelist.

This automatically specification method will automatically find the files in the provided named folder.

### -auto_dut

Automatically generate dut.f in rtl folder for each rtl module, which will be used for testbench.

To use this, the following is needed:

1. based on -list generation, provide xxx from the list: design/dut_auto_filelist/dut_auto_filelist
2. python3 run -auto_dut=xxx
3. dut.f will be generated in design/

### -auto_tb

Automatically generate tb.f in verif folder, which will be used for testbench.

To use this, the following is needed:

1. prepare the xxx filelist in verif/tb_auto_filelist/
2. python3 run -auto_tb=xxx
3. tb.f will be generated in verif/

Plus,

Automatically generate test_include.sv in verif/tb folder, which will include all tests found in verif/test/ and be used for testbench.

The tb.f will include all exist verif/folder, vip folder, test/xxx folder path to be +incdir+ in the testbench.

### -manual_dut

Specify the manually written dut filelist to simulate.

The filelists should be prepared and managed in the relative root folder design/dut_flist/

-manual_dut=xxx_flist.f, design/dut_flist/xxx_flist.f will be used as the dut.f

### -manual_tb

Specify the manually written tb filelist to simulate.

The filelists should be prepared and managed in the relative root folder verif/tb_flist/

-manual_tb=xxx_flist.f, verif/tb_flist/xxx_flist.f will be used as the tb.f

### -run_folder

Specify the run folder. Default is `work`.

### -name

Specify the test name.

eg. -name=xxx_test

### -s_run

Choose the run method for Synopsys tool: `step2`, `step3`, or `none`. Default is `none`.

> Please note that if 3-step run is used, the dut/tb compiling folder will not be refreshed automatically! If the dut/tb is updated, the compiled folder should be cleaned and rerun the 3-step run to use the updated things.
> If the case is in developing stage, it is recomended to use 2-step run, -s_run=step2

### -s_com

Compile only using VCS 2-step method.

### -s_dut

Compile DUT using VCS 3-step method.

### -s_tb

Compile testbench using VCS 3-step method.

### -s_sim

Execute simulation using VCS 3-step method.

### -s_part_comp

Synopsys tool partition compile method: `auto`, `manual`, or `no`. Default is `no`.

do the manual partition,decrease compile time,but must combine json_extra to pass the cfg.v, which can be found in example: uve_extra.json

### -base_dut

Specify the base_dut, always use this with related -flist_dut specified. skip dut compiling, use the base_dut specified dut compiling database

eg. -base_dut=xxx, PROJECT_NAME_xxx will created and compiled. default will use PROJECT_NAME as the compiling folder

### -base_tb

Specify the base_tb, skip tb compiling, use the base_tb specified tb compiling database

eg. -base_tb=xxx_xxx_test

### -c_run

Choose the run method for Cadence tool: `step1`, `step3`, or `none`. Default is `none`.

### -c_com

Compile only using XRUN 1-step method.

### -c_dut

Compile DUT using XRUN 3-step method.

### -c_tb

Compile testbench using XRUN 3-step method.

### -c_sim

Execute simulation using XRUN 3-step method.

### -dump_scope

Specify the dump scope of the waveform. Default is `verif/test/common/dump_scope.txt`.

### -prerun

Prerun any command/script before simulation, which should be passed with -prerun=""

### -postrun

Postrun any command/script after simulation, which should be passed with -postrun=""

### -define

Pass defines to simulation, the options should be used as -define="".

eg. -define="aaa", -define="aaa bbb ccc"

### -tpa

Pass test plugsargs to simulation, the options should be used as -tpa="".

eg. -tpa="+aaa, +bbb"

### -vpa

Pass value plugsargs to simulation, the options should be used as -vpa="".

eg. -tpa="+aaa=xxx, +bbb=yyy"

### -seed

Pass seed to simulation. Default seed is random.

### -repeat

Pass repeat times for one case to simulation. Default is 1.

### -wave

Pass wave dump to simulation. Options: `fsdb`, `vpd`, `shm`.

### -cov

Pass coverage collecting to simulation. Options: `all` or specified types (e.g., `line,tgl,fsm,branch,cond,assert`).

### -svlib

Enable `svlib` so related functions/tasks can be used. (needed folder/files must be exist)

## Running Regression

To run a regression of all tests in a testlist, the regression folder will be created in run folder using regression and runing date/time conbination

The test with seed combination folder will be created in the regression_ folder.

The options in each test command in testlist will be ignored:

- -wave
- -seed

These options can be passed within the command of the regression.

Note that if there is -repeat option in single test command, -seed will be ignored and random seed will be used in -repeat times

eg.

VCS 3-step command

```terminal
python3 run -s_regress3=test/ap_if/testlist_ap_if -reg_num=8 -wave=fsdb -seed=100
```

VCS 2-step command

```terminal
python3 run -s_regress2=test/ap_if/testlist_ap_if -reg_num=8 -wave=fsdb -seed=100
```

Please note that if all regression is run with waveform open, the size of the result folder will be large, which may consume too much disk space.

### Display in terminal

All the information will show with *COLOR*.

The information will show:

- the main program process PID
- the parallel running process number
- total running case number
- total cpu count of the current server
- regression location in run folder
- running test
  - name
  - PID
  - starting date/time
- finishing test
  - name
  - finishing date/time
  - duration time
- successfully finished test (test may stuck, this will not show)
- test rough result PASSED/FAILED
- test result report file location

eg.

```terminal
❯ python3 run -s_regress3=test/ap_if/testlist_ap_if -reg_num=8

ID of main process: 125289
The parallel running tests number is: 8
--------------------------------------------------------------
Regression of test/ap_if/testlist_ap_if. Total Case is: 17
The number of CPU is: 96
Regression location is: regression_2022_12_09_10_08_48
--------------------------------------------------------------
Running test: ap_if_sv_multi_frame_full_1600x1600_vip_test                  PID: 125296         start@2022_12_09_10_08_49    
Running test: ap_if_sv_single_frame_full_1600x1600_test                     PID: 125302         start@2022_12_09_10_08_49    
Running test: ap_if_sv_multi_frame_short_1600x16_vip_test                   PID: 125307         start@2022_12_09_10_08_49    
Running test: ap_if_sv_single_frame_short_1600x16_test                      PID: 125316         start@2022_12_09_10_08_49    
Running test: ap_if_sv_single_frame_full_1600x1600_vip_test                 PID: 125318         start@2022_12_09_10_08_49    
Running test: ap_if_sv_multi_frame_short_1600x16_test                       PID: 125319         start@2022_12_09_10_08_49    
Running test: ap_if_sv_single_frame_short_1600x16_vip_test                  PID: 125320         start@2022_12_09_10_08_50    
Running test: ap_if_sv_multi_frame_hw_sync_1600x16_vip_test                 PID: 125324         start@2022_12_09_10_08_50    
!!!Done test: ap_if_sv_multi_frame_short_1600x16_test                                           finish@2022_12_09_10_09_27   Duration: 00:00:37            
Running test: ap_if_sv_multi_frame_full_1344x1344_test                      PID: 125319         start@2022_12_09_10_09_27    
!!!Done test: ap_if_sv_single_frame_short_1600x16_test                                          finish@2022_12_09_10_09_28   Duration: 00:00:38            
Running test: ap_if_sv_multi_frame_full_1344x1344_vip_test                  PID: 125316         start@2022_12_09_10_09_28    
!!!Done test: ap_if_sv_multi_frame_short_1600x16_vip_test                                       finish@2022_12_09_10_12_46   Duration: 00:03:56            
Running test: ap_if_sv_multi_frame_short_1344x16_test                       PID: 125307         start@2022_12_09_10_12_46    
!!!Done test: ap_if_sv_multi_frame_hw_sync_1600x16_vip_test                                     finish@2022_12_09_10_12_46   Duration: 00:03:56            
Running test: ap_if_sv_multi_frame_short_1344x16_vip_test                   PID: 125324         start@2022_12_09_10_12_46    
!!!Done test: ap_if_sv_single_frame_short_1600x16_vip_test                                      finish@2022_12_09_10_12_47   Duration: 00:03:57            
Running test: ap_if_sv_single_frame_full_1344x1344_test                     PID: 125320         start@2022_12_09_10_12_47    
!!!Done test: ap_if_sv_multi_frame_short_1344x16_test                                           finish@2022_12_09_10_13_10   Duration: 00:00:24            
Running test: ap_if_sv_single_frame_full_1344x1344_vip_test                 PID: 125307         start@2022_12_09_10_13_10    
!!!Done test: ap_if_sv_multi_frame_short_1344x16_vip_test                                       finish@2022_12_09_10_15_39   Duration: 00:02:53            
Running test: ap_if_sv_single_frame_short_1344x16_test                      PID: 125324         start@2022_12_09_10_15_39    
!!!Done test: ap_if_sv_multi_frame_full_1344x1344_test                                          finish@2022_12_09_10_15_56   Duration: 00:06:28            
Running test: ap_if_sv_single_frame_short_1344x16_vip_test                  PID: 125319         start@2022_12_09_10_15_56    
!!!Done test: ap_if_sv_single_frame_short_1344x16_test                                          finish@2022_12_09_10_16_05   Duration: 00:00:26            
Running test: ap_if_sv_multi_frame_full_1600x1600_test                      PID: 125324         start@2022_12_09_10_16_05    
!!!Done test: ap_if_sv_single_frame_full_1600x1600_test                                         finish@2022_12_09_10_17_59   Duration: 00:09:09            
!!!Done test: ap_if_sv_single_frame_full_1344x1344_test                                         finish@2022_12_09_10_18_33   Duration: 00:05:46            
!!!Done test: ap_if_sv_single_frame_short_1344x16_vip_test                                      finish@2022_12_09_10_18_53   Duration: 00:02:57            
!!!Done test: ap_if_sv_multi_frame_full_1344x1344_vip_test                                      finish@2022_12_09_10_24_02   Duration: 00:14:34            
!!!Done test: ap_if_sv_multi_frame_full_1600x1600_test                                          finish@2022_12_09_10_24_23   Duration: 00:08:17            
!!!Done test: ap_if_sv_single_frame_full_1344x1344_vip_test                                     finish@2022_12_09_10_26_54   Duration: 00:13:43            
!!!Done test: ap_if_sv_multi_frame_full_1600x1600_vip_test                                      finish@2022_12_09_10_28_45   Duration: 00:19:55            
!!!Done test: ap_if_sv_single_frame_full_1600x1600_vip_test                                     finish@2022_12_09_10_28_46   Duration: 00:19:56            
----------------
Finished test count: 17
Successfully Finished Test: ap_if_sv_multi_frame_short_1600x16_test
Successfully Finished Test: ap_if_sv_single_frame_short_1600x16_test
Successfully Finished Test: ap_if_sv_multi_frame_short_1600x16_vip_test
Successfully Finished Test: ap_if_sv_multi_frame_hw_sync_1600x16_vip_test
Successfully Finished Test: ap_if_sv_single_frame_short_1600x16_vip_test
Successfully Finished Test: ap_if_sv_multi_frame_short_1344x16_test
Successfully Finished Test: ap_if_sv_multi_frame_short_1344x16_vip_test
Successfully Finished Test: ap_if_sv_multi_frame_full_1344x1344_test
Successfully Finished Test: ap_if_sv_single_frame_short_1344x16_test
Successfully Finished Test: ap_if_sv_single_frame_full_1600x1600_test
Successfully Finished Test: ap_if_sv_single_frame_full_1344x1344_test
Successfully Finished Test: ap_if_sv_single_frame_short_1344x16_vip_test
Successfully Finished Test: ap_if_sv_multi_frame_full_1344x1344_vip_test
Successfully Finished Test: ap_if_sv_multi_frame_full_1600x1600_test
Successfully Finished Test: ap_if_sv_single_frame_full_1344x1344_vip_test
Successfully Finished Test: ap_if_sv_multi_frame_full_1600x1600_vip_test
Successfully Finished Test: ap_if_sv_single_frame_full_1600x1600_vip_test
testname is: ap_if_sv_multi_frame_full_1600x1600_vip_test_1425870750                      PASSED     
testname is: ap_if_sv_single_frame_full_1600x1600_test_1425870750                         PASSED     
testname is: ap_if_sv_multi_frame_short_1600x16_vip_test_1425870750                       PASSED     
testname is: ap_if_sv_single_frame_short_1600x16_test_1425870750                          PASSED     
testname is: ap_if_sv_single_frame_full_1600x1600_vip_test_1425870750                     PASSED     
testname is: ap_if_sv_multi_frame_short_1600x16_test_1425870750                           PASSED     
testname is: ap_if_sv_single_frame_short_1600x16_vip_test_1425870750                      PASSED     
testname is: ap_if_sv_multi_frame_hw_sync_1600x16_vip_test_1425870750                     PASSED     
testname is: ap_if_sv_multi_frame_full_1344x1344_test_1425870750                          PASSED     
testname is: ap_if_sv_multi_frame_full_1344x1344_vip_test_1425870750                      PASSED     
testname is: ap_if_sv_multi_frame_short_1344x16_test_1425870750                           PASSED     
testname is: ap_if_sv_multi_frame_short_1344x16_vip_test_1425870750                       PASSED     
testname is: ap_if_sv_single_frame_full_1344x1344_test_1425870750                         PASSED     
testname is: ap_if_sv_single_frame_full_1344x1344_vip_test_1425870750                     PASSED     
testname is: ap_if_sv_single_frame_short_1344x16_test_1425870750                          PASSED     
testname is: ap_if_sv_single_frame_short_1344x16_vip_test_1425870750                      PASSED     
testname is: ap_if_sv_multi_frame_full_1600x1600_test_1425870750                          PASSED     
-----------------------------------------------------
Result Report: /proj/path/kevin/ap_if/run/regression_2025_12_09_10_08_48/reg_result
The regression is finished.
Regression location is: regression_2025_12_09_10_08_48
-----------------------------------------------------
```

### General Options for regression

#### -s_regress2

Do regression with provided testlist using VCS 2-step method.

#### -s_regress3

Do regression with provided testlist using VCS 3-step method.

#### -c_regress1

Do regression with provided testlist using XRUN 1-step method.

#### -c_regress3

Do regression with provided testlist using XRUN 3-step method.

#### -reg_num

Pass the parallel number of regression. Default is 5.

Please do not set the num too large to hang the server.

The parallel running is using multiple process in a single server. More number will cause faster regression time but higher system resource comsumption. So please provide a reasonable num and make sure not to disturb other engineers' work.

this can be used combined with -lsf/-slurm.

#### -suite

Do regression with provided suite in the testlist.

eg. testlist

```testlist
SUITE BASE ----------------

//Description: IP-AP_IF, Frames-2, Resolution-1344x16, Random-Pic data, Owner-Kevin, Status-Done
run -s_run=step2 -name=ap_if_sv_multi_frame_short_1344x16_test -auto_dut=ap_if -auto_tb=ap_if -define="VRF_AP_IF" -vpa="+ap_if_frame_num=2 +resolution_left=1344 +resolution_right=16" -base_tb=ap_if_sv_single_frame_short_1344x16_test -wave=fsdb -seed=100 -json_extra=verification_extra.json

//Description: IP-AP_IF, Frames-2, Resolution-1344x16, base_dut-second, Random-Pic data, Owner-Kevin, Status-Done
run -s_run=step2 -name=ap_if_sv_multi_frame_short_1344x16_test -auto_dut=ap_if -auto_tb=ap_if -define="VRF_AP_IF" -vpa="+ap_if_frame_num=2 +resolution_left=1344 +resolution_right=16" -base_tb=ap_if_sv_single_frame_short_1344x16_test -wave=fsdb -seed=100 -base_dut=second -repeat=2


SUITE XXX ----------------

//Description: IP-AP_IF, Frames-1, Resolution-1344x16, Random-Pic data, Owner-Kevin, Status-Done
run -s_run=step2 -name=ap_if_sv_single_frame_short_1344x16_test -auto_dut=ap_if -auto_tb=ap_if -define="VRF_AP_IF" -vpa="+ap_if_frame_num=1 +resolution_left=1344 +resolution_right=16" -prerun="touch aaa" -postrun="touch bbb" -wave=fsdb -seed=100 -repeat=1

//Description: IP-AP_IF, Frames-1, Resolution-1344x16, Random-Pic data, Owner-Kevin, Status-Done
run -s_run=step2 -name=ap_if_sv_single_frame_short_1344x16_test -auto_dut=ap_if -auto_tb=ap_if -define="VRF_AP_IF" -vpa="+ap_if_frame_num=1 +resolution_left=1344 +resolution_right=16" -prerun="touch aaa" -postrun="touch bbb" -wave=fsdb -seed=100 -base_dut=fourth -repeat=2
```

-suite=BASE, then the 2 tests in SUITE BASE will be run and other SUITEs will be ignored

#### -rm_pass

In regression, this option will remove passed test folders to save disk space, but the passed test logs will reserved to replace the missed folders.

#### -rerun

After regression, if this is specified, the collected failed tests will maintained in reg_result_fail, and all of the failed tests will be rerun in the same folder in the regression folder with waveform open(now the waveform is open as fsdb).

Then the debug will be easier and faster.

### rerun_for options

No matter -rerun was passed or not, this option will rerun the failed tests and with waveform open for the regression folder provided

eg. -rerun_for=regression_2023_03_21_15_37_11

>Notice: either -lsf/-slurm can be used.

#### -s_rerun2_for

Rerun failed tests with waveform open for the provided regression folder (VCS 2-step).

#### -s_rerun3_for

Rerun failed tests with waveform open for the provided regression folder (VCS 3-step).

#### -c_rerun1_for

Rerun failed tests with waveform open for the provided regression folder (XRUN 1-step).

#### -c_rerun3_for

Rerun failed tests with waveform open for the provided regression folder (XRUN 3-step).

## Job Scheduler

The general configuration json file are located in: config/json/job_scheduler/xxx.json

### -job

Specify the job schedule method: `slurm`, `lsf`, or `no`. Default is `no`.

### -lsf_q

Use LSF to run. Necessary in login server.

specify the bqueue for using lsf. for example, python3 run ... -lsf -lsf_q=sim

### -slurm_q

Use SLURM to run. Necessary in login server.

### -slurm_mem

Specify the memory for each task in SLURM. Default is `1000M`.

## JSON for projects

### -json

The options for EDA and all process of the simulation/emulation are managed in a JSON file. Default is uve.json.

Pass the used json file to simulation.

eg. -json=config/json/project/xxx.json

### -json_extra

pass extra json file used to simulation including comp/run sections. example json is uve_extra.json

eg. -json_extra=config/json/project/xxx_extra.json

## Other Options

### -report

Only valid in regression, support VCS-2step and VCS-3step flow.

It will use the result check tool to analyse all logs in detail and generate html report into regression folder, report.html, which can be opened and reviewed in web brownser such as Firefox.

The report is simpla, plain but useful. the information will be displayed:

- summary for case num, pass, fail etc.
- result status
- log link (can be opened if in linux server)
- case name
- seed
- simulation time
- finish time
- log full path
- first error

When -slurm open the result check tool will be submitted to slurm.

When this option is closed, the basic report will also generated in regression flow:

- basic analysis based on the base test PASS/FAIL method.
- reg_result/reg_result_fail files will be generated in regression folder

If the option is closed during regression, it is not needed to rerun the regression. Then if user need to review the report.html, just go to the regression folder, execute the report script.

```bash
python3 report -h

usage: report [-h] [-step2] [-clean]

Report Flow

optional arguments:
  -h, --help  show this help message and exit
  -step2      Do the result analysis and collection for 2-step regression.
              default is 3-step
  -clean      Clean the test_xxx.py in each folder.
```

1. -step2: do the report collection in regression folder running with VCS-2step. default is VCS-3step

2. -clean: In general usage, the user do not need to worry the py files used or generated by python pytest.

If the user want to clean all the test_xxx.py files manually, this option is used for it.

Please refer to the Guideline_for_creating_and_managing_files.pdf for:

- error check/ignore
- warning check/ignore

This is very important for QA for verification.

### -clean

Clean the root folder.

### -debug

Enable debug mode to print additional debug information.

### -git_update

Update the repository and submodules.

### -gen_test_status

Please configure the tests to be searched according to folder, the info is located: config/info/tests.info

Automatically generate the xlsx file to show the existed tests in current repository. The tests are listed in different tab of the xlsx managed using test folder.

The information will show:

- Test Group (for different module to be verified)
- Test SUITE (Feature)
- Test Name
- Test Description
- Random Config
- Verification Level
- Platform
- Status
- Defines
- Test Plugsargs
- Value Plugsargs
- Owner
- Test Case count
- Total Test Group count
- Total Test count

### -check_git_clean

Check all the folders in the repo, analyze folders/files within specified level layer.
check_git_clean_check will be created to store the information for reviewing. This will be git ignored and need to be deleted manually.

review information:

- newly added folder
- should not contain in xxx

### -info_defines

Collect all the defines in design/verif folders, analyze folders/files within specified level layer.
info_defines will be created to store the information for reviewing. This will be git ignored and need to be deleted manually.
Please note: vip folder will be skipped.

review information:

- Found in design
- Found in verif

### -info_git_submodule

Show all the git repository/submodule information.

### -info_uvm

File/structures summary of xVCs according to the specified list in `config/info/xxx.info`.

### -info_all_testlist

Info about all the testlists in the test folder.

## Examples

### Setup Environment

```sh
python run -env_setup
```

### Generate Filelist

```sh
python run -list
```

### Run Simulation with Synopsys Tool

```sh
python run -tool=snps -s_run=step2 -name=test_case
```

### Run Regression with Cadence Tool

```sh
python run -tool=cdns -c_regress1=test/xxx/testlist_xxx
```

### Clean Root Folder

```sh
python run -clean
```

## Contributing

If you would like to contribute to UVE Tools, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Create a new Pull Request

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
