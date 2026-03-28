import pandas as pd
import sys

print('arguments', sys.argv)

days = sys.argv[1]
print(f'running pipe for day {days}')

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print(df.head())

df.to_parquet(f"output_day_{sys.argv[1]}.parquet")