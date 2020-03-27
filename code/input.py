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
    print(dataset)
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
print(len(accounts))
account_duplicate = {i:accounts.count(i) for i in accounts}
print(account_duplicate)