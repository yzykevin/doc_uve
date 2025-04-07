# Job Scheduler

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