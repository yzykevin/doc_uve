# SNPS VCS

- [SNPS VCS](#snps-vcs)
  - [-s\_run2](#-s_run2)
  - [-s\_run3](#-s_run3)
  - [-s\_com](#-s_com)
  - [-s\_dut](#-s_dut)
  - [-s\_tb](#-s_tb)
  - [-s\_sim](#-s_sim)
  - [-s\_part\_comp](#-s_part_comp)

> Specify `-tool=snps` to use these options.

## -s_run2

Select the run method for the Synopsys tool: `step2`. This performs the complete process from compiling to simulating.

## -s_run3

Select the run method for the Synopsys tool: `step3`. This performs the complete process from compiling to simulating.

> **Note:** If `step3` is used, the DUT/testbench compiling folder will not be refreshed automatically. If the DUT/testbench is updated, the compiled folder must be cleaned, and the `step3` run must be executed again to use the updated files.  
> For cases in the development stage, it is recommended to use the `step2` run (`-s_run=step2`).

## -s_com

Compile only using VCS `step2` method.

## -s_dut

Compile the DUT using VCS `step3` method.

## -s_tb

Compile the testbench using VCS `step3` method.

## -s_sim

Execute the simulation using VCS `step3` method.

## -s_part_comp

Specify the Synopsys tool partition compile method: `auto`, `manual`, or `no`. The default is `no`.

For manual partitioning, compile time can be reduced. However, you must combine `json_extra` to pass the `cfg.v`. An example can be found in `xxx_extra.json`.
