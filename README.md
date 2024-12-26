##################### Project log #############################
25.12.2024:
project folder created
git init
README.md created
folder producer created
producer files to producer copied
producer\Dockerfile created and configured
producer\.dockerignore created and configured
stock-publisher image builded
stock-publisher image tagged
stock-publisher image published to docker
    ## first git commit ##
docker-compose.yml created
RabbitMQ added to docker compose file
Stock-Publisher added to docker compose file
MongoDB cluster added to docker compose file
    connection string: mongodb://host.docker.internal:27017,host.docker.internal:27018,host.docker.internal:27019/?replicaSet=rs0 (internal: mongodb://mongo1:27017,mongo2:27018,mongo3:27019/?replicaSet=rs0)
DB and collaction created

    ## second git commit ##
26.12.2024
folder consumer created
file consumer\consumer.py created
python script created in consumer\consumer.py
consumer\Dockerfile created and configured
consumer\requirements.txt created and configured
consumer image builded
consumer image tagged
consumer image published to docker
3 consumer added to docker compose file and configured 
healthchecks adjusted





#################### checklist ##################
Producer "Stock-Publisher"          ->      done
Rabbit MQ "Message Broker"          ->      done
Consumer                            ->      done
MongoDB Cluster                     ->      done
Frontend "Stock-Liveview"
NGINX "Load Balancer"