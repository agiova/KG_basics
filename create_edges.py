from py2neo import Relationship, Graph
import json
import time
import pandas as pd

start_time = time.time()
print("Start create edges")

with open('config.json', 'r') as f:
    config = json.load(f)
f.close()

graph_address = 'http://{}:{}@localhost:7474/db/data/'.format(config['neo4j_credentials']['username'],
                                                              config['neo4j_credentials']['password'])

graph = Graph(graph_address)

path = config['path_to_data']

f = open(path + "asoiaf-{}-edges.csv".format(config["book_to_analyse"]),"r")
nodes = pd.read_csv(f)

list_nodes1 = list(nodes["Source"])
list_nodes2 = list(nodes["Target"])
weight = list(nodes["weight"])

for index, y in enumerate(list_nodes1):
    z = list_nodes2[index]
    node1 = graph.find_one('character', property_key='name', property_value=y)
    node2 = graph.find_one('character', property_key='name', property_value=z)

    graph.create(Relationship(node1, "relation_with", node2, weight= int(weight[index])))

print("--- %s seconds ---" % (time.time() - start_time))
