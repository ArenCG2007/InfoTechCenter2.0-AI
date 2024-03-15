# Print a separator for better visual separation
print("**************************************************")
print("Gasoline Branch\n\n")

# Import necessary libraries
import random
from time import sleep


# Function to randomly select a gas level
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel


# Function to randomly select a gas station
def listOfGasStations():
    gasStations = ["Shell", "Speedway", "Marathon", "Circle K", "Mobil", "Costco", "Meijer", "7Eleven"]
    gasStationsNearby = random.choice(gasStations)
    return gasStationsNearby


# Function to alert about gas levels and nearest gas stations
def gasLevelAlert():
    # Generate random distances to gas stations
    milesToGasStationsLow = round(random.uniform(1, 25), 1)
    milesToGasStationsQuarterTank = round(random.uniform(25.1, 50), 1)

    # Determine the current gas level
    gasLevelIndicator = gasLevelGauge()

    # Print the current gas level
    print("Gas Level:", gasLevelIndicator)

    # Check the gas level and provide appropriate alerts
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***\n")
        sleep(2.5)
        print("    ***Calling Triple AAA***")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is low, consider refueling soon.")
        sleep(2.5)
        print("The closest gas station is", listOfGasStations(), "which is", milesToGasStationsLow, "miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is at a quarter. You might want to refuel soon.")
        sleep(2.5)
        print("The closest gas station is", listOfGasStations(), "which is", milesToGasStationsQuarterTank,
              "miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is at half full, you have plenty to reach your destination.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is at three-quarters full.")
    else:
        print("Your gas tank is full.")


# Loop to simulate multiple runs of the gas level alert
for _ in range(3):  # Run the alert 3 times
    gasLevelAlert()
    print("\n" + "=" * 50 + "\n")  # Print a separator after each alert
