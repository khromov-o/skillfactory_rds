from IPython.display import display
import numpy as np
import pandas as pd
from itertools import combinations

imdb = pd.read_csv('./data.csv', parse_dates= ['release_date'])
display(imdb.columns)
imdb['profit'] = imdb['revenue']-imdb['budget']


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
genresSet = set()
for x in imdb.genres.unique():
    for y in x.split('|'):
        genresSet.add(y)

ids = []
genres = []
for x in genresSet:
    temp = imdb[imdb.genres.str.contains(x, na=False)].imdb_id.values
    ids.extend(temp)
    temp =  [x]*len(temp)
    genres.extend(temp)

d = {'imdb_id':ids, 'genre':genres}
genresdf = pd.DataFrame(data=d)

s = genresdf.groupby(['genre'])['imdb_id'].count().sort_values(ascending=False).index[0]
display('#11',s)

#12
sub = genresdf.merge(imdb[imdb.profit>0], on='imdb_id', how='inner')
s = sub.groupby(['genre'])['imdb_id'].count().sort_values(ascending=False).index[0]
display('#12',s)

#13
s = imdb['director'].value_counts().index[0]
display('#13 ',s)

#14
sub = imdb[(imdb.revenue-imdb.budget)>0]
s = sub['director'].value_counts().index[0]
display('#14 ',s)

#15
s = imdb.groupby(['director'])['revenue'].sum().sort_values(ascending=False).index[0]
display('#15 ',s)

#16
actorsSet = set()
for x in imdb.cast.unique():
    for y in x.split('|'):
        actorsSet.add(y)

ids = []
actors = []
for x in actorsSet:
    temp = imdb[imdb.cast.str.contains(x, na=False)].imdb_id.values
    ids.extend(temp)
    temp =  [x]*len(temp)
    actors.extend(temp)

d = {'imdb_id':ids, 'actor':actors}
actorsdf = pd.DataFrame(data=d)

sub = actorsdf.merge(imdb, on='imdb_id', how='inner')
s = sub.groupby(['actor'])['profit'].sum().sort_values(ascending=False).index[0]
display('#16 ',s)

#17
sub = actorsdf.merge(imdb, on='imdb_id', how='inner')
s = sub[sub.release_year==2012].groupby(['actor'])['profit'].sum().sort_values(ascending=True).index[0]
display('#17 ',s)

#18
sub = actorsdf.merge(imdb[imdb.budget>imdb.budget.mean()], on='imdb_id', how='inner')
s = sub.groupby('actor')['imdb_id'].count().sort_values(ascending=False).index[0]
display('#18 ',s)

#19
sub = genresdf.merge(actorsdf[actorsdf.actor=='Nicolas Cage'], on='imdb_id', how='inner')
s = sub.groupby('genre')['imdb_id'].count().sort_values(ascending=False).index[0]
display('#19 ',s)

#20
studios = set()
for x in imdb.production_companies.unique():
    for y in x.split('|'):
        studios.add(y)

ids = []
studioss = []
for x in studios:
    temp = imdb[imdb.production_companies.str.contains(x, na=False)].imdb_id.values
    ids.extend(temp)
    temp = [x] * len(temp)
    studioss.extend(temp)

d = {'imdb_id':ids, 'studio':studioss}
studiodf = pd.DataFrame(data=d)

def fixStudio(x):
    res = x
    if x in ['Warner Bros.', 'Warner Bros. Pictures']:
        res = 'Warner Bros.'
    if x in ['Universal Studios', 'Universal Pictures', 'Universal Pictures Corporation', 'Universal']:
        res = 'Universal Pictures (Universal)'
    if x in ['Paramount Vantage', 'Paramount Classics']:
        res = 'Paramount Classics'
    if x in ['Columbia Pictures Corporation', 'Columbia Pictures']:
        res = 'Columbia Pictures'
    if x in ['Twentieth Century Fox', '20th Century Fox', 'Twentieth Century Fox Film Corporation']:
        res = 'Twentieth Century Fox Film Corporation'
    if x in ['Miramax Films', 'Miramax']:
        res = 'Miramax Films'
    if x in ['Walt Disney Pictures', 'Walt Disney']:
        res = 'Walt Disney Pictures'
    return res

studiodf.studio = studiodf.studio.apply(fixStudio)

s = studiodf.groupby('studio')['imdb_id'].count().sort_values(ascending=False).index[0]
display('#20 ',s)

#21
sub = studiodf.merge(imdb[imdb.release_year==2015], on='imdb_id', how='inner')
s =  sub.groupby('studio')['imdb_id'].count().sort_values(ascending=False).index[0]
display('#21 ',s)

#22
sub = studiodf.merge(genresdf[genresdf.genre=='Comedy'], on='imdb_id', how='inner').copy()
sub = sub.merge(imdb, on='imdb_id', how='inner').copy()
s = sub.groupby('studio').sum()['profit'].sort_values(ascending=False).index[0]
display('#22 ',s)

#23
sub = studiodf.merge(imdb[imdb.release_year==2012], on='imdb_id', how='inner').copy()
s = sub.groupby('studio').sum()['profit'].sort_values(ascending=False).index[0]
display('#23 ',s)

#24
sub = imdb.merge(studiodf[studiodf.studio=='Paramount Pictures'], on='imdb_id', how='inner').copy()
s = sub.groupby('imdb_id').sum()['profit'].sort_values(ascending=True).index[0]
display('#24 ',s)

#25
sub = imdb.merge(studiodf, on='imdb_id', how='inner').copy()
s = sub.groupby('release_year').sum()['profit'].sort_values(ascending=False).index[0]
display('#25 ',s)

#26
sub = imdb.merge(studiodf[studiodf.studio=='Warner Bros.'], on='imdb_id', how='inner').copy()
s = sub.groupby('release_year').sum()['profit'].sort_values(ascending=False).index[0]
display('#26 ',s)

#27
imdb['month'] = imdb['release_date'].dt.month

s = imdb.groupby('month')['imdb_id'].count().sort_values(ascending=False).index[0]
display('#27 ',s)

#28
s = imdb[(imdb.month==6)|(imdb.month==7)|(imdb.month==8)]['imdb_id'].count()
display('#28 ',s)

#29
s = imdb[(imdb.month==12)|(imdb.month==1)|(imdb.month==2)].groupby('director')['imdb_id'].count().sort_values(ascending=False).index[0]
display('#29 ',s)

#30
pivot = imdb.pivot_table(values=['profit'], index=['release_year'], columns=['month'], aggfunc='sum')
maxValue = pivot.idxmax(axis=1)
display('#30', maxValue.describe())

#31
imdb['clen'] = imdb['original_title'].str.len()
sub = imdb.merge(studiodf, on='imdb_id', how='inner').copy()
s = sub.groupby('studio')['clen'].mean().sort_values(ascending=False).index[0]
display('#31', s)

#32
imdb['wlen'] = imdb['original_title'].apply(lambda  x : len(x.split()))
sub = imdb.merge(studiodf, on='imdb_id', how='inner').copy()
s = sub.groupby('studio')['wlen'].mean().sort_values(ascending=False)
display('#32', s)

#33
wordSet = set()
imdb['original_title'].str.lower().str.split().apply(wordSet.update)
display('#33', len(wordSet))

#34
display('#34', imdb[imdb.vote_average>imdb.vote_average.quantile(.99)].original_title)

#35
def getActorPairs(cast):
    pairs = []
    for pair in combinations(cast.split('|'), 2):
        pairs.append(' and '.join(sorted(pair)))
    return ' | '.join(pairs)

imdb['actors'] = imdb['cast'].apply(getActorPairs)
actorsPairs = imdb.actors.str.get_dummies(sep='|')
maxValue = actorsPairs.idxmax(axis=1)
display('#35 ', maxValue.describe())

#36
def getProfit(x):
    if x>0:
        return 1
    else:
        return 0

def getProfitB(x):
    if x>0:
        return 0
    else:
        return 1

imdb['profit_a'] = imdb.profit.apply(getProfit)
imdb['profit_b'] = imdb.profit.apply(getProfitB)
directors = ['Quentin Tarantino','Steven Soderbergh','Robert Rodriguez', 'Christopher Nolan', 'Clint Eastwood']
sub = imdb[imdb.director.isin(directors)].groupby(['director']).agg({'profit_a': 'sum', 'profit_b': 'sum'})
sub['profit_result'] = sub['profit_a']/(sub['profit_a']+sub['profit_b'])

display('#36', sub)