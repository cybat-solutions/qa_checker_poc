import pandas as pd
import os

df = pd.DataFrame(columns=["a", "b", "c"], data=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])

VALUE_TEST = os.environ["VALUE_TEST"]

SHAREPOINT_PASSWORD = "ok boomer"

if __name__ == "__main__":
    print("Hello World!")
    print(df.shape)
    print(df.info())
    print(df)
    print(SHAREPOINT_PASSWORD)
    if VALUE_TEST == "test":
        print(VALUE_TEST, "is equal to test")
    else:
        print('env vars aren\'t working')
