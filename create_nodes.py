from py2neo import Node, Graph
import json
import time
import pandas as pd

start_time = time.time()
print("Start create nodes")

with open('config.json', 'r') as f:
    config = json.load(f)
f.close()

graph_address = 'http://{}:{}@localhost:7474/db/data/'.format(config['neo4j_credentials']['username'],
                                                              config['neo4j_credentials']['password'])

graph = Graph(graph_address)

path = config['path_to_data']

f = open(path + "asoiaf-{}-nodes.csv".format(config["book_to_analyse"]),"r")
nodes = pd.read_csv(f)

list_nodes = list(nodes["Id"])

# create nodes
for x in list(set(list_nodes)):
    if not graph.find_one('character', property_key='name', property_value=x):
        graph.create(Node('character', name=x))

print("--- %s seconds ---" % (time.time() - start_time))
