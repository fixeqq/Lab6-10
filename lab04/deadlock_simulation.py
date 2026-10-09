import threading
import time


gpu_0_lock = threading.Lock()
gpu_1_lock = threading.Lock()


def train_model_a():
    print("[Model A] Waiting to acquire GPU 0...")
    gpu_0_lock.acquire()
    print("[Model A] Successfully acquired GPU 0! Processing...")
    time.sleep(0.1)
    print("[Model A] Waiting to acquire GPU 1...")
    gpu_1_lock.acquire()
    print("[Model A] Successfully acquired GPU 1! Training complete.")
    gpu_1_lock.release()
    gpu_0_lock.release()


def train_model_b():
    print("[Model B] Waiting to acquire GPU 1...")
    gpu_1_lock.acquire()
    print("[Model B] Successfully acquired GPU 1! Processing...")
    time.sleep(0.1)
    print("[Model B] Waiting to acquire GPU 0...")
    gpu_0_lock.acquire()
    print("[Model B] Successfully acquired GPU 0! Training complete.")
    gpu_0_lock.release()
    gpu_1_lock.release()


def main():
    print("--- Starting ML Training Cluster ---")
    thread1 = threading.Thread(target=train_model_a)
    thread2 = threading.Thread(target=train_model_b)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("--- Cluster Execution Completed ---")


if __name__ == "__main__":
    main()
