from IPython.display import display
import numpy as np
import pandas as pd

imdb = pd.read_csv('./data.csv')
display(imdb.columns)

#1
s = imdb[imdb.budget==imdb.budget.max()]
display(s.original_title)

#2
s = imdb[imdb.runtime==imdb.runtime.max()]
display(s.original_title)

#3
s = imdb[imdb.runtime==imdb.runtime.min()]
display(s.original_title)

#4
s = imdb.runtime.mean()
display(s)

#5
s = imdb.runtime.median()
display(s)

#6
s = imdb[(imdb.revenue-imdb.budget)==(imdb.revenue-imdb.budget).max()]
display(s.original_title)

#7
s = imdb[(imdb.revenue-imdb.budget)==(imdb.revenue-imdb.budget).min()]
display(s.original_title)

#8
s = imdb[(imdb.revenue-imdb.budget>0)].count()
display(s.original_title)

#8
sub = imdb[imdb.release_year==2008]
s = sub[sub.revenue==sub.revenue.max()]
display(s.original_title)

#10
sub = imdb[(imdb.release_year>=2012)&(imdb.release_year<=2014)]
s = sub[(sub.revenue-sub.budget)==(sub.revenue-sub.budget).min()]
display(s.original_title)

#11
set = {'Action', 'Adventure', 'Drama', 'Comedy', 'Thriller'}
data = pd.Series(dtype=np.int, index =set)
for x in set:
    data.loc[x]=len(imdb[imdb.genres.str.contains(x, na=False)])
display(data.sort_values(ascending=False).index[0])

#12
sub = imdb[(imdb.revenue-imdb.budget)>0]
set = {'Action', 'Adventure', 'Drama', 'Comedy', 'Thriller'}
data = pd.Series(dtype=np.int, index =set)
for x in set:
    data.loc[x]=len(sub[sub.genres.str.contains(x, na=False)])
display(data.sort_values(ascending=False).index[0])

#13
s = imdb['director'].value_counts().index[0]
display(s)

#14
sub = imdb[(imdb.revenue-imdb.budget)>0]
s = sub['director'].value_counts().index[0]
display(s)

#15
s = imdb.groupby(['director'])['revenue'].sum().sort_values(ascending=False).index[0]
display(s)

#16
set = {'Emma Watson', 'Johnny Depp', 'Michelle Rodriguez', 'Orlando Bloom', 'Rupert Grint'}
data = pd.Series(dtype=np.int, index =set)
for x in set:
    sub=imdb[imdb.cast.str.contains(x, na=False)]
    data.loc[x]=(sub.revenue-sub.budget).sum()
display('#16 ',data.sort_values(ascending=False).index[0])

#17
set = {'Nicolas Cage', 'Danny Huston', 'Kirsten Dunst', 'Jim Sturgess', 'Sami Gayle'}
data = pd.Series(dtype=np.int, index =set)
for x in set:
    sub=imdb[(imdb.release_year==2012)&imdb.cast.str.contains(x, na=False)]
    data.loc[x]=(sub.revenue-sub.budget).sum()
display('#17 ',data.sort_values(ascending=True).index[0])