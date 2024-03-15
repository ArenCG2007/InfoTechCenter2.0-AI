import time
import sys

def boot_up_sequence(duration=0.5, iterations=20):
    """Simulates a boot-up sequence with ellipsis animation and percentage completion."""
    print("\n\nWelcome to InfoTech Center V1.0\n")
    time.sleep(duration)

    for i in range(iterations):
        progress = (i + 1) * 100 // iterations
        ellipsis = i % 4
        message = f"Infotech Center System Booting{'.' * ellipsis} {progress}%"
        sys.stdout.write("\r" + message)
        sys.stdout.flush()
        time.sleep(duration)

    print("\n\nOperating System Booted Up - Retina Scanned - Access Granted")

if __name__ == "__main__":
    try:
        boot_up_sequence()
    except KeyboardInterrupt:
        print("\n\nBoot-up sequence interrupted.")
    except Exception as e:
        print(f"\n\nAn error occurred: {e}")
