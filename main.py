import pandas as pd
import os

df = pd.DataFrame(columns=["a", "b", "c"], data=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])


if __name__ == "__main__":
    print("Hello World!")
    print(df.shape)
    print(df.info())
    print(df)
    print(os.environ.get("VALUE_TEST"))
