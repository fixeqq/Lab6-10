"""Observe the RAM used by a Python process before and after allocation."""

import os
import time

import psutil


def print_memory_usage():
    process = psutil.Process(os.getpid())
    mem_mb = process.memory_info().rss / (1024 * 1024)
    print(f"[OS Monitor] Current Physical RAM Usage: {mem_mb:.2f} MB")


def main():
    print(f"--- AI Model Memory Allocation (PID: {os.getpid()}) ---")
    print_memory_usage()

    print("\nLoading a large Neural Network layer into memory...")
    time.sleep(2)
    ai_model_weights = [0.0] * 10_000_000

    print("Model Loaded successfully!")
    print_memory_usage()

    # Keep the process alive long enough to inspect it with htop.
    print("\nProgram is sleeping. Open another terminal and run htop")
    time.sleep(30)
    del ai_model_weights


if __name__ == "__main__":
    main()
