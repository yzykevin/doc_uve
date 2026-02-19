# Xcelium

> Specify `-tool=cdns` to use these options.

## -c_run1

Choose the run method for Cadence tool: `step1`. This performs the complete process from compiling to simulating.

## -c_run3

Choose the run method for Cadence tool: `step3`. This performs the complete process from compiling to simulating.

## -c_com

Compile only using XRUN 1-step method.

## -c_dut

Compile DUT using XRUN 3-step method.

## -c_tb

Compile testbench using XRUN 3-step method.

**Guardrail:** `-c_tb` requires a valid DUT compile database. If no DUT compile is requested in the same command, specify `-base_dut=<name>`.

## -c_sim

Execute simulation using XRUN 3-step method.

**Guardrail:** `-c_sim` requires a valid TB compile database. If no TB compile is requested in the same command, specify `-base_tb=<name>`.

## Wave compatibility (XRUN)

`-wave=shm` is the native Cadence format.

`-wave=fsdb` and `-wave=vpd` may work only with proper PLI setup and are not the default recommendation.
