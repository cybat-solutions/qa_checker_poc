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

workflow_summary_filename = os.environ.get("GITHUB_STEP_SUMMARY", None)

workflow_summary_text = f"""<summary><b>{SHAREPOINT_PASSWORD.upper()}</b></summary>\n
| NUM | LETTER |
| --- |:------:|
"""

if __name__ == "__main__":
    print("Hello World!")
    print(df.shape)
    print(df.columns)
    print("SHAREPOINT_PASSWORD", SHAREPOINT_PASSWORD)
    print("VALUE_TEST", VALUE_TEST)

    for num, letter in enumerate("abcde"):
        print(letter)
        workflow_summary_text += f"| {num} | {letter} |\n"

        logger.info(f"info, letter: {letter}")
        logger.warning(f"warning, letter: {letter}")
        logger.error(f"error, letter: {letter}")
        sleep(1)

    if workflow_summary_filename is not None:
        with open(workflow_summary_filename, 'a') as f:
            f.write(workflow_summary_text)
