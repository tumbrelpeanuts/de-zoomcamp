#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
import click


@click.command()
@click.option('--pg-user', default='root', help='PostgresSQL user')
@click.option('--pg-pass', default='root', help='PostgresSQL password')
@click.option('--pg-host', default='localhost', help='PostgresSQL host')
@click.option('--pg-port', default=5432, help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--year', default=2025, type=int, help='Year of the data')
@click.option('--month', default=11, type=int, help='Month of the data')
@click.option('--target-table', default='green_taxi_data', help='Target table name')
def run(pg_user, pg_pass, pg_host, pg_port, pg_db, year, month, target_table):
    engine=create_engine(f'postgresql+psycopg://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')
    url = f'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_{year}-{month}.parquet'

    df = pd.read_parquet(url)
    df.head(0).to_sql(name=target_table, con=engine, if_exists='replace')
    df.to_sql(name=target_table, con=engine, if_exists='append')


if __name__ == '__main__':
    run()