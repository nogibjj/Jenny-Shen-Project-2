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
@click.option("--ticker1", default="AMZN", help="Type the name of the ticker1 here",)
@click.option("--ticker2", default="AAPL", help="Type the name of the ticker2 here",)

def cli_query1(ticker1, ticker2):
    """Execute a SQL query"""
    df = pd.read_csv("dataset/all_stocks_5yr.csv")
    ticker1 = subdataframe(df, ticker1)
    ticker2 = subdataframe(df, ticker2)
    # find the correlation between both stock price
    toReturn = ticker1["close"].corr(ticker2["close"])
    print(toReturn)
    return toReturn

# run the CLI
if __name__ == "__main__":
    cli()
