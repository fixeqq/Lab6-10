"""Demonstrate OS-level write protection with chmod."""

import os
import stat


def main():
    secure_file = "secret_config.json"

    if os.path.exists(secure_file):
        os.chmod(secure_file, 0o666)
        os.remove(secure_file)

    with open(secure_file, "w") as f:
        f.write("{'api_key': '12345XYZ'}")
    print(f"Created {secure_file}.")

    print("Locking file permissions to Read-Only (0o400)...")
    os.chmod(secure_file, 0o400)
    print(f"New Permissions: {stat.filemode(os.stat(secure_file).st_mode)}")

    print("\nAttempting to overwrite the file...")
    try:
        with open(secure_file, "a") as f:
            f.write("\nMALICIOUS HACKER DATA")
        print("Success! Data written.")
    except PermissionError as error:
        print(f">>> [OS KERNEL BLOCKED] PermissionError: {error}")
        print(">>> The Operating System successfully protected the file!")
    finally:
        os.chmod(secure_file, 0o600)
        os.remove(secure_file)


if __name__ == "__main__":
    main()
