import threading
import time

from task import process_image


def thread_worker(image_id):
    process_image(image_id)


def main():
    num_images = 16
    threads = []
    print(f"--- Starting Multithreading for {num_images} images ---")
    start_time = time.time()

    for i in range(num_images):
        thread = threading.Thread(target=thread_worker, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    elapsed = time.time() - start_time
    print(f"Total Time (Threads): {elapsed:.2f} seconds")


if __name__ == "__main__":
    main()
