import click
import pandas as pd

@click.command()
@click.option('--day', type=int, required=True, help='Your day')
@click.option('--hour', type=int, required=False, help='Your hour')
def main(day, hour):
    hour = hour or 0
    print(f'running pipe for day {day} at hour {hour or 0}')
    df = pd.DataFrame({'A': [1,2], 'B': [3,4]})
    print(df.head())
    df.to_parquet(f"output_day_{day}_{hour}.parquet")


if __name__ == '__main__':
    main()

