"""Simulate an OS coordinating diverse AI workloads."""

import os
import queue
import threading
import time


class AIClusterOS:
    def __init__(self, total_ram_gb, num_gpus):
        self.total_ram_gb = total_ram_gb
        self.available_ram_gb = total_ram_gb
        self.ram_lock = threading.Lock()
        self.gpu_locks = {i: threading.Lock() for i in range(num_gpus)}
        self.gpu_status = {i: "IDLE" for i in range(num_gpus)}

        self.job_queue = queue.Queue()
        self.active_jobs = []
        self.is_running = True

        self.dash_thread = threading.Thread(target=self._dashboard_loop, daemon=True)
        self.dash_thread.start()
        self.scheduler_thread = threading.Thread(target=self._os_scheduler_loop)
        self.scheduler_thread.start()

    def _dashboard_loop(self):
        while self.is_running:
            time.sleep(1.5)
            print("\n" + "=" * 50)
            print(f"[LIVE DASHBOARD] RAM Available: {self.available_ram_gb}/{self.total_ram_gb} GB")
            gpu_str = " | ".join(
                f"GPU {i}: {self.gpu_status[i]}" for i in self.gpu_locks
            )
            print(f"[LIVE DASHBOARD] {gpu_str}")
            print(f"[LIVE DASHBOARD] Queue Size: {self.job_queue.qsize()} | Active Jobs: {len(self.active_jobs)}")
            print("=" * 50 + "\n")

    def submit_job(self, job_name, dataset_path, req_ram, req_gpus, duration):
        self.job_queue.put((job_name, dataset_path, req_ram, req_gpus, duration))
        print(f"[API] Submitted: {job_name} -> Queued.")

    def _os_scheduler_loop(self):
        while self.is_running or not self.job_queue.empty():
            try:
                job_data = self.job_queue.get(timeout=1)
                worker = threading.Thread(target=self._execute_job, args=job_data)
                worker.start()
            except queue.Empty:
                continue

    def _execute_job(self, job_name, dataset_path, req_ram, req_gpus, duration):
        if not os.path.exists(dataset_path):
            print(f"[FAIL] [{job_name}] Dataset '{dataset_path}' not found or permission denied.")
            self.job_queue.task_done()
            return

        self.active_jobs.append(job_name)
        print(f"[WAIT] [{job_name}] Waiting for {req_ram} GB RAM...")
        while True:
            with self.ram_lock:
                if self.available_ram_gb >= req_ram:
                    self.available_ram_gb -= req_ram
                    break
            time.sleep(0.5)

        print(f"[MEMORY] [{job_name}] Allocated {req_ram} GB RAM.")

        sorted_gpus = sorted(req_gpus)
        if sorted_gpus:
            print(f"[WAIT] [{job_name}] Waiting for GPUs {sorted_gpus}...")
        for gpu in sorted_gpus:
            self.gpu_locks[gpu].acquire()
            self.gpu_status[gpu] = f"BUSY ({job_name})"

        if sorted_gpus:
            print(f"[RUNNING] [{job_name}] Acquired GPUs {sorted_gpus}.")
        else:
            print(f"[RUNNING] [{job_name}] Running on CPU only.")

        try:
            time.sleep(duration)
            print(f"[DONE] [{job_name}] Finished successfully.")
        finally:
            for gpu in reversed(sorted_gpus):
                self.gpu_status[gpu] = "IDLE"
                self.gpu_locks[gpu].release()
            with self.ram_lock:
                self.available_ram_gb += req_ram
            self.active_jobs.remove(job_name)
            self.job_queue.task_done()

    def shutdown(self):
        self.job_queue.join()
        self.is_running = False
        self.scheduler_thread.join()
        time.sleep(2.0)
        print("\n=== Cluster OS Shutdown Gracefully ===")


def main():
    with open("secure_dataset.csv", "w") as f:
        f.write("dummy data")

    print("=== Booting AI Cluster OS (64 GB RAM, 4 GPUs) ===")
    os_system = AIClusterOS(total_ram_gb=64, num_gpus=4)

    os_system.submit_job("Workload_A_LLaMA", "secure_dataset.csv", 40, [2, 1, 0], 8)
    time.sleep(1)
    os_system.submit_job("Workload_B_Preproc", "secure_dataset.csv", 16, [], 6)
    time.sleep(1)
    os_system.submit_job("Workload_C_Infer", "secure_dataset.csv", 2, [3], 3)
    time.sleep(1)
    os_system.submit_job("Workload_D_Hacker", "secret_keys.txt", 1, [], 1)

    os_system.shutdown()
    os.remove("secure_dataset.csv")


if __name__ == "__main__":
    main()
