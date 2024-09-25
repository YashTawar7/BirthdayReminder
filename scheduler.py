import schedule
import time


def my_function():
    # Code for your function goes here
    print("Running my_function")


# Schedule the function to run at a specific time
schedule.every().day.at("19:25").do(my_function)


# Continuously check if the scheduled time has arrived
while True:
    schedule.run_pending()
    time.sleep(1)
