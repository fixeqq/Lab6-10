import multiprocessing
import time

from task import process_image


def process_worker(image_id):
    process_image(image_id)


def main():
    num_images = 16
    processes = []
    print(f"--- Starting Multiprocessing for {num_images} images ---")
    start_time = time.time()

    for i in range(num_images):
        process = multiprocessing.Process(target=process_worker, args=(i,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    elapsed = time.time() - start_time
    print(f"Total Time (Processes): {elapsed:.2f} seconds")


if __name__ == "__main__":
    main()
