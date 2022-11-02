import pandas as pd
import os

from time import sleep

import logging

df = pd.DataFrame(columns=["a", "b", "c"], data=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])

VALUE_TEST = os.environ.get("VALUE_TEST", "test")
SHAREPOINT_PASSWORD = "ok boomer"

counter = 0

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter())
logger.addHandler(handler)

if __name__ == "__main__":
    print("Hello World!")
    print(df.shape)
    print(df.columns)
    print("SHAREPOINT_PASSWORD", SHAREPOINT_PASSWORD)
    print("VALUE_TEST", VALUE_TEST)

    while counter != 5:
        print(counter)
        logger.info(f"info, counter: {counter}")
        logger.warning(f"warning, counter: {counter}")
        logger.error(f"error, counter: {counter}")
        sleep(1)
        counter += 1
