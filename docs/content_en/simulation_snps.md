# VCS

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

**Guardrail:** `-s_tb` requires a valid DUT compile database. If no DUT compile is requested in the same command, specify `-base_dut=<name>`.

## -s_sim

Execute the simulation using VCS `step3` method.

**Guardrail:** `-s_sim` requires a valid TB compile database. If no TB compile is requested in the same command, specify `-base_tb=<name>`.

## -s_part_comp

Specify the Synopsys tool partition compile method: `auto`, `manual`, or `no`. The default is `no`.

For manual partitioning, compile time can be reduced. However, you must combine `json_extra` to pass the `cfg.v`. An example can be found in `xxx_extra.json`.

## Wave compatibility (VCS)

`-wave=fsdb` and `-wave=vpd` are supported for VCS.

`-wave=shm` is Cadence-oriented and is blocked for VCS.
