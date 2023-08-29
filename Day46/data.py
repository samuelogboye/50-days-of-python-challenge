#!/usr/bin/python3


import pandas as pd


data = {
    'Year': [2009, 2002, 2009, 2010, 2009],
    'Title': ['Brothers', 'Spider-Man', 'WatchMen', 'Inception', 'Avatar'],
    'Genre': ['Drama', 'Sci-fi', 'Drama', 'Sci-fi', 'Fantasy']
}

df = pd.DataFrame(data)
print(df)
