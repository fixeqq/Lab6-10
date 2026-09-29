"""Compare FIFO and LRU page replacement policies."""


def simulate_fifo(reference_string, num_frames):
    frames = []
    page_faults = 0

    print(f"\n--- Running FIFO Algorithm (Frames: {num_frames}) ---")
    for page in reference_string:
        if page not in frames:
            page_faults += 1
            if len(frames) >= num_frames:
                victim = frames.pop(0)
                print(f"Page Fault! Evicted Page {victim}. Loaded Page {page}")
            else:
                print(f"Page Fault! Loaded Page {page} (Empty Frame)")
            frames.append(page)
        else:
            print(f"Page Hit! Page {page} is already in RAM.")

    print(f">> Total FIFO Page Faults: {page_faults}")
    return page_faults


def simulate_lru(reference_string, num_frames):
    # The list is kept from least recently used to most recently used.
    frames = []
    page_faults = 0

    print(f"\n--- Running LRU Algorithm (Frames: {num_frames}) ---")
    for page in reference_string:
        if page not in frames:
            page_faults += 1
            if len(frames) >= num_frames:
                victim = frames.pop(0)
                print(f"Page Fault! Evicted Page {victim}. Loaded Page {page}")
            else:
                print(f"Page Fault! Loaded Page {page} (Empty Frame)")
            frames.append(page)
        else:
            print(f"Page Hit! Page {page} is already in RAM.")
            # An accessed page becomes the most recently used page.
            frames.remove(page)
            frames.append(page)

    print(f">> Total LRU Page Faults: {page_faults}")
    return page_faults


def main():
    # This sequence has repeated accesses, so it shows temporal locality.
    ai_memory_requests = [2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5, 2]
    total_physical_frames = 3

    fifo_faults = simulate_fifo(ai_memory_requests, total_physical_frames)
    lru_faults = simulate_lru(ai_memory_requests, total_physical_frames)

    print("\n--- Page Replacement Summary ---")
    print(f"FIFO faults: {fifo_faults}")
    print(f"LRU faults: {lru_faults}")
    print(f"LRU advantage: {fifo_faults - lru_faults} fewer fault(s)")


if __name__ == "__main__":
    main()
