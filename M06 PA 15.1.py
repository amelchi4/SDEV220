import multiprocessing
import time
import random
from datetime import datetime

def x():
    time.sleep(random.uniform(0, 1))
    print(f"Current time: {datetime.now()}")

if __name__ == "__main__":
    for _ in range(3):
        multiprocessing.Process(target=x).start()
