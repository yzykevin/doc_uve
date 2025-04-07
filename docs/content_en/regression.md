# Regression

To run a regression of all tests in a testlist, the regression folder will be created in the `work` folder using a combination of regression and running date/time.

The test with seed combination folder will be created in the `regression_` folder.

The options in each test command in the testlist will be ignored:

- `-wave`
- `-seed`

These options can be passed within the command of the regression.

Note that if there is a `-repeat` option in a single test command, `-seed` will be ignored, and a random seed will be used for the `-repeat` times.

Example:

VCS 3-step command

```terminal
python3 run -s_regress3=test/xxx/testlist_xxx -reg_num=8 -wave=fsdb -seed=100
```

VCS 2-step command

```terminal
python3 run -s_regress2=test/xxx/testlist_xxx -reg_num=8 -wave=fsdb -seed=100
```

**Note:** If all regression is run with waveform open, the size of the result folder will be large, which may consume too much disk space.

## Display in Terminal

All the information will be displayed with *COLOR*.

The information includes:

- The main program process PID
- The number of parallel running processes
- Total number of running cases
- Total CPU count of the current server
- Regression location in the `run` folder
- Running test details:
  - Name
  - PID
  - Starting date/time
- Finished test details:
  - Name
  - Finishing date/time
  - Duration
- Successfully finished tests (tests that may get stuck will not show)
- Test rough result: `PASSED`/`FAILED`
- Test result report file location

## `-reg_num`

Specifies the number of parallel regressions. Default is 5.

**Caution:** Do not set the number too high to avoid overloading the server.

Parallel running uses multiple processes on a single server. A higher number will result in faster regression time but higher system resource consumption. Please provide a reasonable number and ensure it does not disturb other engineers' work.

This can be used in combination with `-lsf`/`-slurm`.

## `-suite`

Runs regression with the provided suite in the testlist.

## `-rm_pass`

In regression, this option removes passed test folders to save disk space, but the passed test logs will be retained to replace the removed folders.

## `-rerun`

After regression, if this option is specified, the failed tests will be collected and maintained in `reg_result_fail`. All failed tests will be rerun in the same folder within the regression folder with waveform open (currently as `fsdb`).

This makes debugging easier and faster.

## `rerun_for` Options (tools related)

Regardless of whether `-rerun` is passed or not, this option reruns the failed tests with waveform open for the specified regression folder.

Example:

```terminal
-s_rerun2_for=regression_2028_03_21_15_37_11
```

Please check the detailed options in tools related descriptions.
