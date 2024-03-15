import random
from time import sleep

# Constants
MIN_MILES_LOW = 1
MAX_MILES_LOW = 25
MIN_MILES_QUARTER = 25.1
MAX_MILES_QUARTER = 50

def gasLevelGauge():
    """Simulates a gas level gauge."""
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gasLevelList)

def locateGasStation():
    """Simulates locating a nearby gas station."""
    gasStations = ["Shell", "Speedway", "Marathon", "Circle K", "Mobil", "Costco", "Meijer", "7-Eleven"]
    return random.choice(gasStations)

def gasLevelAlert():
    """Alerts the user based on the gas level."""
    gasLevelIndicator = gasLevelGauge()

    if gasLevelIndicator == "Empty":
        print("*** WARNING - YOUR TANK IS EMPTY ***\n")
        sleep(2.5)
        print("    *** Calling Triple AAA ***")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is low. Checking for the nearest gas station...")
        sleep(2.5)
        miles_to_station = round(random.uniform(MIN_MILES_LOW, MAX_MILES_LOW), 1)
        print("The closest gas station is", locateGasStation(), "which is", miles_to_station, "miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is at a quarter tank.")
        sleep(2.5)
        miles_to_station = round(random.uniform(MIN_MILES_QUARTER, MAX_MILES_QUARTER), 1)
        print("The closest gas station is", locateGasStation(), "which is", miles_to_station, "miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is at half tank. You have plenty to reach your destination.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is at three quarter tank.")
    else:
        print("Your gas tank is full.")

# Execute the gas level alert system
gasLevelAlert()
