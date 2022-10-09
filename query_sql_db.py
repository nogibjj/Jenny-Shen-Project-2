#!/usr/bin/env python

import click
from dblib.querydb import querydb

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


# run the CLI
if __name__ == "__main__":
    cli()
