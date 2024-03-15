import time
import sys

def boot_up_sequence(duration=0.5, iterations=20):
    """
    Simulates a boot-up sequence with ellipsis animation and percentage completion.

    Args:
        duration (float): Time delay between each iteration.
        iterations (int): Number of iterations for the boot-up sequence.
    """
    # Display welcome message
    print("\n\nWelcome to InfoTech Center V1.0\n")
    time.sleep(duration)

    # Iterate through the boot-up sequence
    for i in range(iterations):
        # Calculate progress percentage
        progress = (i + 1) * 100 // iterations
        # Calculate ellipsis for animation
        ellipsis = i % 4
        # Construct the boot-up message with ellipsis and progress percentage
        message = f"Infotech Center System Booting{'.' * ellipsis} {progress}%"
        # Write message to stdout, overwriting previous message using carriage return
        sys.stdout.write("\r" + message)
        sys.stdout.flush()  # Flush stdout to ensure immediate display
        time.sleep(duration)  # Wait for specified duration between iterations

    # Print final boot-up message
    print("\n\nOperating System Booted Up - Retina Scanned - Access Granted")

if __name__ == "__main__":
    try:
        # Call the boot-up sequence function
        boot_up_sequence()
    except KeyboardInterrupt:
        # Handle keyboard interrupt
        print("\n\nBoot-up sequence interrupted.")
    except Exception as e:
        # Handle other exceptions
        print(f"\n\nAn error occurred: {e}")
