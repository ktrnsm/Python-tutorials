#trend follow
from pytrends.request import TrendReq
import pandas as pd
import time

def get_related_queries(kw_list):
    pytrends = TrendReq(hl='tr-TR',timeout=(10,25))
    pytrends.build_payload(kw_list, cat=0, timeframe='today 1-m', geo='TR', gprop='')
    related_queries = pytrends.related_queries()
    return related_queries

while True:
    related_queries_data = get_related_queries(['rüyada'])
    related_queries_df = pd.concat([related_queries_data['rüyada']['top'], related_queries_data['rüyada']['rising']])
    related_queries_df.to_csv('related_queries.csv', index=False)
    time.sleep(24*60*60) # wait for 24 hours
