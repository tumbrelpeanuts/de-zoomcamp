import pandas as pd
import click
from sqlalchemy import create_engine


@click.command()
@click.option('--pg-user', default="root", help="PostgreSQL user")
@click.option('--pg-pass', default="root", help="PostgreSQL password")
@click.option('--pg-host', default="localhost", help="PostgreSQL host")
@click.option('--pg-port', default=5432, type=int, help="PostgreSQL port")
@click.option('--pg-db', default="ny_taxi", help="PostgreSQL database name")
@click.option('--trip-table', default="green_taxi_data", help="Green taxi trip table name")
@click.option('--zone-table', default="taxi_zone", help="Taxi zone lookup table name")
def run(pg_user, pg_pass, pg_host, pg_port, pg_db, trip_table, zone_table):
    engine=create_engine(f'postgresql+psycopg://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')

    trip_data(engine, trip_table)
    zone_data(engine, zone_table)


def trip_data(engine, trip_table):
    prefix = 'https://d37ci6vzurychx.cloudfront.net/trip-data/'
    url = f'{prefix}green_tripdata_2025-11.parquet'

    df_trip = pd.read_parquet(url)

    df_trip.head(0).to_sql(
        name=trip_table,
        con=engine,
        if_exists='replace'
    )

    df_trip.to_sql(
        name=trip_table,
        con=engine,
        if_exists='append'
    )


def zone_data(engine, zone_table):
    prefix='https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/'
    url=f'{prefix}taxi_zone_lookup.csv'

    df_zone=pd.read_csv(url)

    df_zone.head(0).to_sql(
        name=zone_table,
        con=engine,
        if_exists='replace'
    )

    df_zone.to_sql(
        name=zone_table,
        con=engine,
        if_exists='append'
    )


if __name__ == "__main__":
    run()

