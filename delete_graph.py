from py2neo import Graph
import json

with open('config.json', 'r') as f:
    config = json.load(f)
f.close()

graph_address = 'http://{}:{}@localhost:7474/db/data/'.format(config['neo4j_credentials']['username'],
                                                              config['neo4j_credentials']['password'])

graph = Graph(graph_address)

graph.delete_all()

print('Old graph successfully deleted')
