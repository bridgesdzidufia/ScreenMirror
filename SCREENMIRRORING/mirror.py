import os
import subprocess

def check_device():
    """Check if an Android device is connected."""
    try:
        result = subprocess.check_output(['adb', 'devices']).decode()
        devices = [line.split()[0] for line in result.splitlines()[1:] if 'device' in line]
        if devices:
            print(f"Device found: {devices[0]}")
            return True
        else:
            print("No device connected. Please connect your phone via USB.")
            return False
    except subprocess.CalledProcessError as e:
        print(f"Error checking device: {e}")
        return False

def start_mirroring():
    """Launch scrcpy to mirror the Android phone."""
    try:
        print("Starting scrcpy...")
        subprocess.run(['scrcpy'], check=True)
    except FileNotFoundError:
        print("scrcpy not found. Please ensure it is installed.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to launch scrcpy: {e}")

if __name__ == "__main__":
    if check_device():
        start_mirroring()
