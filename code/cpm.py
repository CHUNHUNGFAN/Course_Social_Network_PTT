#%%
import networkx as nx
from networkx.algorithms.community import k_clique_communities

f = open("relationshipValue.txt",'r')
fr = f.readlines()

G = nx.Graph()

for line in fr:
    line = line[:-2]
    line_dict = eval(line)
    G.add_edge(line_dict['source'],line_dict['target'])

c = list(k_clique_communities(G, 4))

for _ci in c:
    print(_ci)
    print()


#%%

f = open("accountsWithEdge.txt",'r')
fr = f.readlines()

for line in fr:
    #delete \n and , in line
    line = line[:-2]
    #change string to dictionary
    line_dict = eval(line)
    #check id in which frozenset
    for _index in range(len(c)):
        if line_dict['id'] in c[_index]:
            line_dict['group'] = _index + 1
    #print out the results
    print(line_dict,end=",")
    print()