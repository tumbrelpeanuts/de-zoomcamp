#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
import click

dtype = {
    'LocationID': 'Int64',
    'Borough': 'string',
    'Zone': 'string',
    'service_zone': 'string'
}

@click.command()
@click.option('--pg-user', default='root', help='PostgresSQL user')
@click.option('--pg-pass', default='root', help='PostgresSQL password')
@click.option('--pg-host', default='localhost', help='PostgresSQL host')
@click.option('--pg-port', default=5432, help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--target-table', default='taxi_zone_data', help='Target table name')
def run(pg_user, pg_pass, pg_host, pg_port, pg_db, target_table):
    engine=create_engine(f'postgresql+psycopg://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')
    url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv'

    df = pd.read_csv(url, dtype=dtype)

    df.head(0).to_sql(name=target_table,con=engine, if_exists='replace')
    df.to_sql(name=target_table, con=engine, if_exists='append')



if __name__ == '__main__':
    run()