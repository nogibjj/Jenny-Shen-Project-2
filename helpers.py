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
