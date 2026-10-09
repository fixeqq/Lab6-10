# Run Labs 1 to 4

Run these commands in GitHub Codespaces from the repository root.

## Install dependencies

```bash
python3 -m pip install -r requirements-lab01-04.txt
```

## Lab 1

```bash
cd lab01
python3 profiler.py
python3 stress_test.py
# Press Ctrl+C after observing htop
cd ..
```

## Lab 2

```bash
cd lab02
python3 runner_seq.py
python3 runner_thread.py
python3 runner_process.py
python3 fork_zombie.py
# Open another terminal and run htop while fork_zombie.py is sleeping
# Press Ctrl+C only after observing the Z process, if needed
cd ..
```

## Lab 3

```bash
cd lab03
python3 race_condition.py
python3 ipc_pipe.py
python3 producer_consumer.py
cd ..
```

## Lab 4

```bash
cd lab04
python3 deadlock_avoidance.py
python3 bankers_algorithm.py
python3 starvation_sim.py
python3 deadlock_detection.py
```

Run deadlock_simulation.py only when ready to observe the intentional deadlock. It is designed to remain stuck until it is stopped.
