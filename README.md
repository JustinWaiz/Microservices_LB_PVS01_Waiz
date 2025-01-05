# Distributed Financial System

This project implements a **distributed financial system** designed to simulate the processing and storage of fictitious financial data. The system is structured with several key components to ensure scalability, fault tolerance, and reliability.

## Overview

- **Data Generation**  
  A producer generates synthetic financial data simulating transactions (e.g., buy/sell events) for specific companies. The producer, implemented in Go, is packaged into a Docker container and sends data to a RabbitMQ message broker.

- **Message Broker**  
  RabbitMQ acts as the intermediary, holding data in queues for further processing. Separate queues are created for each company, allowing specific consumers to process distinct datasets.

- **Data Processing**  
  Consumers retrieve data from RabbitMQ queues in batches of 1000, compute the average price of transactions, and store the results in a MongoDB database. Each consumer is dedicated to processing data from a single queue.

- **Database**  
  MongoDB is deployed as a cluster (replica set) to ensure high availability and fault tolerance. Aggregated data is stored in a structured format, accessible for visualization.

- **Visualization**  
  A frontend application provides a live view of the aggregated financial data. Packaged as a Docker container, the frontend operates with redundancy, using multiple instances managed by an NGINX load balancer to distribute requests evenly and maintain service availability.

## Objectives

- Demonstrate a complete lifecycle of distributed system components, from data production to visualization.
- Ensure fault tolerance with clustered database architecture and redundant frontend instances.
- Package and deploy all components using Docker, enabling seamless integration and scalability.

This project showcases the integration of modern tools and technologies like **Docker**, **RabbitMQ**, **MongoDB**, and **Node.js** to create a robust distributed system.

# Docker container images #
### Producer "Stock-Publisher" ###
`justin799/stock-publisher`
### Consumer ###
`justin799/consumer`
### Frontend "Stock-Liveview" ###
`justin799/stock-liveview`

# Project log #
## 25.12.2024 ##
- project folder created
- git init
- README.md created
- folder producer created
- producer files to producer copied
- producer\Dockerfile created and configured
- producer\.dockerignore created and configured
- stock-publisher image builded
- stock-publisher image tagged
- stock-publisher image published to docker
- docker-compose.yml created
- RabbitMQ added to docker compose file
- Stock-Publisher added to docker compose file
- MongoDB cluster added to docker compose file
    - connection string: mongodb://host.docker.internal:27017,host.docker.internal:27018,host.docker.internal:27019/?replicaSet=rs0 (internal: mongodb://mongo1:27017,mongo2:27018,mongo3:27019/?replicaSet=rs0)
- DB and collaction created
## 26.12.2024 ##
- folder consumer created
- file consumer\consumer.py created
- python script created in consumer\consumer.py
- consumer\Dockerfile created and configured
- consumer\requirements.txt created and configured
- consumer image builded
- consumer image tagged
- consumer image published to docker
- 3 consumer added to docker compose file and configured 
- healthchecks adjusted
## 01.01.2025 ##
- README.md formated
- folder frontend created
- frontend files to frontend copied
- frontend\Dockerfile configured
- frontend\.dockerignore configured
- stock-liveview image builded
- stock-liveview image tagged
- stock-liveview image published to docker
- 1 frontend added to docker compose file and configured
- all containers tested (all running properly)
    - producer successfully create and sends data to RabbitMQ
    - RabbitMQ successfuly holds data in queues
    - 3 consumers successfully retrieve data from RabbitMQ queues, compute the average price and store the results in the MongoDB cluster
    - frontend presents provides a live view of the financial data stored in the MongoDB cluster
- checklist formated
- introduction to project written
- open points: 
    - chapter "Getting started (How to use this project/files)"
    - NGINX "Load Balancer"
- "all containers tested" updated
## 03.01.2024 ##
- Path to Docker container images added
- corrected typo in "path of Docker container images"
## 05.01.2024 ##
- docker compose: adjusted healtcheck of MongoDB cluster for all consumers and liveview



# Checklist #
| component | state|
| ------------ | ------------ |
| Producer "Stock-Publisher" | done |
| Rabbit MQ "Message Broker" | done |
| Consumer | done |
| MongoDB Cluster | done |
| Frontend "Stock-Liveview" | done (1/2) |
| NGINX "Load Balancer" | not started |