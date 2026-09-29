"""Show how mmap maps a large file without loading all of it immediately."""

import mmap
import os

import psutil


def print_memory():
    process = psutil.Process(os.getpid())
    usage_mb = process.memory_info().rss / (1024 * 1024)
    print(f"[OS Monitor] Physical RAM Usage: {usage_mb:.2f} MB")


def main():
    file_path = "fake_llm_weights.bin"

    print("Creating a 50MB fake LLM file on Disk...")
    with open(file_path, "wb") as f:
        f.write(b"\x00" * (50 * 1024 * 1024))

    print_memory()

    print("\nMapping the 50MB file into Virtual Memory...")
    with open(file_path, "r+b") as f:
        mm = mmap.mmap(f.fileno(), 0)
        print_memory()

        print("\nAccessing weight at index 25,000,000 (Triggers OS Page Fault)...")
        weight = mm[25_000_000]
        print(f"Weight value accessed successfully: {weight}")
        mm.close()

    os.remove(file_path)


if __name__ == "__main__":
    main()
