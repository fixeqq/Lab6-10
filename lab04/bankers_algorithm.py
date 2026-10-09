import numpy as np


total_resources = np.array([10, 5, 7])
max_need = np.array([
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
])
allocated = np.array([
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
])


def is_safe_state(available, max_need, allocated):
    num_jobs = len(allocated)
    work = available.copy()
    finish = [False] * num_jobs
    safe_sequence = []
    need = max_need - allocated

    while len(safe_sequence) < num_jobs:
        allocated_in_this_round = False
        for i in range(num_jobs):
            if not finish[i] and np.all(need[i] <= work):
                work += allocated[i]
                finish[i] = True
                safe_sequence.append(f"Job_{i}")
                allocated_in_this_round = True
        if not allocated_in_this_round:
            return False, []

    return True, safe_sequence


def main():
    print("--- OS Scheduler: Banker's Algorithm Check ---")
    available = total_resources - np.sum(allocated, axis=0)
    print(f"Currently Available Resources: {available}")
    safe, sequence = is_safe_state(available, max_need, allocated)

    if safe:
        print(f">> SYSTEM IS SAFE. Execution Sequence: {' -> '.join(sequence)}")
        print(">> OS will grant the lock requests.")
    else:
        print(">> WARNING: SYSTEM IS UNSAFE! Granting locks will cause a Deadlock.")
        print(">> OS Scheduler denies the request and forces the process to wait.")


if __name__ == "__main__":
    main()
