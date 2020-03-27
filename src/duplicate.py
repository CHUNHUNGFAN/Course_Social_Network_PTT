#%%
import json
import os
from pandas import DataFrame
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns',None)

path = "../dataset/"
allFileList = os.listdir(path)

class Article():
    def __init__(self, id):
        self.id = id
        self.user = []

articles = []
accounts = []

for dataset in range(len(allFileList)):
    with open(path + allFileList[dataset]) as file:
        result = json.load(file)

    # result: dictionary
    counter = 0
    for article in result["articles"]:
        articles.append(Article(article["article_id"]))
        
        # article["messages"]: list
        for comment in article["messages"]:
            articles[counter].user.append(comment["push_userid"])
            accounts.append(comment["push_userid"])

        counter += 1

Boxes = {'Account': accounts}

df = DataFrame(Boxes, columns= ['Account'])

dups_color = df.pivot_table(index=['Account'], aggfunc='size')

print(dups_color)


