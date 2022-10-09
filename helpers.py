import numpy as np


def subdataframe(df, tick):

    ndf = df[df["Name"] == tick]
    return ndf


def growth(df, tick):
    # list of stock dataframes
    ticker = subdataframe(df, tick)
    # find mini and maxi of each stocks
    mini = float(ticker["close"][np.argmin(ticker.date)])
    maxi = float(ticker["close"][np.argmax(ticker.date)])
    # find the abosolute difference between both stock price
    diff = maxi - mini
    # find the percentage growth
    toReturn = (diff / mini) * 100
    return toReturn

def corrticker(df, ticker1, ticker2):
    # list of stock dataframes
    ticker1 = subdataframe(df, ticker1)
    ticker2 = subdataframe(df, ticker2)
    # find the correlation between both stock price
    toReturn = ticker1["close"].corr(ticker2["close"])
    return toReturn
