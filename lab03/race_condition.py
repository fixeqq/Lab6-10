import threading
import time


shared_weight = 0


def update_weights(iterations):
    global shared_weight
    for _ in range(iterations):
        temp = shared_weight
        time.sleep(0.0000001)
        shared_weight = temp + 1


def main():
    target_iterations = 100
    thread1 = threading.Thread(target=update_weights, args=(target_iterations,))
    thread2 = threading.Thread(target=update_weights, args=(target_iterations,))

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    expected_value = target_iterations * 2
    print(f"Expected Weight Value: {expected_value}")
    print(f"Actual Weight Value:   {shared_weight}")
    if expected_value != shared_weight:
        print(">> ERROR: Race Condition Detected! Data is corrupted.")


if __name__ == "__main__":
    main()
