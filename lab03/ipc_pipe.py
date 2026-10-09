import os
import time


def main():
    read_fd, write_fd = os.pipe()
    pid = os.fork()

    if pid > 0:
        os.close(write_fd)
        read_file = os.fdopen(read_fd)
        print(f"[Trainer PID:{os.getpid()}] Waiting for data from DataLoader...")
        data = read_file.read()
        print(f"[Trainer PID:{os.getpid()}] Received Data: '{data}'")
        print(f"[Trainer PID:{os.getpid()}] Training complete.")
        os.wait()
    elif pid == 0:
        os.close(read_fd)
        write_file = os.fdopen(write_fd, "w")
        print(f"  -> [DataLoader PID:{os.getpid()}] Loading image from disk...")
        time.sleep(2)
        image_data = "Image_Tensor_Batch_01"
        print(f"  -> [DataLoader PID:{os.getpid()}] Sending data through OS Pipe...")
        write_file.write(image_data)
        write_file.close()


if __name__ == "__main__":
    main()
