#%%
import json
import os

path = "../dataset/"
allFileList = os.listdir(path)

accounts = []

file = open("accountsDuplicateTimes.txt",'r')
fileR = file.readlines()
for line in fileR:
    line = line.split()
    accounts.append(line[0])

accountsArticles = [[] for row in range(len(accounts))]

for dataset in range(len(allFileList)):
    with open(path + allFileList[dataset]) as file:
        result = json.load(file)

    # result: dictionary
    counter = 0
    for article in result["articles"]:
        articleId = article["article_id"]
        
        # article["messages"]: list
        for comment in article["messages"]:
            userId = comment["push_userid"]
            if userId in accounts:
                userIndex = accounts.index(userId)
                accountsArticles[userIndex].append(articleId)

#%%
# remove duplicated article id in accountsArticles list
for accountArticlesIndex in range(len(accountsArticles)):
    accountsArticles[accountArticlesIndex] = list(dict.fromkeys(accountsArticles[accountArticlesIndex]))

#%%
#calculate common post rate and print out the edge
relationship = [[0 for column in range(len(accounts))] for row in range(len(accounts))]
relationshipValue = [[0 for column in range(len(accounts))] for row in range(len(accounts))]
for accountArticlesRowIndex in range(len(accountsArticles)):
    for accountArticlesColumnIndex in range(accountArticlesRowIndex + 1, len(accountsArticles)):
        checkString = str(accountArticlesRowIndex) + " " + str(accountArticlesColumnIndex)
        print(checkString)
        firstAccountArticle = accountsArticles[accountArticlesRowIndex]
        secondAccountArticle = accountsArticles[accountArticlesColumnIndex]
        commonPostNumber = len(set(firstAccountArticle).intersection(secondAccountArticle))
        totalPostNumber = len(firstAccountArticle) + len(secondAccountArticle)
        commonPostRate = float(commonPostNumber) / totalPostNumber
        if commonPostRate >= 0.05:
            relationship[accountArticlesRowIndex][accountArticlesColumnIndex] += 1
            relationshipValue[accountArticlesRowIndex][accountArticlesColumnIndex] += commonPostRate

#%%
#collect account index have links with other accounts
accountWithEdge = []
for row in range(len(relationship)):
    for column in range(row + 1, len(relationship)):
        if relationship[row][column] != 0:
            if row not in accountWithEdge:
                accountWithEdge.append(row)
            if column not in accountWithEdge:
                accountWithEdge.append(column)

# print(accountWithEdge)
# print(len(accountWithEdge))
# print(len(accounts))

# %%
#print out the edge link
for row in range(len(relationship)):
    for column in range(row + 1, len(relationship)):
        if relationship[row][column] != 0:
            _string = "{\"source\": \"" + str(accounts[row]) + "\", \"target\": \"" + str(accounts[column]) + "\", \"value\": " + str(relationshipValue[row][column]) + "},"
            print(_string)
#%%
for account in accounts:
    _string = "{\"id\": \"" + account + "\", \"group\": 1},"
    print(_string)
# %%
#print out account just have links
for accountIndex in accountWithEdge:
    _string = "{\"id\": \"" + accounts[accountIndex] + "\", \"group\": 1},"
    print(_string)