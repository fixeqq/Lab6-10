# Lab 6-10 workspace

This folder contains the working files for Labs 6-10. The scripts are prepared for execution in GitHub Codespaces. Do not use timing values from a different computer in the final report; run the scripts in Codespaces and copy the observed output into the matching report file.

## Folder layout

- `lab05/`: `memory_allocation.py`, `page_table_sim.py`, `ai_mmap_model.py`, `Lab05_Report.txt`
- `lab06/`: `page_replacement.py`, `ai_thrashing.py`, `Lab06_Report.txt`
- `lab07/`: `cpu_scheduler.py`, `ai_inference_scheduler.py`, `Lab07_Report.txt`
- `lab08/`: `disk_scheduler.py`, `ai_dataset_io.py`, `Lab08_Report.txt`
- `lab09/`: `inode_inspector.py`, `os_security.py`, `ai_weight_protection.py`, `Lab09_Report.txt`
- `lab10/`: `ultimate_cluster_os.py`, `Lab10_Report.txt`

## Run later in Codespaces

Open a terminal in each lab folder and run the Python scripts with `python3`. For Lab 5, install the required package first with `pip install psutil`. Copy the actual outputs, timings, and observations into the corresponding report. The reports contain placeholders so that no result is accidentally presented before the experiment is run.

After checking all reports:

```bash
git add lab05 lab06 lab07 lab08 lab09 lab10 Lab6-10_README.md
git commit -m "Add Lab 5 files and report"
git push
```

If Lab 5 is included in the assignment, combine the completed reports and selected experiment evidence into one PDF named `Student_ID_Lab5-10.pdf`.
