# Simulation

## -tool

Select the tool to use: Synopsys VCS (`snps`) or Cadence XRUN (`cdns`). Default is `snps`.

## -list

Automatically generate `filelist.f` in the `design` folder, which will be used for the testbench.

The `filelist.f` will include all `.v` files with the absolute path of the cloned repo. Please ensure the `rtl` folder is clean and does not contain unused files.

To use this, follow these steps:

1. Create the `xxx` folder and place all design files into it.
2. Add the `xxx` name to `design/fl/dut_auto_fl/dut_auto_filelist`.
3. Run the command: `python3 run -list`.
4. The `xxx_filelist.f` will be generated in `design/fl/dut_auto_fl/`.

The list can be found and managed in `design/fl/dut_auto_fl/dut_auto_filelist`.

All the folder names in dut_auto_filelist will be generated.

## -auto_dut

Automatically generate `dut.f` in the `design/fl/` folder for each RTL module, which will be used for the testbench.

To use this, follow these steps:

1. Based on `-list` generation, provide `xxx` from the list: `design/fl/dut_auto_fl/dut_auto_filelist`.
2. Run the command: `python3 run -auto_dut=xxx`.
3. The `dut.f` will be generated in `design/fl/`.

## -auto_tb

Automatically generate `tb.f` in the `verif/fl/` folder, which will be used for the testbench.

To use this, follow these steps:

1. Prepare the `xxx` filelist in `verif/fl/tb_auto_fl/`.
2. Run the command: `python3 run -auto_tb=xxx`.
3. The `tb.f` will be generated in `verif/fl/`.

Additionally, automatically generate `xxx_test_include.sv` in the `verif/tb/test_include/` folder, which will include all tests found in `verif/test/xxx/` and be used for the testbench.

The `tb.f` will include all existing `verif/pkg/xxx` folders, `vip_snps` folders, and `verif/test/xxx` folder paths.

## -manual_dut

Specify the manually written DUT filelist to simulate.

The filelists should be prepared and managed in the relative root folder `design/fl/dut_manual_fl/`.

Example, using `-manual_dut=xxx_flist.f`:

The file `design/fl/dut_manual_fl/xxx_flist.f` will be used as the `dut.f`.

## -manual_tb

Specify the manually written TB filelist to simulate.

The filelists should be prepared and managed in the relative root folder `verif/fl/tb_manual_fl/`.

Example, using `-manual_tb=xxx_flist.f`:

The file `verif/fl/tb_manual_fl/xxx_flist.f` will be used as the `tb.f`.

## -run_folder

Specify the run folder. Default is `work`.

## -name

Specify the test name.

Example, using `-name=xxx_test`. This will use xxx_test.sv like +UVM_TESTNAME=xxx_test

### -base_dut

3-step only! skip dut compiling, use the base_dut specified dut compiling database。

Example: `-base_dut=xxx`  
This creates and compiles `PROJECT_NAME_xxx`. By default, `PROJECT_NAME` is used as the compilation folder.

### -base_tb

3-step only! skip tb compiling, use the base_tb specified tb compiling database

Example: `-base_tb=xxx_xxx_test`

## -dump_scope

Specify the waveform dump scope. Default: `verif/test/common/dump_scope.txt`.

## -prerun

Run a command/script before simulation. Use the format: `-prerun=""`.

## -postrun

Run a command/script after simulation. Use the format: `-postrun=""`.

## -define

Pass defines to the simulation. Use the format: `-define=""`.

Examples:  
`-define="aaa"`  
`-define="aaa bbb ccc"`

## -tpa

Pass test plug arguments to the simulation. Use the format: `-tpa=""`.

Examples:  
`-tpa="+aaa"`  
`-tpa="+aaa, +bbb"`

## -vpa

Pass value plug arguments to the simulation. Use the format: `-vpa=""`.

Examples:  
`-vpa="+aaa=xxx"`  
`-vpa="+aaa=xxx, +bbb=yyy"`

## -seed

Specify a seed for the simulation. Default: random.

## -repeat

Specify the number of times to repeat a test case. Default: 1.

## -wave

Specify the wave dump format. Options: `fsdb`, `vpd`, `shm`.

### -cov

Enable coverage collection. Options: `all` or specific types (e.g., `line,tgl,fsm,branch,cond,assert`).
