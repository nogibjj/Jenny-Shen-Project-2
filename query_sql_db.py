#!/usr/bin/env python

import click
from dblib.querydb import querydb
from dblib.querydb import corrticker

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
@click.option('--ticker1', default="AMZN", help='Type the name of the ticker1 here')
@click.option('--ticker2', default="AAPL", help='Type the name of the ticker2 here')
def corr(ticker1, ticker2):
    """Input two teams for historical matches"""
    corrticker(ticker1, ticker2)

# run the CLI
if __name__ == "__main__":
    cli()
