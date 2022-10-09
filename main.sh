#! /usr/bin/env bash

#hello message
echo "Hello! Welcome to the stock analysis tool!"
chmod +x query_sql_db.py

echo "Please enter the stock ticker you would like to analyze: "
read ticker
./query_sql_db.py cli-query --ticker_name $ticker

echo "Let's compare the rate of return between two stocks. Please enter the first stock ticker: "
read ticker1
echo "Please enter the second stock ticker: "
read ticker2
./query_sql_db.py cli-query --ticker_name $ticker-name1 $ticker-name2

