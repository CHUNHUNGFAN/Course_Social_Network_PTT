#%%
import json
import os

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
        # article["messages"]: list
        for comment in article["messages"]:
            if comment["push_userid"] == "mlnaml123":
                print(article["article_id"],end=" ")
                print(comment["push_datetime"])

        counter += 1