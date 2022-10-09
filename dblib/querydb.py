from databricks import sql
import os
import pandas as pd
import helpers

def querydb(ticker="AAL"):
    query = "SELECT * FROM default.all_stocks_5yr_csv where Name = '{}'".format(ticker)
    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()

        # for row in result:
        #    print(row)

    df = pd.DataFrame(result)
    df.columns = ["date", "open", "high", "low", "close", "volume", "Name"]
    toReturn = helpers.growth(df, ticker)
    print(toReturn)
    return toReturn
 
