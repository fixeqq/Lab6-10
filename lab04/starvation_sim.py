import threading
import time


shared_resource_lock = threading.Lock()
job_counts = {"Greedy_Model_A": 0, "Greedy_Model_B": 0, "Polite_Model": 0}
is_running = True


def greedy_task(name):
    while is_running:
        shared_resource_lock.acquire()
        job_counts[name] += 1
        shared_resource_lock.release()
        time.sleep(0.00001)


def polite_task(name):
    while is_running:
        time.sleep(0.01)
        shared_resource_lock.acquire()
        job_counts[name] += 1
        shared_resource_lock.release()


def main():
    print("--- Starting Cluster Starvation Simulation (Running for 3 seconds) ---")
    thread1 = threading.Thread(target=greedy_task, args=("Greedy_Model_A",))
    thread2 = threading.Thread(target=greedy_task, args=("Greedy_Model_B",))
    thread3 = threading.Thread(target=polite_task, args=("Polite_Model",))
    thread1.start()
    thread2.start()
    thread3.start()

    time.sleep(3.0)
    global is_running
    is_running = False
    thread1.join()
    thread2.join()
    thread3.join()

    print("\n--- Final Resource Acquisition Counts ---")
    for worker_name, count in job_counts.items():
        print(f"{worker_name}: {count} times")


if __name__ == "__main__":
    main()
