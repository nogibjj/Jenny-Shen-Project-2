#!/usr/bin/env python

import click
import pandas as pd
from dblib.querydb import querydb
from helpers import subdataframe

# build a click group
@click.group()
def cli():
    """A simple CLI to query a SQL database"""


# build a click command
@cli.command()
@click.option(
    "--ticker_name",
    default="AAL",
    help="Type the name of the ticker here",
)
def cli_query(ticker_name):
    """Execute a SQL query"""
    querydb(ticker_name)

# build  click commands for query directly
@cli.command()
@click.option("--ticker1", default="AMZN", help="Type the name of the ticker1 here")
@click.option("--ticker2", default="AAPL", help="Type the name of the ticker2 here")

def corrticker(ticker1 = 'AMZN', ticker2 = 'AAPL'):
    """Execute a SQL query"""
    df = pd.read_csv("dataset/all_stocks_5yr.csv", index_col=0)
    ticker1 = subdataframe(df, ticker1)
    ticker1['pct_change'] = ticker1.loc[:,"close"].pct_change()
    ticker2 = subdataframe(df, ticker2)
    ticker2['pct_change'] = ticker2.loc[:,"close"].pct_change()
    compare = pd.merge(ticker1['pct_change'], ticker2['pct_change'], on="date").dropna()
    # find the correlation between two stocks
    result = compare["pct_change_x"].corr(compare["pct_change_y"])
    print(result)
    return result

if __name__ == "__main__":
    cli()
