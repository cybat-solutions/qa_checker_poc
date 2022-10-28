import pandas as pd
import os

from time import sleep

import logging

df = pd.DataFrame(columns=["a", "b", "c"], data=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])

VALUE_TEST = os.environ.get("VALUE_TEST", "test")
SHAREPOINT_PASSWORD = "ok boomer"

counter = 0

class CustomFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord):
        head = getattr(record, "head", None)
        body = getattr(record, "body", None)
        if not head and not body:
            return super().format(record)

        outputtype = "notice"

        if record.levelno == logging.DEBUG:
            outputtype = "debug"

        elif record.levelno == logging.WARNING:
            outputtype = "warning"

        elif record.levelno in (logging.ERROR, logging.CRITICAL):
            outputtype = "error"

            if record.exc_info:
                # print the traceback and the exception name and details
                logger.exception(record.msg)

        return (
                f"::{outputtype}" + ('' if head is None else f" title={head}")
                + "::" + (body or record.msg)
        )


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setFormatter(CustomFormatter())
logger.addHandler(handler)

if __name__ == "__main__":
    print("Hello World!")
    print(df.shape)
    print(df.columns)
    print("SHAREPOINT_PASSWORD", SHAREPOINT_PASSWORD)
    print("VALUE_TEST", VALUE_TEST)

    while counter != 5:
        print(counter)
        logger.info(f"counter: {counter}")
        sleep(1)
        counter += 1
