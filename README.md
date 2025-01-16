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
### NGINX "Load Balancer" ###
`justin799/pvs-nginx`

# Getting started #
Below you will find instructions how to use this project.
## Prerequisites ##
- Docker Desktop to run the composition (https://www.docker.com/products/docker-desktop/)
    - on operating systems without a GUI, you can use this documentation (https://docs.docker.com/engine/install/) to install docker
- MongoDB Compass to view database entries (https://www.mongodb.com/try/download/compass)
- Browser to access frontend (stock-liveview) and RabbitMQ management 
## Installing and Running ##
1. **Clone the repository**

   ```bash
   git clone https://github.com/JustinWaiz/Microservices_LB_PVS01_Waiz.git
   cd Microservices_LB_PVS01_Waiz
   ```

2. **Run the composition**

   ```bash
    docker-compose up -d
   ```

3. **View logs**

   ```bash
    docker-compose logs <container-name>
   ```

4. **Stop the composition**

   ```bash
    docker-compose down
   ```

## Access the applications ##
- Database cluster
    - Open MongoDB Compass and enter the connection string `mongodb://host.docker.internal:27017,host.docker.internal:27018,host.docker.internal:27019/?replicaSet=rs0`
- RabbitMQ
    - Access the management platform over `localhost:15672`
- Frontend "Stock-Liveview"
    - Access the frontend over `localhost:80`

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
## 03.01.2025 ##
- Path to Docker container images added
- corrected typo in "path of Docker container images"
## 05.01.2025 ##
- docker compose: adjusted healtcheck of MongoDB cluster for all consumers and liveview
- picture uploaded
## 08.01.2025: ##
- networks (rabbitmq-network, mongodb-network, frontend-network) added
- docker compose changed to use MongoDB service names in URL
## 09.01.2025: ##
- 2nd frontend added
- NGINX Loadbalancer added
## 11.01.2025: ##
- "Getting started" added to README.md
## 12.01.2025: ##
- instructions for viewing logs and stopping the composition added
## 14.01.2025: ##
- checklist removed as no longer needed
- consumer.py edited to round stock prices
- consumer image rebuilded
- image tagged: 2
- image pushed
- added overview on Docker Hub for this image
- docker compose file updated to use justin799/consumer:2
- folder nginx created
- nginx.conf moved to nginx folder
- Dockerfile created and configured
- image created, tagged and pushed to docker hub
- docker compose file adjusted with custom nginx image
- consumer tested:
  1. database deleted and all consumer stopped
  2. stock-publisher runned until every queue of RabbitMQ had approximately 22k - 23k messages
  3. all consumer started successively
  4. checked if all RabbitMQ queues were emtpy
  ## 16.01.2025 ##
  - Path to Docker container images updated with custom nginx image