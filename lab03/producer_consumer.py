import random
import threading
import time


BUFFER_SIZE = 5
buffer = [None] * BUFFER_SIZE
in_index = 0
out_index = 0

mutex = threading.Lock()
empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)


def data_loader_producer():
    global in_index
    for i in range(10):
        item = f"Image_Batch_{i}"
        time.sleep(random.uniform(0.1, 0.3))
        empty.acquire()
        mutex.acquire()
        buffer[in_index] = item
        print(f"[Producer] Loaded: {item} into slot {in_index}")
        in_index = (in_index + 1) % BUFFER_SIZE
        mutex.release()
        full.release()


def gpu_trainer_consumer():
    global out_index
    for _ in range(10):
        full.acquire()
        mutex.acquire()
        item = buffer[out_index]
        print(f"    -> [Consumer] Training on: {item} from slot {out_index}")
        out_index = (out_index + 1) % BUFFER_SIZE
        mutex.release()
        empty.release()
        time.sleep(random.uniform(0.2, 0.5))


def main():
    print("--- Starting ML Data Pipeline (Bounded Buffer) ---")
    producer_thread = threading.Thread(target=data_loader_producer)
    consumer_thread = threading.Thread(target=gpu_trainer_consumer)
    producer_thread.start()
    consumer_thread.start()
    producer_thread.join()
    consumer_thread.join()
    print("--- Pipeline Execution Completed Successfully ---")


if __name__ == "__main__":
    main()
