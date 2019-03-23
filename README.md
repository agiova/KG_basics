# KG_basics
This repo include basic scripts to build and modify a KG

## Preparation
1. Install neo4j community server edition (see `https://neo4j.com/download-center/`).
2. Then start the service in `Neo4j/neo4j-community-X.X.X/bin` by running the following command: `neo4j start` 

## Instructions
1. run the bash script `setup.sh`, it will clone the repo with the data needed to build the KG.
2. make sure that the requirements are satisfied (see `requirements.txt`)
3. check and eventually adapt `config.json`
4. run the bash script `build_kg.sh`, it will first delete the old graph, then create the new one given the input given in config.json.