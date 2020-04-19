from IPython.display import display
import numpy as np
import pandas as pd

imdb = pd.read_csv('./data.csv')

#1
s = imdb[imdb.budget==imdb.budget.max()]
display(s.original_title)
